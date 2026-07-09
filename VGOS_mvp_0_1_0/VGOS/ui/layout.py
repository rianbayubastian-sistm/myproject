from __future__ import annotations

import streamlit as st


MENU_ITEMS = [
    "Dashboard",
    "Projects",
    "Analyze",
    "Scene Editor",
    "Knowledge",
    "QC",
    "Production",
    "Research",
    "Reports",
    "Settings",
]


def configure_page() -> None:
    st.set_page_config(page_title="VGOS", page_icon="VGOS", layout="wide")


def render_header() -> None:
    st.title("VGOS v1.0")
    st.caption("Visual Generation Operating System | MVP 0.1.0 | Freeze foundation")


def render_sidebar() -> str:
    st.sidebar.header("Menu Utama")
    return st.sidebar.radio("Navigation", MENU_ITEMS, label_visibility="collapsed")


def render_console(messages: list[str]) -> None:
    st.divider()
    st.subheader("Bottom Console")
    if not messages:
        st.info("Console siap.")
        return
    for message in messages[-8:]:
        st.code(message)

