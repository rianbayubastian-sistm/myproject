from __future__ import annotations

import streamlit as st

from engine.storage import list_projects


def render() -> None:
    projects = list_projects()

    st.subheader("Dashboard")
    col1, col2, col3 = st.columns(3)
    col1.metric("Today's Task", "MVP Foundation")
    col2.metric("Progress", "Milestone 1")
    col3.metric("Projects", len(projects))

    st.markdown("#### Production")
    st.progress(0.15, text="Milestone 1 foundation")

    st.markdown("#### Recent Project")
    if projects:
        for project in projects[-5:]:
            st.write(f"- {project.get('name', 'Untitled')} | {project.get('status', 'Draft')}")
    else:
        st.info("Belum ada project.")

    left, right = st.columns(2)
    with left:
        st.markdown("#### Knowledge Growth")
        st.write("JSON knowledge base initialized.")
        st.markdown("#### Research")
        st.write("Research module planned for Milestone 3.")
    with right:
        st.markdown("#### QC Status")
        st.write("MVP prompt QC rules available.")

