from __future__ import annotations

import json

import streamlit as st

from engine.storage import KNOWLEDGE_DIR, load_knowledge, write_json


MODULES = [
    "world",
    "camera",
    "lighting",
    "weather",
    "material",
    "architecture",
    "motion",
    "decoration",
    "boundary",
    "grammar",
    "vocabulary",
]


def render() -> None:
    st.subheader("Knowledge")
    module = st.selectbox("Library", MODULES)
    data = load_knowledge(module)

    st.markdown("#### Current Data")
    edited = st.text_area("JSON", json.dumps(data, indent=2, ensure_ascii=False), height=360)

    cols = st.columns(4)
    if cols[0].button("Tambah"):
        data.append({"id": "new_item", "label": "New Item", "keywords": [], "prompt_terms": []})
        write_json(KNOWLEDGE_DIR / f"{module}.json", data)
        st.rerun()
    if cols[1].button("Edit / Save", type="primary"):
        try:
            parsed = json.loads(edited)
            write_json(KNOWLEDGE_DIR / f"{module}.json", parsed)
            st.success("Knowledge saved.")
        except json.JSONDecodeError as exc:
            st.error(f"JSON error: {exc}")
    if cols[2].button("Delete Last"):
        if data:
            data.pop()
            write_json(KNOWLEDGE_DIR / f"{module}.json", data)
            st.rerun()
    if cols[3].button("Version"):
        st.info("Versioning formal akan masuk Milestone 2. File JSON saat ini menjadi source of truth.")

