from __future__ import annotations

import json

import streamlit as st

from engine.storage import ROOT_DIR


def render() -> None:
    st.subheader("Settings")
    settings_path = ROOT_DIR / "config" / "settings.json"
    if settings_path.exists():
        st.json(json.loads(settings_path.read_text(encoding="utf-8")))
    else:
        st.warning("settings.json tidak ditemukan.")

