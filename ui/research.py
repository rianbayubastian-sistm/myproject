from __future__ import annotations

import streamlit as st


def render() -> None:
    st.subheader("Research")
    st.info("Milestone 3 module placeholder.")
    st.columns(4)
    for source in ["Youtube", "Pinterest", "Instagram", "Competitor"]:
        st.write(f"- {source}")
    st.markdown("Output planned: Trend, Theme, DNA, Reference, Idea.")

