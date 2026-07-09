from __future__ import annotations

import streamlit as st

from engine.compiler import compile_prompt
from engine.storage import save_project
from engine.validator import validate_scene


DEFAULT_SCENE = {
    "scene": "Ultra-luxury contemporary penthouse living residence overlooking the illuminated historic skyline of Rome.",
    "camera": "Premium large-format digital cinema camera, master-grade apochromatic prime lens, natural 38 mm, f/4.5, eye-level architectural perspective.",
    "lighting": "Warm interior tungsten illumination balanced with cool nocturnal urban lighting, physically accurate global illumination.",
    "weather": "Night, clear city atmosphere.",
    "material": "Matte European oak flooring, polished walnut furniture, premium woven upholstery, crystal glassware, transparent architectural glass.",
    "motion": "Hero motion only: natural fireplace flames; restrained candle flame oscillation; faint airborne dust drift.",
    "boundary": "Absolute positional stability for architecture, furniture, skyline, kitchen, staircase, sofa, and table.",
    "decoration": "Fresh tulips, fine wine, curated books, handmade candles, satin ceramic decor.",
    "overlay": "No text overlay.",
}


def render() -> None:
    st.subheader("Scene Editor")
    project = st.session_state.get("active_project", {})
    scene = dict(DEFAULT_SCENE)
    scene.update(project.get("scene", {}))

    preview, inspector = st.columns([2, 1])

    with preview:
        st.markdown("#### Preview")
        st.info("MVP preview: scene data akan dikompilasi menjadi prompt. Visual generator/API masuk setelah fondasi stabil.")
        scene["scene"] = st.text_area("Scene", scene["scene"], height=90)
        scene["camera"] = st.text_area("Camera", scene["camera"], height=80)
        scene["lighting"] = st.text_area("Lighting", scene["lighting"], height=80)
        scene["weather"] = st.text_input("Weather", scene["weather"])
        scene["material"] = st.text_area("Material", scene["material"], height=80)
        scene["motion"] = st.text_area("Motion", scene["motion"], height=80)
        scene["boundary"] = st.text_area("Boundary", scene["boundary"], height=80)
        scene["decoration"] = st.text_area("Decoration", scene["decoration"], height=80)
        scene["overlay"] = st.text_input("Overlay", scene["overlay"])

    with inspector:
        st.markdown("#### Inspector")
        validation = validate_scene(scene)
        st.json(validation)
        if st.button("Compile", type="primary"):
            compiled = compile_prompt(scene)
            project["scene"] = scene
            project["compiled"] = compiled
            if project.get("id"):
                save_project(project)
            st.session_state["active_project"] = project
            st.session_state["compiled_prompt"] = compiled
            st.success("Prompt compiled.")

    compiled_prompt = st.session_state.get("compiled_prompt") or project.get("compiled")
    if compiled_prompt:
        st.markdown("#### Compiled Output")
        st.text_area("Prompt", compiled_prompt.get("prompt", ""), height=180)
        st.text_area("Negative Prompt", compiled_prompt.get("negative_prompt", ""), height=120)
        st.json({"format": compiled_prompt.get("format"), "duration_seconds": compiled_prompt.get("duration_seconds"), "version": compiled_prompt.get("version")})

