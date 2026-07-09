from __future__ import annotations

import streamlit as st

from ui import analyze, dashboard, knowledge, production, projects, qc, reports, research, scene_editor, settings
from ui.layout import configure_page, render_console, render_header, render_sidebar


PAGES = {
    "Dashboard": dashboard.render,
    "Projects": projects.render,
    "Analyze": analyze.render,
    "Scene Editor": scene_editor.render,
    "Knowledge": knowledge.render,
    "QC": qc.render,
    "Production": production.render,
    "Research": research.render,
    "Reports": reports.render,
    "Settings": settings.render,
}


def main() -> None:
    configure_page()
    render_header()

    selected = st.session_state.pop("page_override", None) or render_sidebar()
    st.sidebar.caption("VGOS 0.1.0 | Frozen menu")

    console = st.session_state.setdefault("console", [])
    console.append(f"Open page: {selected}")

    page = PAGES[selected]
    page()
    render_console(console)


if __name__ == "__main__":
    main()
