
import streamlit as st
from components.common import autosave
st.set_page_config(page_title="Value Chain Assessment", layout="wide")
st.title("05 — Value Chain Assessment")
st.number_input("Takt time (sec)", step=1.0, key="takt_sec")
st.number_input("Bottleneck cycle time (sec)", step=1.0, key="bn_ct_sec")
st.number_input("FPY (%)", step=0.1, key="fpy_current")
autosave()
