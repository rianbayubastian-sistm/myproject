from __future__ import annotations

import streamlit as st

from engine.report import build_daily_report
from engine.storage import list_projects


def render() -> None:
    st.subheader("Reports")
    report_type = st.radio("Type", ["Daily", "Weekly", "Monthly"], horizontal=True)
    report = build_daily_report(list_projects())
    report["type"] = report_type
    st.json(report)

