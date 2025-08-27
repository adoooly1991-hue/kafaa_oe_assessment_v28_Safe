
import streamlit as st
from components.common import autosave, workspace_bar, quick_stepper
st.set_page_config(page_title="Observations", layout="wide")
workspace_bar("06 — Observations")
quick_stepper(6)
st.title("06 — Observations")
st.text_area("Add observation (one per line)", key="observations_text")
if st.session_state.get("observations_text"):
    st.session_state["observations"] = [x.strip() for x in st.session_state["observations_text"].split("\n") if x.strip()]
    st.write("Parsed observations:")
    for o in st.session_state["observations"]:
        st.write(f"- {o}")
autosave()
