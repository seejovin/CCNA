"""Read saved progress for all ten sets without touching their write bridges.

This is a read-only snapshot of this browser's saved records, not a database of
every completed attempt. Validate each record against its bank before using it.
Call again with a different refresh token to include subsequent saves in other
tabs. Identical requests are intentionally not republished on Streamlit reruns.
"""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
from uuid import uuid4

import streamlit as st

from browser_storage import storage_key


BANK_IDS = tuple(f"ccna-200-301-v1.1-set-{number:02d}" for number in range(1, 11))
STORAGE_KEYS = {bank_id: storage_key(bank_id) for bank_id in BANK_IDS}
_SESSION_KEY = "_ccna_collection_storage_session"
_component = st.components.v2.component(
    "ccna_collection_storage",
    js=Path(__file__).with_suffix(".js").read_text(encoding="utf-8"),
)


def read_collection_progress(refresh_token: str) -> dict:
    """Return the current requested snapshot, or ``{}`` while awaiting it.

    Loaded events contain ``status``, ``request_id``, ``records`` (all ten bank
    IDs, each mapped to a progress object or ``None``), and ``errors`` (bank IDs
    with safe error messages). Missing records are ``None`` without an error.
    A bad or inaccessible record does not prevent the other sets being read.
    ``restore_progress`` must perform schema and bank validation separately.
    """
    if not isinstance(refresh_token, str):
        raise TypeError("The collection refresh token must be a string.")
    if _SESSION_KEY not in st.session_state:
        st.session_state[_SESSION_KEY] = uuid4().hex
    session_id = st.session_state[_SESSION_KEY]
    serialized = json.dumps([session_id, refresh_token], separators=(",", ":"))
    request_id = sha256(serialized.encode("utf-8")).hexdigest()
    result = _component(
        data={
            "request_id": request_id,
            "session_id": session_id,
            "storage_keys": STORAGE_KEYS,
        },
        key="ccna_collection_storage_bridge",
        default={"event": None},
        on_event_change=lambda: None,
        height=0,
    )
    event = result.get("event")
    if (
        not isinstance(event, dict)
        or event.get("request_id") != request_id
        or event.get("status") != "loaded"
        or not isinstance(event.get("records"), dict)
        or not isinstance(event.get("errors"), dict)
    ):
        return {}
    return dict(event)
