from __future__ import annotations

import streamlit as st

from engine.qc import run_prompt_qc


def render() -> None:
    st.subheader("QC")
    compiled = st.session_state.get("compiled_prompt") or st.session_state.get("active_project", {}).get("compiled", {})
    if not compiled:
        st.warning("Belum ada compiled prompt. Compile dari Scene Editor terlebih dahulu.")
        return

    results = run_prompt_qc(compiled)
    for item in results:
        status = item["status"]
        if status == "PASS":
            st.success(f"{item['item']}: PASS")
        elif status == "WARNING":
            st.warning(f"{item['item']}: WARNING | {item['note']}")
        else:
            st.error(f"{item['item']}: FAIL | {item['note']}")

