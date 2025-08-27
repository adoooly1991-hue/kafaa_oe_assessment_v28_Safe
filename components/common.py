
import streamlit as st, json, pathlib, datetime
def ensure_dirs():
    pathlib.Path("exports").mkdir(parents=True, exist_ok=True)
    pathlib.Path("workspaces").mkdir(parents=True, exist_ok=True)
def autosave():
    def jsonable(v):
        try: json.dumps(v); return True
        except Exception: return False
    ws = {k:v for k,v in st.session_state.items() if jsonable(v)}
    ensure_dirs()
    active = st.session_state.get("active_workspace_name", "_autosave")
    p = pathlib.Path("workspaces")/f"{active}.json"
    p.write_text(json.dumps(ws, ensure_ascii=False, indent=2), encoding="utf-8")
    st.session_state["_last_autosave"] = datetime.datetime.now().strftime("%H:%M:%S")
def brand_palette():
    return {"primary":"#C51F2D","secondary":"#0E223F","muted":"#EEF2F6","text":"#1F2937"}
def kpi(a):
    return "—" if a in (None, "", [], {}, 0) else a
