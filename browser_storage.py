"""A small, read-before-write bridge to this browser's persistent storage.

Call ``sync_storage(None)`` until a loaded event arrives. Validate that payload
before calling ``sync_storage(payload)`` on every run. A save is durable only
when the returned saved event has the current ``storage_request_id(payload)``.
The same component must remain mounted, including while loading or displaying
errors. An explicitly confirmed backup replacement uses a fresh replacement ID
and the baseline ID from the last read/save event; ordinary saves cannot repair
malformed data. Keep a replacement pending until its exact saved acknowledgment.
"""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import re
from uuid import uuid4

import streamlit as st

from progress_store import restore_progress
from quiz_core import load_bank


STORAGE_KEY = "ccna:200-301:v1.1:set-01:progress:v1"
DEFAULT_BANK_ID = "ccna-200-301-v1.1-set-01"
_SESSION_KEY = "_ccna_browser_storage_session"
_component = st.components.v2.component(
    "ccna_browser_storage",
    js=Path(__file__).with_suffix(".js").read_text(encoding="utf-8"),
)


def _serialize(payload: dict) -> str:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=False, allow_nan=False)


def storage_request_id(payload: dict | None, *, replacement_id: str | None = None) -> str:
    """Identify a content-specific save or one explicitly confirmed replacement."""
    if replacement_id is not None and (
        payload is None or not isinstance(replacement_id, str)
        or not re.fullmatch(r"[a-f0-9]{32}", replacement_id)
    ):
        raise ValueError("A replacement requires progress and a fresh UUID hex token.")
    if payload is None:
        return "load"
    digest = sha256(_serialize(payload).encode("utf-8")).hexdigest()
    return digest if replacement_id is None else f"replace:{replacement_id}:{digest}"


def storage_key(bank_id: str) -> str:
    """Keep the original Set 01 key and isolate every additional set."""
    match = re.fullmatch(r"ccna-200-301-v1\.1-set-(0[1-9]|10)", bank_id)
    if not match:
        raise ValueError("Unsupported question set for saved progress.")
    return f"ccna:200-301:v1.1:set-{match[1]}:progress:v1"


def sync_storage(payload: dict | None, *, bank_id: str = DEFAULT_BANK_ID,
                 replacement_id: str | None = None,
                 expected_baseline: str | None = None) -> dict:
    """Read or save asynchronously; an empty dict means no event has arrived.

    Events have ``status`` (loaded/saved/error), ``request_id`` and, for reads,
    ``payload``. Errors also include a safe user-facing ``error`` and ``code``.
    Reads (including corrupt-data errors) and acknowledged saves carry a
    ``baseline_id``. For a confirmed replacement supply that ID as
    ``expected_baseline`` plus a new ``uuid4().hex`` as ``replacement_id``.
    Retain both unchanged while waiting; retry requires a new replacement ID.
    Only a matching saved request ID permits the caller to adopt the candidate.
    The raw baseline is kept inside the browser. Writes from stale tabs are
    rejected, with Web Locks serializing writes where supported.
    """
    key = storage_key(bank_id)
    if payload is not None and (not isinstance(payload, dict) or payload.get("bank_id") != bank_id):
        raise ValueError("Progress and destination set must match.")
    request_id = storage_request_id(payload, replacement_id=replacement_id)
    if replacement_id is not None:
        if not isinstance(expected_baseline, str) or not expected_baseline:
            raise ValueError("A replacement requires the previously read browser baseline.")
        # Validate at the bridge boundary as well as in the import UI. Validation
        # never mutates the candidate or fabricates missing mistake timestamps.
        restore_progress(payload, load_bank(int(bank_id.rsplit("-", 1)[1])))
    elif expected_baseline is not None:
        raise ValueError("A browser baseline is only used for confirmed replacement.")
    if _SESSION_KEY not in st.session_state:
        st.session_state[_SESSION_KEY] = uuid4().hex
    request = {
        "operation": "replace" if replacement_id is not None else "load" if payload is None else "save",
        "request_id": request_id,
        "session_id": st.session_state[_SESSION_KEY],
        "storage_key": key,
    }
    if payload is not None:
        request["serialized"] = _serialize(payload)
    if replacement_id is not None:
        request.update(replacement_id=replacement_id, expected_baseline=expected_baseline)
    result = _component(
        data=request,
        key="ccna_browser_storage_bridge" if bank_id == DEFAULT_BANK_ID else f"ccna_browser_storage_bridge_{bank_id}",
        default={"event": None},
        on_event_change=lambda: None,
        height=0,
    )
    event = result.get("event")
    return dict(event) if isinstance(event, dict) else {}
