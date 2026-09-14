import assert from "node:assert/strict";
import {readFile} from "node:fs/promises";
import test from "node:test";

const source = await readFile(new URL("../browser_storage.js", import.meta.url), "utf8");
const {default: render} = await import(`data:text/javascript;base64,${Buffer.from(source).toString("base64")}`);
const key = "ccna:200-301:v1.1:set-01:progress:v1";
const backup = () => ({schema_version: 1, bank_id: "ccna-200-301-v1.1-set-01",
  submissions: {}, flags: [], wrong_answers: {}});
let sequence = 0;
const token = () => (++sequence).toString(16).padStart(32, "0");

function setup(initial = null) {
  const items = new Map(initial === null ? [] : [[key, initial]]);
  const storage = {
    writes: 0,
    getItem: name => items.get(name) ?? null,
    setItem(name, value) { this.writes++; items.set(name, value); },
  };
  Object.defineProperty(globalThis, "localStorage", {configurable: true, value: storage});
  Object.defineProperty(globalThis, "navigator", {configurable: true, value: {}});
  return storage;
}

function client(session = "session-1", host = {}) {
  const events = [];
  return {
    events,
    host,
    load() { this.send("load", "load"); },
    save(payload, request = JSON.stringify(payload)) { this.send("save", request, JSON.stringify(payload)); },
    replace(payload, replacement_id = token(), expected_baseline = this.last()?.baseline_id) {
      this.send("replace", `replace:${replacement_id}:${JSON.stringify(payload)}`, JSON.stringify(payload),
                {replacement_id, expected_baseline});
      return replacement_id;
    },
    send(operation, request_id, serialized, extra = {}) {
      render({parentElement: host, data: {operation, request_id, serialized, storage_key: key, session_id: session, ...extra},
              setStateValue: (name, event) => { assert.equal(name, "event"); events.push(event); }});
    },
    last() { return events.at(-1); },
  };
}

test("first load never writes; save survives a fresh browser component", () => {
  const storage = setup();
  const tab = client();
  tab.load();
  assert.deepEqual(tab.last(), {status: "loaded", request_id: "load", payload: null, baseline_id: tab.last().baseline_id});
  assert.equal(typeof tab.last().baseline_id, "string");
  assert.equal(storage.writes, 0);
  const payload = {wrong_answers: {"CCNA1-002": {response: ["B"]}}};
  tab.save(payload, "hash-one");
  assert.deepEqual(tab.last(), {status: "saved", request_id: "hash-one", baseline_id: tab.last().baseline_id});
  const reopened = client("new-session");
  reopened.load();
  assert.deepEqual(reopened.last().payload, payload);
});

test("repeated load/save renders do not cause event rerun loops or duplicate writes", () => {
  const storage = setup();
  const tab = client();
  tab.load(); tab.load(); tab.load();
  assert.equal(tab.events.length, 1);
  tab.save({answer: ["A"]}); tab.save({answer: ["A"]}); tab.save({answer: ["A"]});
  assert.equal(tab.events.length, 2);
  assert.equal(storage.writes, 1);
  tab.save({answer: ["B"]});
  assert.equal(tab.events.length, 3);
  assert.equal(storage.writes, 2);
});

test("corrupted or non-object JSON is preserved and blocks writes", () => {
  for (const raw of ["{broken", "[]", "null", '"string"']) {
    const storage = setup(raw);
    const tab = client();
    tab.load(); tab.load();
    assert.equal(tab.last().code, "corrupt");
    assert.equal(tab.events.length, 1);
    tab.save({new: true});
    assert.equal(tab.last().code, "uninitialized");
    assert.equal(storage.writes, 0);
    assert.equal(storage.getItem(key), raw);
  }
});

test("blocked storage reports an error once and never claims to save", () => {
  setup();
  Object.defineProperty(globalThis, "localStorage", {configurable: true, get() {
    throw new DOMException("blocked", "SecurityError");
  }});
  const tab = client();
  tab.load(); tab.load();
  assert.equal(tab.last().code, "unavailable");
  assert.equal(tab.events.length, 1);
});

test("quota errors preserve existing data and do not loop", () => {
  const raw = '{"old":true}';
  const storage = setup(raw);
  storage.setItem = () => { throw new DOMException("full", "QuotaExceededError"); };
  const tab = client();
  tab.load();
  tab.save({new: true}); tab.save({new: true});
  assert.equal(tab.last().code, "quota");
  assert.equal(tab.events.length, 2);
  assert.equal(storage.getItem(key), raw);
});

test("a stale second tab cannot replace progress saved by the first", () => {
  const storage = setup();
  const first = client("first");
  const second = client("second");
  first.load(); second.load();
  first.save({first: true});
  second.save({second: true});
  assert.equal(second.last().code, "conflict");
  assert.deepEqual(JSON.parse(storage.getItem(key)), {first: true});
  second.save({first: true});
  assert.equal(second.last().status, "saved");
});

test("a Python reconnect on the same host resets the baseline and emits a new load", () => {
  const storage = setup();
  const first = client("first");
  first.load(); first.save({answer: true});
  const reconnect = client("new-python-session", first.host);
  reconnect.load();
  assert.deepEqual(reconnect.last().payload, {answer: true});
  const prematureSave = client("another-python-session", first.host);
  prematureSave.save({discarded: true});
  assert.equal(prematureSave.last().code, "uninitialized");
  assert.deepEqual(JSON.parse(storage.getItem(key)), {answer: true});
});

test("Web Locks serialize concurrent tabs and skip obsolete queued commands", async () => {
  const storage = setup();
  let queue = Promise.resolve();
  globalThis.navigator.locks = {request(_name, callback) {
    const next = queue.then(callback);
    queue = next.catch(() => {});
    return next;
  }};
  const first = client("first");
  const second = client("second");
  first.load(); second.load();
  await queue;
  first.save({first: true}); second.save({second: true});
  await queue;
  assert.equal(first.last().status, "saved");
  assert.equal(second.last().code, "conflict");
  assert.deepEqual(JSON.parse(storage.getItem(key)), {first: true});
  first.save({obsolete: true}); first.save({latest: true});
  await queue;
  assert.deepEqual(JSON.parse(storage.getItem(key)), {latest: true});
  assert.equal(storage.writes, 2);
});

test("switching storage keys preserves both sets and requires a fresh read", () => {
  const storage = setup();
  const host = {};
  const events = [];
  const secondKey = "ccna:200-301:v1.1:set-02:progress:v1";
  const send = (storage_key, operation, request_id, payload) => render({
    parentElement: host,
    data: {session_id: "same-session", storage_key, operation, request_id, serialized: JSON.stringify(payload)},
    setStateValue: (_name, event) => events.push(event),
  });
  send(key, "load", "load");
  send(key, "save", "first-answer", {bank_id: "set-01", answer: ["B"]});
  send(secondKey, "save", "premature", {bank_id: "set-02", answer: ["C"]});
  assert.equal(events.at(-1).code, "uninitialized");
  assert.equal(storage.getItem(secondKey), null);
  send(secondKey, "load", "load");
  assert.equal(events.at(-1).payload, null);
  send(secondKey, "save", "second-answer", {bank_id: "set-02", answer: ["C"]});
  send(key, "load", "load");
  assert.deepEqual(events.at(-1).payload, {bank_id: "set-01", answer: ["B"]});
  assert.deepEqual(JSON.parse(storage.getItem(secondKey)), {bank_id: "set-02", answer: ["C"]});
});

test("an already-open Set 01 bridge preserves its read baseline during upgrade", () => {
  const raw = JSON.stringify({bank_id: "set-01", answer: ["B"]});
  const storage = setup(raw);
  const host = {};
  host[Symbol.for("ccna.set01.browserStorage.state.v1")] = {
    sessionId: "existing-session", ready: true, baseline: raw, lastRequest: "save:old-hash",
  };
  const upgraded = client("existing-session", host);
  upgraded.save({bank_id: "set-01", answer: ["C"]}, "new-hash");
  assert.equal(upgraded.last().status, "saved");
  assert.deepEqual(JSON.parse(storage.getItem(key)), {bank_id: "set-01", answer: ["C"]});
});

test("confirmed replacement recovers corrupt, unsupported and invalid stored data without an early write", () => {
  for (const raw of ["{broken", "[]", "null", '"text"', '{"schema_version":2}', '{"submissions":false}']) {
    const storage = setup(raw);
    const otherKey = key.replace("set-01", "set-02");
    storage.setItem(otherKey, "other-set-history");
    storage.writes = 0;
    const tab = client();
    tab.load();
    const observed = tab.last().baseline_id;
    assert.equal(typeof observed, "string");
    assert.equal(storage.getItem(key), raw);
    assert.equal(storage.writes, 0);
    tab.replace(backup(), token(), observed);
    assert.equal(tab.last().status, "saved");
    assert.notEqual(tab.last().baseline_id, observed);
    assert.deepEqual(JSON.parse(storage.getItem(key)), backup());
    assert.equal(storage.getItem(otherKey), "other-set-history");
    const reopened = client("reopened");
    reopened.load();
    assert.deepEqual(reopened.last().payload, backup());
    tab.save({...backup(), flags: ["CCNA1-001"]});
    assert.equal(tab.last().status, "saved", "successful recovery initializes ordinary saves");
  }
});

test("replacement requires an actual read and the exact observed baseline", () => {
  const storage = setup("{broken");
  const tab = client();
  tab.replace(backup(), token(), "invented");
  assert.equal(tab.last().code, "uninitialized");
  tab.load();
  tab.replace(backup(), token(), "invented");
  assert.equal(tab.last().code, "stale_replacement");
  tab.replace(backup(), token(), "");
  assert.equal(tab.last().code, "invalid_request");
  assert.equal(storage.writes, 0);
  assert.equal(storage.getItem(key), "{broken");
});

test("malformed or wrong-bank replacements leave the raw baseline unchanged", () => {
  const storage = setup("{broken");
  const tab = client();
  tab.load();
  const observed = tab.last().baseline_id;
  for (const serialized of ["{bad", "[]", "null", "42", '{}', JSON.stringify({...backup(), bank_id: "ccna-200-301-v1.1-set-02"})]) {
    const replacement_id = token();
    tab.send("replace", `invalid-${replacement_id}`, serialized, {replacement_id, expected_baseline: observed});
    assert.equal(tab.last().code, "invalid_replacement");
  }
  assert.equal(storage.writes, 0);
  assert.equal(storage.getItem(key), "{broken");
});

test("duplicate pending replacement retains the same acknowledgement and cannot replay after later work", () => {
  const storage = setup("{broken");
  const tab = client();
  tab.load();
  const observed = tab.last().baseline_id;
  const operation = tab.replace(backup(), token(), observed);
  const acknowledged = tab.last();
  const eventCount = tab.events.length;
  tab.replace(backup(), operation, observed);
  assert.strictEqual(tab.last(), acknowledged);
  assert.equal(tab.events.length, eventCount);
  assert.equal(storage.writes, 1);
  const newer = {...backup(), flags: ["CCNA1-001"]};
  tab.save(newer);
  tab.replace(backup(), operation, tab.last().baseline_id);
  assert.equal(tab.last().code, "replayed");
  assert.deepEqual(JSON.parse(storage.getItem(key)), newer);
  assert.equal(storage.writes, 2);
});

test("a replacement token cannot be reused with different content after a failed attempt", () => {
  const storage = setup("{broken");
  const tab = client();
  tab.load();
  const observed = tab.last().baseline_id;
  const operation = tab.replace({bank_id: "wrong-set"}, token(), observed);
  assert.equal(tab.last().code, "invalid_replacement");
  tab.replace(backup(), operation, observed);
  assert.equal(tab.last().code, "replayed");
  tab.replace(backup(), token(), observed);
  assert.equal(tab.last().status, "saved");
  assert.equal(storage.writes, 1);
});

test("quota failures preserve corrupt data and need a new token to retry", () => {
  const storage = setup("{broken");
  const write = storage.setItem;
  storage.setItem = () => { throw new DOMException("full", "QuotaExceededError"); };
  const tab = client();
  tab.load();
  const observed = tab.last().baseline_id;
  const operation = tab.replace(backup(), token(), observed);
  assert.equal(tab.last().code, "quota");
  assert.equal(tab.last().baseline_id, observed);
  assert.equal(storage.getItem(key), "{broken");
  storage.setItem = write;
  tab.replace(backup(), operation, observed);
  assert.equal(tab.last().code, "quota", "identical render retains failed acknowledgement");
  tab.replace(backup(), token(), observed);
  assert.equal(tab.last().status, "saved");
  assert.equal(storage.writes, 1);
});

test("replacement refuses a newer other-tab record even when it equals the candidate", () => {
  for (const newer of [backup(), {...backup(), flags: ["CCNA1-001"]}]) {
    const storage = setup("{broken");
    const tab = client();
    tab.load();
    const observed = tab.last().baseline_id;
    storage.setItem(key, JSON.stringify(newer));
    tab.replace(backup(), token(), observed);
    assert.equal(tab.last().code, "conflict");
    assert.equal(storage.writes, 1);
    assert.deepEqual(JSON.parse(storage.getItem(key)), newer);
    tab.replace(backup(), token(), observed);
    assert.equal(tab.last().code, "conflict", "retry must not adopt the competing record");
  }
});

test("readback disagreement never acknowledges a replacement as saved", () => {
  const storage = setup("{broken");
  const tab = client();
  tab.load();
  storage.setItem = () => {};
  tab.replace(backup());
  assert.equal(tab.last().code, "conflict");
  assert.equal(storage.getItem(key), "{broken");
  tab.save(backup());
  assert.equal(tab.last().code, "uninitialized");
});

test("a stale candidate cannot replace a later save or a fresh component baseline", () => {
  const storage = setup(JSON.stringify(backup()));
  const tab = client();
  tab.load();
  const observed = tab.last().baseline_id;
  const newer = {...backup(), flags: ["CCNA1-001"]};
  tab.save(newer);
  tab.replace(backup(), token(), observed);
  assert.equal(tab.last().code, "stale_replacement");
  const reopened = client("session-1", {});
  reopened.load();
  reopened.replace(backup(), token(), observed);
  assert.equal(reopened.last().code, "stale_replacement");
  assert.deepEqual(JSON.parse(storage.getItem(key)), newer);
});

test("deferred replacements honor Web Locks and obsolete commands never write or acknowledge", async () => {
  const storage = setup("{broken");
  let queue = Promise.resolve();
  globalThis.navigator.locks = {request(_name, callback) {
    const next = queue.then(callback); queue = next.catch(() => {}); return next;
  }};
  const first = client("first");
  const second = client("second");
  first.load(); second.load(); await queue;
  const observed = first.last().baseline_id;
  first.replace(backup());
  second.replace({...backup(), flags: ["CCNA1-001"]});
  assert.equal(storage.writes, 0, "no acknowledgement before the queued write executes");
  await queue;
  assert.equal(first.last().status, "saved");
  assert.equal(second.last().code, "conflict");
  assert.equal(storage.writes, 1);
  const cancelled = first.replace({...backup(), flags: ["CCNA1-002"]});
  first.load(); await queue;
  assert.equal(first.last().status, "loaded");
  assert.equal(first.events.some(event => event.request_id.includes(cancelled)), false);
  assert.equal(storage.writes, 1);
  first.replace({...backup(), flags: ["CCNA1-003"]}, token(), observed);
  await queue;
  assert.equal(first.last().code, "stale_replacement");
  assert.equal(storage.writes, 1);
});
