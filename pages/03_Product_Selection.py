
import streamlit as st
from components.common import autosave
st.set_page_config(page_title="Product Selection", layout="wide")
st.title("03 — Product Selection")
st.text_input("Champion product", key="champion_product")
st.text_area("Why this product?", key="champion_why")
autosave()
