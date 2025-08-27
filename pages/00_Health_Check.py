
import streamlit as st, sys, platform, numpy, pandas, pptx, reportlab
st.set_page_config(page_title="Health Check", layout="wide")
st.title("Environment Health Check")
st.write({"python": sys.version, "platform": platform.platform()})
st.write({"numpy": numpy.__version__, "pandas": pandas.__version__, "pptx": pptx.__version__, "reportlab": reportlab.Version})
st.success("If you see versions above, the core environment is OK.")
