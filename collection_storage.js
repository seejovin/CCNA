// This invisible component reads only the ten progress keys supplied by Python.
// It never writes storage or changes the per-set save bridges' read baselines.
// Each refresh is a new snapshot; ten localStorage reads are not an atomic
// transaction with simultaneous writes from another browser tab.
const stateKey = Symbol.for("ccna.collection.browserStorage.readState.v1");
const unavailable = "Saved progress for this set could not be accessed. It has been left unchanged.";
const corrupt = "Saved progress for this set could not be read. It has been left unchanged.";

function readSnapshot(request) {
  const entries = Object.entries(request.storage_keys);
  const records = Object.fromEntries(entries.map(([bankId]) => [bankId, null]));
  const errors = {};
  let storage;
  try {
    storage = globalThis.localStorage;
  } catch {
    for (const [bankId] of entries) errors[bankId] = unavailable;
    return {status: "loaded", request_id: request.request_id, records, errors};
  }

  for (const [bankId, key] of entries) {
    let raw;
    try {
      raw = storage.getItem(key);
    } catch {
      errors[bankId] = unavailable;
      continue;
    }
    if (raw === null) continue;
    try {
      const payload = JSON.parse(raw);
      if (payload === null || typeof payload !== "object" || Array.isArray(payload)) {
        throw new Error("Invalid progress object");
      }
      records[bankId] = payload;
    } catch {
      errors[bankId] = corrupt;
    }
  }
  return {status: "loaded", request_id: request.request_id, records, errors};
}

export default function collectionStorage({data, parentElement, setStateValue}) {
  if (!data || !parentElement || !data.storage_keys) return;
  let state = parentElement[stateKey];
  if (!state || state.sessionId !== data.session_id) {
    state = {sessionId: data.session_id, lastRequest: null};
    parentElement[stateKey] = state;
  }
  // Publishing an event triggers a Python rerun. Emit once per request, including
  // errors; an explicit new refresh token or Python session allows a retry.
  if (state.lastRequest === data.request_id) return;
  state.lastRequest = data.request_id;
  setStateValue("event", readSnapshot(data));
}
