
import streamlit as st
from components.common import autosave
st.set_page_config(page_title="Data Collection", layout="wide")
st.title("01 — Data Collection")
st.text_input("Client name (English)", key="client_name")
st.file_uploader("Upload client logo (optional PNG/JPG)", type=["png","jpg","jpeg"], key="client_logo_file")
if st.session_state.get("client_logo_file"):
    st.session_state["client_logo_path"] = "assets/client_logo_uploaded.png"
    with open(st.session_state["client_logo_path"], "wb") as f:
        f.write(st.session_state["client_logo_file"].getvalue())
    st.image(st.session_state["client_logo_path"], width=160)
st.text_area("Scope notes", key="scope_notes")
autosave()
