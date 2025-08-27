
import streamlit as st, json, pathlib, datetime, glob

STEPS = [
    "Home",
    "01 — Data Collection",
    "02 — Financial Assessment",
    "03 — Product Selection",
    "04 — VSM Charter",
    "05 — Value Chain Assessment",
    "06 — Observations",
    "07 — Quantification",
    "08 — Export"
]

def ensure_dirs():
    pathlib.Path("exports").mkdir(parents=True, exist_ok=True)
    pathlib.Path("workspaces").mkdir(parents=True, exist_ok=True)

def _jsonable(v):
    try: json.dumps(v); return True
    except Exception: return False

def autosave():
    if not st.session_state.get("_autosave_on", True):
        return
    ws = {k: v for k, v in st.session_state.items() if _jsonable(v)}
    ensure_dirs()
    active = st.session_state.get("active_workspace_name", "workspace")
    p = pathlib.Path("workspaces") / f"{active}.json"
    p.write_text(json.dumps(ws, ensure_ascii=False, indent=2), encoding="utf-8")
    st.session_state["_last_autosave"] = datetime.datetime.now().strftime("%H:%M:%S")

def quick_stepper(current_index: int):
    cols = st.columns(len(STEPS))
    for i, label in enumerate(STEPS):
        with cols[i]:
            if i == current_index:
                st.markdown(f"**{label}**")
            else:
                st.caption(label)

def workspace_bar(current_page: str):
    ensure_dirs()
    with st.sidebar:
        st.subheader("🗂️ Workspace")
        st.session_state.setdefault("active_workspace_name", "workspace")
        st.text_input("Name", key="active_workspace_name")
        st.toggle("Autosave", key="_autosave_on", value=st.session_state.get("_autosave_on", True))
        files = sorted(glob.glob("workspaces/*.json"))
        file_options = ["—"] + [f.split("/",1)[-1] for f in files]
        st.selectbox("Load existing", file_options, index=0, key="_load_choice")
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("💾 Save"):
                data = {k: v for k, v in st.session_state.items() if _jsonable(v)}
                p = pathlib.Path("workspaces")/f"{st.session_state['active_workspace_name']}.json"
                p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
                st.success("Saved")
        with c2:
            if st.button("🔄 Load"):
                name = st.session_state.get("active_workspace_name","workspace")
                p = pathlib.Path("workspaces")/f"{name}.json"
                if p.exists():
                    data = json.loads(p.read_text(encoding="utf-8"))
                    for k,v in data.items():
                        st.session_state[k] = v
                    st.success("Loaded")
                else:
                    st.warning("No such workspace yet.")
        with c3:
            if st.button("🗑 Clear cache"):
                for k in list(st.session_state.keys()):
                    if not k.startswith("_"):
                        del st.session_state[k]
                st.session_state["active_workspace_name"]="workspace"
                st.success("Cleared")
        st.caption(f"Page: {current_page}")
        if st.session_state.get("_last_autosave"):
            st.caption(f"Autosaved at {st.session_state['_last_autosave']}")

def brand_palette():
    return {"primary":"#C51F2D","secondary":"#0E223F","muted":"#EEF2F6","text":"#1F2937"}

def kpi(a):
    return "—" if a in (None, "", [], {}, 0) else a
