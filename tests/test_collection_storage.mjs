import assert from "node:assert/strict";
import {createHash} from "node:crypto";
import {readFile} from "node:fs/promises";
import test from "node:test";

const source = await readFile(new URL("../collection_storage.js", import.meta.url), "utf8");
const {default: render} = await import(`data:text/javascript;base64,${Buffer.from(source).toString("base64")}`);
const ids = Array.from({length: 10}, (_, index) => `ccna-200-301-v1.1-set-${String(index + 1).padStart(2, "0")}`);
const keys = Object.fromEntries(ids.map((id, index) => [id, `ccna:200-301:v1.1:set-${String(index + 1).padStart(2, "0")}:progress:v1`]));

function setup(initial = {}) {
  const items = new Map(Object.entries(initial));
  const storage = {
    reads: [],
    writes: 0,
    getItem(name) { this.reads.push(name); return items.get(name) ?? null; },
    setItem() { this.writes++; throw new Error("Read-only bridge attempted a write"); },
    removeItem() { this.writes++; throw new Error("Read-only bridge attempted a deletion"); },
    clear() { this.writes++; throw new Error("Read-only bridge attempted a clear"); },
  };
  Object.defineProperty(globalThis, "localStorage", {configurable: true, value: storage});
  return {storage, items};
}

function client(session = "python-session-1", host = {}) {
  const events = [];
  return {
    events,
    host,
    read(refreshToken = "entered-overall-results") {
      const request_id = createHash("sha256").update(JSON.stringify([session, refreshToken])).digest("hex");
      render({
        parentElement: host,
        data: {session_id: session, request_id, storage_keys: keys},
        setStateValue(name, event) { assert.equal(name, "event"); events.push(event); },
      });
      return request_id;
    },
    last() { return events.at(-1); },
  };
}

test("reads exactly ten known keys, retaining objects and representing missing sets as null", () => {
  const first = {bank_id: ids[0], latest_attempt: {answers: {"CCNA1-001": ["A"]}}, wrong_answers: {"CCNA1-002": {response: ["B"]}}};
  const tenth = {bank_id: ids[9], latest_attempt: {answers: {}}, wrong_answers: {}};
  const {storage} = setup({[keys[ids[0]]]: JSON.stringify(first), [keys[ids[9]]]: JSON.stringify(tenth), "unrelated-secret": "do-not-read"});
  const tab = client();
  const request_id = tab.read();
  assert.equal(tab.last().status, "loaded");
  assert.equal(tab.last().request_id, request_id);
  assert.deepEqual(Object.keys(tab.last().records), ids);
  assert.deepEqual(tab.last().records[ids[0]], first);
  assert.deepEqual(tab.last().records[ids[9]], tenth);
  for (const id of ids.slice(1, 9)) assert.equal(tab.last().records[id], null);
  assert.deepEqual(tab.last().errors, {});
  assert.deepEqual(storage.reads, Object.values(keys));
  assert.equal(storage.writes, 0);
});

test("new refresh token includes newer saved progress without writing any record", () => {
  const {storage, items} = setup({[keys[ids[1]]]: '{"correct":1}'});
  const tab = client();
  tab.read("first-visit");
  const first = tab.last();
  items.set(keys[ids[1]], '{"correct":2}');
  tab.read("manual-refresh");
  assert.deepEqual(first.records[ids[1]], {correct: 1});
  assert.deepEqual(tab.last().records[ids[1]], {correct: 2});
  assert.notEqual(first.request_id, tab.last().request_id);
  assert.equal(storage.reads.length, 20);
  assert.equal(storage.writes, 0);
});

test("corrupt or non-object JSON affects only that set and remains unchanged", () => {
  for (const raw of ["{broken", "[]", "null", '"text"', "42", "true"]) {
    const {storage, items} = setup({[keys[ids[0]]]: raw, [keys[ids[8]]]: '{"good":true}'});
    const tab = client();
    tab.read();
    assert.equal(tab.last().records[ids[0]], null);
    assert.match(tab.last().errors[ids[0]], /could not be read/);
    assert.deepEqual(Object.keys(tab.last().errors), [ids[0]]);
    assert.deepEqual(tab.last().records[ids[8]], {good: true});
    assert.equal(items.get(keys[ids[0]]), raw);
    assert.equal(storage.reads.length, 10);
    assert.equal(storage.writes, 0);
  }
});

test("one inaccessible key does not prevent reading the remaining sets", () => {
  const {storage} = setup({[keys[ids[9]]]: '{"good":true}'});
  const getItem = storage.getItem.bind(storage);
  storage.getItem = name => {
    if (name === keys[ids[2]]) throw new DOMException("private storage detail", "SecurityError");
    return getItem(name);
  };
  const tab = client();
  tab.read();
  assert.deepEqual(Object.keys(tab.last().errors), [ids[2]]);
  assert.equal(tab.last().records[ids[2]], null);
  assert.deepEqual(tab.last().records[ids[9]], {good: true});
  assert.doesNotMatch(tab.last().errors[ids[2]], /private storage detail/);
  assert.equal(storage.writes, 0);
});

test("globally blocked storage reports all ten errors without rerun loops", () => {
  const {storage} = setup();
  Object.defineProperty(globalThis, "localStorage", {configurable: true, get() {
    throw new DOMException("private browser detail", "SecurityError");
  }});
  const tab = client();
  tab.read(); tab.read(); tab.read();
  assert.equal(tab.events.length, 1);
  assert.deepEqual(Object.keys(tab.last().errors), ids);
  assert.deepEqual(Object.values(tab.last().records), Array(10).fill(null));
  for (const message of Object.values(tab.last().errors)) assert.doesNotMatch(message, /private browser detail/);
  assert.equal(storage.writes, 0);
});

test("identical requests read and publish once, including after a manual refresh", () => {
  const {storage} = setup();
  const tab = client();
  tab.read(); tab.read(); tab.read();
  assert.equal(tab.events.length, 1);
  assert.equal(storage.reads.length, 10);
  tab.read("refresh-2"); tab.read("refresh-2");
  assert.equal(tab.events.length, 2);
  assert.equal(storage.reads.length, 20);
  assert.equal(storage.writes, 0);
});

test("a new Python session rereads on the same host with the same refresh token", () => {
  const {storage, items} = setup({[keys[ids[0]]]: '{"version":1}'});
  const first = client("session-before-reconnect");
  first.read("same-refresh-token");
  items.set(keys[ids[0]], '{"version":2}');
  const second = client("session-after-reconnect", first.host);
  second.read("same-refresh-token");
  assert.notEqual(second.last().request_id, first.last().request_id);
  assert.deepEqual(second.last().records[ids[0]], {version: 2});
  assert.equal(storage.reads.length, 20);
  assert.equal(storage.writes, 0);
});

test("collection reads leave the active write bridge state and baseline untouched", () => {
  const {storage} = setup({[keys[ids[0]]]: '{"saved":true}'});
  const host = {};
  const writeStateKey = Symbol.for("ccna.set01.browserStorage.state.v1");
  const writeState = {sessionId: "write-session", storageKey: keys[ids[0]], ready: true, baseline: '{"earlier":true}', lastRequest: "save:earlier-hash"};
  host[writeStateKey] = writeState;
  const before = structuredClone(writeState);
  const tab = client("collection-session", host);
  tab.read(); tab.read("refresh-2");
  assert.equal(host[writeStateKey], writeState);
  assert.deepEqual(host[writeStateKey], before);
  assert.equal(storage.writes, 0);
});
