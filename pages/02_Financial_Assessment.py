
import streamlit as st
from components.common import autosave, workspace_bar, quick_stepper
st.set_page_config(page_title="Financial Assessment", layout="wide")
workspace_bar("02 — Financial Assessment")
quick_stepper(2)
st.title("02 — Financial Assessment")
st.number_input("Revenue (SAR)", step=1000, key="revenue_sar")
st.number_input("Target Profit (SAR)", step=1000, key="target_profit_sar")
st.number_input("Cost Reduction Target (SAR)", step=1000, key="cost_reduction_target_sar")
st.caption("Tip: These will feed the Executive Summary and Waterfalls later.")
autosave()
