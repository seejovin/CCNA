// This trusted, invisible Streamlit component only accesses the app's own key.
// The host survives ordinary renders; a Python-session token forces a fresh
// read after server reconnects even when the browser keeps its component DOM.
const stateKey = Symbol.for("ccna.set01.browserStorage.state.v1");

function failure(request, code, error) {
  return {status: "error", request_id: request.request_id, code, error};
}

function baseline(state, raw) {
  state.baseline = raw;
  state.observed = true;
  // This is an opaque observation identity, not a password or capability. A
  // fresh identity also prevents a command from surviving a component remount.
  state.baselineId = globalThis.crypto?.randomUUID?.() ??
    `${Date.now()}:${Math.random()}:${Math.random()}`;
}

function perform(request, state) {
  const fail = (code, error) => ({...failure(request, code, error),
    ...(state.observed ? {baseline_id: state.baselineId} : {})});
  try {
    if (request.operation === "load") {
      const storage = globalThis.localStorage;
      const raw = storage.getItem(request.storage_key);
      // Keep even an unreadable raw value as the compare-and-write baseline.
      // It may only be replaced through an explicit confirmed operation.
      baseline(state, raw);
      let payload = null;
      if (raw !== null) {
        try {
          payload = JSON.parse(raw);
          if (payload === null || typeof payload !== "object" || Array.isArray(payload)) {
            throw new Error("Invalid progress object");
          }
        } catch {
          state.ready = false;
          return fail("corrupt", "Saved browser data could not be read. It has been left unchanged.");
        }
      }
      state.ready = true;
      return {status: "loaded", request_id: request.request_id, payload, baseline_id: state.baselineId};
    }

    const replacing = request.operation === "replace";
    if (replacing) {
      const token = request.replacement_id;
      if (typeof token !== "string" || !/^[a-f0-9]{32}$/.test(token) ||
          typeof request.expected_baseline !== "string" || !request.expected_baseline) {
        return fail("invalid_request", "Confirm the backup replacement again before saving.");
      }
      if (state.replacements.has(token)) {
        return fail("replayed", "This replacement was already attempted. Confirm a new attempt before retrying.");
      }
      // Consume attempts, including failed attempts. An ordinary render of the
      // same command keeps its last event; a new attempt needs a new token.
      state.replacements.add(token);
      if (!state.observed) {
        return fail("uninitialized", "Reload the page before replacing saved progress so existing browser history can be read safely.");
      }
      if (request.expected_baseline !== state.baselineId) {
        return fail("stale_replacement", "Saved progress has changed since this replacement was prepared. Reload and review it before importing again.");
      }
      let candidate;
      try { candidate = JSON.parse(request.serialized); } catch {}
      const match = /^ccna:200-301:v1\.1:set-(0[1-9]|10):progress:v1$/.exec(request.storage_key);
      if (!candidate || Array.isArray(candidate) || typeof candidate !== "object" ||
          !match || candidate.bank_id !== `ccna-200-301-v1.1-set-${match[1]}`) {
        return fail("invalid_replacement", "The replacement must be valid progress for this question set.");
      }
    } else if (request.operation !== "save") {
      return fail("invalid_request", "The browser storage request was not recognized.");
    } else if (!state.ready) {
      return fail("uninitialized", "Reload the page before saving so existing browser history can be read safely.");
    }
    // Compare inside a Web Lock when available. Never silently replace work
    // saved by another tab since this tab's last successful read or write.
    const storage = globalThis.localStorage;
    const current = storage.getItem(request.storage_key);
    if (current !== state.baseline && (replacing || current !== request.serialized)) {
      return fail("conflict", "Another tab changed your saved progress. Download a backup of this tab's work, then reload.");
    }
    if (current !== request.serialized) {
      storage.setItem(request.storage_key, request.serialized);
    }
    // A successful read is insufficient: acknowledge only a completed write
    // (or an identical value already stored), verified immediately afterward.
    if (storage.getItem(request.storage_key) !== request.serialized) {
      return fail("conflict", "Saved progress changed in another tab. Download a backup of this tab's work, then reload.");
    }
    baseline(state, request.serialized);
    state.ready = true;
    return {status: "saved", request_id: request.request_id, baseline_id: state.baselineId};
  } catch (error) {
    if (error?.name === "QuotaExceededError" || error?.name === "NS_ERROR_DOM_QUOTA_REACHED") {
      return fail("quota", "Browser storage is full. Download a progress backup to keep your work.");
    }
    return fail("unavailable", "Browser storage is unavailable. Download a progress backup to keep your work.");
  }
}

export default function browserStorage({data, parentElement, setStateValue}) {
  if (!data || !parentElement) return;
  let state = parentElement[stateKey];
  // An already-open Set 01 app may update without a page reload. Its prior
  // bridge had this same host/session and supported only the original key.
  // Preserve that established read baseline; never adopt it for another set.
  if (state && state.sessionId === data.session_id && state.storageKey === undefined &&
      data.storage_key === "ccna:200-301:v1.1:set-01:progress:v1") {
    state.storageKey = data.storage_key;
  }
  if (!state || state.sessionId !== data.session_id || state.storageKey !== data.storage_key) {
    state = {sessionId: data.session_id, storageKey: data.storage_key, ready: false,
      observed: false, baseline: null, baselineId: null, replacements: new Set(), lastRequest: null};
    parentElement[stateKey] = state;
  }
  // Preserve an older bridge's already-established baseline during deployment.
  // Corrupt data from the old bridge had no baseline and still requires a read.
  if (!state.replacements) state.replacements = new Set();
  if (state.ready && !state.observed) baseline(state, state.baseline);
  const command = `${data.operation}:${data.request_id}`;
  // setStateValue causes a rerun. Do not publish that same event again when
  // Python renders an unchanged command, including repeated error commands.
  if (state.lastRequest === command) return;
  state.lastRequest = command;

  const isCurrent = () => parentElement[stateKey] === state && state.lastRequest === command;
  const run = () => {
    if (!isCurrent()) return;
    const event = perform(data, state);
    if (isCurrent()) setStateValue("event", event);
  };
  // Web Locks serialize the read/compare/write transaction across tabs. Older
  // browsers still receive stale-value detection; use a single active tab in
  // those browsers because localStorage alone has no atomic compare-and-set.
  if (globalThis.navigator?.locks?.request) {
    globalThis.navigator.locks.request(`${data.storage_key}:write`, run).catch(() => {
      if (isCurrent()) {
        setStateValue("event", failure(data, "unavailable", "Browser storage could not be accessed. Download a progress backup to keep your work."));
      }
    });
  } else {
    run();
  }
}
