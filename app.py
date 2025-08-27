
import streamlit as st
from components.common import autosave, ensure_dirs, workspace_bar, quick_stepper
st.set_page_config(page_title="Kafaa OE Assessment", layout="wide")
ensure_dirs()
st.session_state.setdefault("active_workspace_name","workspace")
workspace_bar("Home")
quick_stepper(0)
autosave()
st.title("Kafaa OE Assessment Platform")
st.write("Follow the steps from the left sidebar (Pages). This Safe Mode build keeps things simple to ensure smooth Cloud deployment.")
st.markdown("### Steps")
st.markdown("1. 01 — Data Collection  \n2. 02 — Financial Assessment  \n3. 03 — Product Selection  \n4. 04 — VSM Charter  \n5. 05 — Value Chain Assessment  \n6. 06 — Observations  \n7. 07 — Quantification  \n8. 08 — Export (PPTX + Preview)")
