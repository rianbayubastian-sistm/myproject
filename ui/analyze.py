from __future__ import annotations

import streamlit as st

from engine.analyzer import analyze_image_metadata, analyze_text


def render() -> None:
    st.subheader("Analyze")

    input_mode = st.radio("Input", ["Upload Image", "Paste Prompt", "Paste URL", "Start Empty"], horizontal=True)
    result = None

    if input_mode == "Upload Image":
        uploaded = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg", "webp"])
        if uploaded:
            st.image(uploaded, caption=uploaded.name, use_container_width=True)
            if st.button("Start Analyze", type="primary"):
                data = uploaded.getvalue()
                result = analyze_image_metadata(uploaded.name, uploaded.type, len(data))

    elif input_mode == "Paste Prompt":
        text = st.text_area("Paste Prompt", height=180, value="Ultra luxury penthouse in Rome at night with fireplace, glass, warm tungsten lighting, cinematic cinemagraph.")
        if st.button("Start Analyze", type="primary"):
            result = analyze_text(text)

    elif input_mode == "Paste URL":
        url = st.text_input("Paste URL")
        if st.button("Start Analyze", type="primary"):
            result = analyze_text(url)

    else:
        if st.button("Start Empty", type="primary"):
            result = analyze_text("")

    if result:
        st.session_state["last_analysis"] = result
        project = st.session_state.get("active_project")
        if project:
            project["analysis"] = result
            st.session_state["active_project"] = project

    stored = st.session_state.get("last_analysis")
    if stored:
        st.markdown("#### Knowledge Result")
        left, right = st.columns([1, 1])
        with left:
            st.markdown("Background Detection")
            st.json(stored.get("background_profile", {}))
            st.markdown("DNA Summary")
            st.json(stored.get("dna_summary", {}))
        with right:
            st.markdown("Theme Mapping")
            st.json(stored.get("theme_mapping", {}))
            st.markdown("Risk Detection")
            st.json(stored.get("risk_detection", []))

        with st.expander("DNA Detection Detail"):
            st.json(stored.get("dna_detection", {}))

