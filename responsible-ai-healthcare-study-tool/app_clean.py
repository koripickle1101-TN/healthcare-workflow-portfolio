import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Healthcare Operations AI Evaluator", layout="wide")

ORANGE = "#FF8200"
WARM = "#E8E3DC"
SOFT = "#F7F4EF"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&family=Playfair+Display:wght@700;900&family=Allura&display=swap');
html, body, [class*='css'] {{ font-family: Inter, sans-serif; color: #000000; }}
.stApp {{ background: linear-gradient(180deg,#FFFFFF 0%,#FFFFFF 78%,#FBF8F3 100%); }}
section[data-testid='stSidebar'] {{ background:#FFFFFF; border-right:1px solid {WARM}; }}
.block-container {{ max-width:1220px; padding-top:1.2rem; }}
.brand {{ border:1px solid {WARM}; border-radius:34px; padding:30px; background:#FFFFFF; box-shadow:0 24px 64px rgba(0,0,0,.055); margin-bottom:28px; }}
.sig {{ font-family:Allura,cursive; font-size:82px; text-align:center; line-height:.9; color:#111111; }}
.kicker {{ text-align:center; letter-spacing:8px; text-transform:uppercase; font-weight:800; font-size:21px; margin-top:14px; }}
.intel {{ text-align:center; letter-spacing:12px; text-transform:uppercase; font-weight:900; font-size:32px; color:{ORANGE}; }}
.line {{ height:2px; width:78%; margin:18px auto; background:linear-gradient(90deg,transparent,{ORANGE},transparent); }}
.hero {{ border:1px solid {WARM}; border-radius:36px; padding:48px; background:linear-gradient(135deg,#FFFFFF 0%,#FFFFFF 68%,rgba(255,130,0,.08) 100%); box-shadow:0 28px 78px rgba(0,0,0,.07); }}
.eyebrow {{ font-size:12px; letter-spacing:3px; text-transform:uppercase; font-weight:900; display:inline-block; padding-bottom:8px; border-bottom:2px solid {ORANGE}; margin-bottom:24px; }}
.title {{ font-family:Playfair Display,serif; font-size:clamp(42px,6vw,78px); line-height:.96; letter-spacing:-2px; margin:0 0 22px 0; }}
.orange {{ color:{ORANGE}; }}
.copy {{ max-width:900px; font-size:18px; line-height:1.7; color:#242424; }}
.card {{ border:1px solid {WARM}; border-top:5px solid {ORANGE}; border-radius:26px; padding:24px; background:#FFFFFF; box-shadow:0 18px 48px rgba(0,0,0,.05); height:100%; }}
.cardtitle {{ font-family:Playfair Display,serif; font-size:28px; line-height:1.1; margin-bottom:10px; }}
.section {{ font-family:Playfair Display,serif; font-size:42px; line-height:1; margin:38px 0 16px; }}
.metricbox {{ border:1px solid {WARM}; border-left:5px solid {ORANGE}; border-radius:22px; background:{SOFT}; padding:24px; min-height:130px; }}
.big {{ font-family:Playfair Display,serif; font-size:42px; font-weight:900; }}
.label {{ font-size:12px; font-weight:900; letter-spacing:1.4px; text-transform:uppercase; color:#555555; }}
.pill {{ display:inline-block; border:1px solid {ORANGE}; background:rgba(255,130,0,.08); border-radius:999px; padding:8px 13px; margin:4px 5px 4px 0; font-size:12px; font-weight:900; text-transform:uppercase; }}
.callout {{ border:1px solid {WARM}; border-left:6px solid {ORANGE}; border-radius:24px; padding:24px; background:#FFFFFF; margin:18px 0; }}
.footsig {{ font-family:Allura,cursive; font-size:48px; }}
.footer {{ text-align:center; border-top:1px solid {WARM}; margin-top:56px; padding:34px 0 18px; }}
div.stButton > button, div.stDownloadButton > button {{ border-radius:999px; border:1px solid {ORANGE}; background:{ORANGE}; color:white; font-weight:900; }}
</style>
""", unsafe_allow_html=True)

if "alerts" not in st.session_state:
    st.session_state.alerts = []
if "pipeline" not in st.session_state:
    st.session_state.pipeline = []


def data_engine(n):
    rng = np.random.default_rng(42)
    df = pd.DataFrame({
        "record_id": [f"CASE {i:04d}" for i in range(1, n + 1)],
        "payer_group": rng.choice(["Commercial", "Medicaid", "Medicare", "Self Pay"], n),
        "workflow_area": rng.choice(["Patient Access", "Prior Authorization", "Health Information", "Revenue Cycle"], n),
        "documentation_score": rng.integers(60, 100, n),
        "authorization_age_days": rng.integers(0, 12, n),
        "queue_age_days": rng.integers(0, 16, n),
    })
    df["risk_score"] = (100 - df["documentation_score"] + df["authorization_age_days"] * 5 + df["queue_age_days"] * 2).clip(0, 100)
    df["risk_level"] = pd.cut(df["risk_score"], [-1, 35, 65, 100], labels=["Low", "Moderate", "High"])
    df["delay_flag"] = np.where(df["risk_score"] >= 60, 1, 0)
    return df


def make_safe(df):
    out = df.copy()
    out["record_id"] = [f"SAFE {i:05d}" for i in range(1, len(out) + 1)]
    return out


def fairness(df):
    table = df.groupby("payer_group", observed=True).agg(records=("record_id", "count"), delay_rate=("delay_flag", "mean"), average_risk=("risk_score", "mean")).reset_index()
    table["delay_rate"] = table["delay_rate"].round(3)
    table["average_risk"] = table["average_risk"].round(1)
    high = table["delay_rate"].max()
    low = table["delay_rate"].min()
    ratio = 1.0 if high == 0 else round(low / high, 2)
    return table, ratio


def brand():
    st.markdown("<div class='brand'><div class='sig'>Kori Pickle</div><div class='line'></div><div class='kicker'>Healthcare Operations</div><div class='intel'>Intelligence</div></div>", unsafe_allow_html=True)


def footer():
    st.markdown("<div class='footer'><div style='font-weight:900;'>Created by Kori Pickle</div><div class='footsig'>Kori Pickle</div><div><span class='pill'>LinkedIn</span><span class='pill'>GitHub</span></div></div>", unsafe_allow_html=True)


def report_text(df, ratio, score, status):
    high = int((df["risk_level"] == "High").sum())
    return f"""HEALTHCARE OPERATIONS INTELLIGENCE
Created by Kori Pickle

Responsible AI Operations Evaluator

Executive Summary
This working study tool uses synthetic data to evaluate workflow risk explainability fairness alert readiness governance controls and safe export logic.

Core Metrics
Records reviewed {len(df)}
High risk records {high}
Fairness ratio {ratio}
Governance readiness {score} of 10
Pipeline status {status}

Responsible Use Boundary
This tool does not replace human review payer policy interpretation coding validation compliance oversight patient communication or operational leadership judgment.

Created by Kori Pickle
Kori Pickle
LinkedIn and GitHub
"""

with st.sidebar:
    st.markdown("<div class='sig'>Kori Pickle</div><div class='kicker'>Healthcare Operations Intelligence</div>", unsafe_allow_html=True)
    workspace = st.radio("Choose a workspace", ["Command Center", "Explainability", "Fairness Alerts", "Safe Pipeline", "Governance Checklist", "Portfolio Export"])
    n = st.slider("Synthetic record volume", 80, 500, 180, 20)
    safety_floor = st.slider("Fairness safety floor", 50, 95, 80, 5)
    st.markdown("<span class='pill'>White FFFFFF</span><span class='pill'>Vols Orange FF8200</span><span class='pill'>Black Typography</span>", unsafe_allow_html=True)

df = data_engine(n)
safe = make_safe(df)
fair_table, ratio = fairness(df)
brand()

if workspace == "Command Center":
    st.markdown("<div class='hero'><div class='eyebrow'>Responsible AI Operations Evaluator</div><div class='title'>A working audit tool for <span class='orange'>workflow risk governance</span></div><div class='copy'>This premium simulator evaluates synthetic healthcare operations records for explainability fairness alert readiness safe export logic and governance discipline.</div></div>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown(f"<div class='metricbox'><div class='big'>{len(df)}</div><div class='label'>Synthetic Records</div></div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='metricbox'><div class='big'>{int((df['risk_level'] == 'High').sum())}</div><div class='label'>High Risk Records</div></div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='metricbox'><div class='big'>{ratio}</div><div class='label'>Fairness Ratio</div></div>", unsafe_allow_html=True)
    c4.markdown("<div class='metricbox'><div class='big'>No</div><div class='label'>Protected Data Used</div></div>", unsafe_allow_html=True)
    st.markdown("<div class='section'>Live Workflow Snapshot</div>", unsafe_allow_html=True)
    st.dataframe(df.head(25), use_container_width=True, hide_index=True)
    st.download_button("Download synthetic audit data", df.to_csv(index=False), file_name="synthetic_responsible_ai_audit_data.csv", mime="text/csv")

elif workspace == "Explainability":
    st.markdown("<div class='section'>Explainability Workspace</div>", unsafe_allow_html=True)
    explain = pd.DataFrame({"factor": ["Authorization Age", "Documentation Gaps", "Queue Age", "Payer Pattern"], "weight": [38, 30, 20, 12]})
    st.bar_chart(explain.set_index("factor"))
    st.dataframe(explain, use_container_width=True, hide_index=True)
    selected = st.selectbox("Select a record", df["record_id"].head(50))
    row = df[df["record_id"] == selected].iloc[0]
    st.markdown(f"<div class='callout'>Selected record {selected}<br>Risk score {row['risk_score']}<br>Risk level {row['risk_level']}<br>Main signal authorization age {row['authorization_age_days']} days</div>", unsafe_allow_html=True)

elif workspace == "Fairness Alerts":
    st.markdown("<div class='section'>Fairness Alert Simulator</div>", unsafe_allow_html=True)
    st.dataframe(fair_table, use_container_width=True, hide_index=True)
    simulated = st.slider("Simulated fairness ratio", 0.50, 1.00, float(ratio), 0.01)
    if simulated < safety_floor / 100:
        st.error("Fairness alert triggered. Human review is required before operational use.")
        if st.button("Simulate team alert"):
            alert = {"system": "Responsible AI Operations Evaluator", "alert_type": "Fairness safety boundary crossed", "current_ratio": round(simulated, 2), "required_action": "Pause use and review group performance", "created_by": "Kori Pickle"}
            st.session_state.alerts.append(alert)
            st.success("Team alert simulated and logged")
            st.json(alert)
    else:
        st.success("Fairness bounds stable")
    st.dataframe(pd.DataFrame(st.session_state.alerts), use_container_width=True, hide_index=True)

elif workspace == "Safe Pipeline":
    st.markdown("<div class='section'>Safe Pipeline Simulator</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    c1.dataframe(df[["record_id", "payer_group", "workflow_area", "risk_score"]].head(8), use_container_width=True, hide_index=True)
    c2.dataframe(safe[["record_id", "payer_group", "workflow_area", "risk_score"]].head(8), use_container_width=True, hide_index=True)
    if st.button("Execute safe stream simulation"):
        progress = st.progress(0)
        for step in range(100):
            time.sleep(0.003)
            progress.progress(step + 1)
        event = {"pipeline_status": "Completed", "records_streamed": len(safe), "data_type": "Synthetic safe data", "destination": "Mock audit table"}
        st.session_state.pipeline.append(event)
        st.success("Safe export simulation completed")
    st.dataframe(pd.DataFrame(st.session_state.pipeline), use_container_width=True, hide_index=True)
    st.download_button("Download safe export", safe.to_csv(index=False), file_name="safe_mock_pipeline_export.csv", mime="text/csv")

elif workspace == "Governance Checklist":
    st.markdown("<div class='section'>Governance Checklist</div>", unsafe_allow_html=True)
    items = ["Uses synthetic safe data only", "Requires human review before action", "Explains workflow risk", "Identifies accountable owner", "Checks fairness across groups", "Provides alert logic", "Creates audit record", "Avoids clinical decision replacement", "Supports portfolio export", "Includes responsible use boundary"]
    done = [item for item in items if st.checkbox(item)]
    st.markdown(f"<div class='metricbox'><div class='big'>{len(done)} of 10</div><div class='label'>Governance Readiness Score</div></div>", unsafe_allow_html=True)
    st.text_area("Governance notes", height=150)

elif workspace == "Portfolio Export":
    st.markdown("<div class='section'>Portfolio Export</div>", unsafe_allow_html=True)
    readiness = st.slider("Governance score to include", 0, 10, 8)
    status = st.selectbox("Pipeline status", ["Not tested", "Simulated successfully", "Needs review"])
    report = report_text(df, ratio, readiness, status)
    st.text_area("Portfolio ready export", report, height=520)
    st.download_button("Download portfolio report", report, file_name="responsible_ai_operations_report.txt", mime="text/plain")

footer()
