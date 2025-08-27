
import streamlit as st
from components.common import autosave
st.set_page_config(page_title="Quantification", layout="wide")
st.title("07 — Quantification")
st.number_input("Frozen cash (SAR) — total", step=1000, key="frozen_cash_total")
st.number_input("Sales opportunity (SAR/yr) — total", step=1000, key="sales_opp_total")
autosave()
