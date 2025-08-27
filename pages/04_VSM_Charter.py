
import streamlit as st
from components.common import autosave, workspace_bar, quick_stepper
st.set_page_config(page_title="VSM Charter", layout="wide")
workspace_bar("04 — VSM Charter")
quick_stepper(4)
st.title("04 — VSM Charter")
st.date_input("Charter date", key="charter_date")
st.text_area("Objectives", key="charter_objectives")
st.text_area("Stakeholders", key="charter_stakeholders")
autosave()
