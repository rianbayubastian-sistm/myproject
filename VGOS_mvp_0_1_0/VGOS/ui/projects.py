from __future__ import annotations

from datetime import datetime

import streamlit as st

from engine.storage import list_projects, save_project


def _new_project_id(name: str) -> str:
    return name.strip().lower().replace(" ", "_") or f"project_{datetime.now().strftime('%Y%m%d%H%M%S')}"


def render() -> None:
    st.subheader("Projects")

    with st.expander("+ New Project", expanded=True):
        name = st.text_input("Project Name", value="Beach Cafe Rain")
        description = st.text_area("Description", value="Luxury rainy beach cafe cinemagraph.")
        if st.button("Create Project", type="primary"):
            project = {
                "id": _new_project_id(name),
                "name": name,
                "description": description,
                "status": "Draft",
                "created_at": datetime.now().isoformat(timespec="seconds"),
                "scene": {},
                "analysis": {},
                "compiled": {},
            }
            save_project(project)
            st.session_state["active_project"] = project
            st.success(f"Project dibuat: {name}")

    st.markdown("#### Project List")
    projects = list_projects()
    if not projects:
        st.info("Belum ada project.")
        return

    for project in projects:
        cols = st.columns([3, 2, 1, 1])
        cols[0].write(project.get("name", "Untitled"))
        cols[1].write(project.get("status", "Draft"))
        if cols[2].button("Open", key=f"open_{project.get('id')}"):
            st.session_state["active_project"] = project
            st.session_state["page_override"] = "Scene Editor"
            st.rerun()
        if cols[3].button("Clone", key=f"clone_{project.get('id')}"):
            clone = dict(project)
            clone["id"] = f"{project.get('id')}_clone"
            clone["name"] = f"{project.get('name')} Clone"
            clone["created_at"] = datetime.now().isoformat(timespec="seconds")
            save_project(clone)
            st.success("Project cloned.")

    st.markdown("#### Archive")
    st.caption("Archive action akan dibuat pada milestone berikutnya.")

