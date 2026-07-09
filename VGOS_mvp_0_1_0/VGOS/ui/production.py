from __future__ import annotations

import streamlit as st


def render() -> None:
    st.subheader("Production")
    schedule = [
        ("Senin", "Night Jazz", 10, 6),
        ("Selasa", "Bossa", 10, 0),
        ("Rabu", "Luxury Rain", 10, 0),
        ("Kamis", "Interior Cinemagraph", 10, 0),
        ("Jumat", "Cafe Ambience", 10, 0),
    ]
    for day, theme, target, done in schedule:
        st.write(f"{day} | {theme} | {target} Target")
        st.progress(done / target, text=f"{done}/{target}")

