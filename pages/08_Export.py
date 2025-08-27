
import streamlit as st, json
from pathlib import Path
from components.common import autosave, ensure_dirs
from report.report_engine import build_pptx, build_preview
st.set_page_config(page_title="Export", layout="wide")
st.title("08 — Export")
ensure_dirs()
payload = {
    "client": {"name_en": st.session_state.get("client_name","Client"), "logo": st.session_state.get("client_logo_path")},
    "financials": {"cost_reduction_target_sar": st.session_state.get("cost_reduction_target_sar", 0)},
    "muda": {"quantification": {"cash": [{"label":"Total","value": st.session_state.get("frozen_cash_total",0)}],
                                "lost_opportunity": [{"label":"Total","value": st.session_state.get("sales_opp_total",0)}]}},
    "observations": st.session_state.get("observations", [])
}
Path("report").mkdir(parents=True, exist_ok=True)
payload_path = "report/live_payload.json"
Path(payload_path).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
st.code(json.dumps(payload, ensure_ascii=False, indent=2)[:800])
col1, col2 = st.columns(2)
with col1:
    if st.button("Generate PPTX"):
        out = f"exports/Assessment_Report_{payload['client']['name_en'].replace(' ','_')}.pptx"
        build_pptx(payload_path, out, "kafaa")
        st.success(f"Created {out}")
        st.download_button("Download PPTX", data=open(out,'rb').read(), file_name=Path(out).name)
with col2:
    if st.button("Preview cover image"):
        outp = f"exports/Preview_{payload['client']['name_en'].replace(' ','_')}.png"
        build_preview(payload_path, outp, "kafaa")
        st.image(outp, caption="Preview", width=600)
autosave()
