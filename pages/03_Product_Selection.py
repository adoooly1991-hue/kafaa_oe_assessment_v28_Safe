
import streamlit as st
from components.common import autosave, workspace_bar, quick_stepper
st.set_page_config(page_title="Product Selection", layout="wide")
workspace_bar("03 — Product Selection")
quick_stepper(3)
st.title("03 — Product Selection")
st.text_input("Champion product", key="champion_product")
st.text_area("Why this product?", key="champion_why")
autosave()
