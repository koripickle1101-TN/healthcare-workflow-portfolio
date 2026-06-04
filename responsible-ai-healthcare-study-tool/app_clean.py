import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(
    page_title="Responsible AI Governance Lab",
    page_icon="🟧",
    layout="wide",
    initial_sidebar_state="expanded",
)

ORANGE = "#FF8200"
WARM = "#E8E3DC"
SOFT = "#F7F4EF"
BLACK = "#000000"

st.markdown(
    f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:wght@700;800;900&family=Allura&display=swap');

html, body, [class*='css'] {{ font-family: Inter, sans-serif; color: {BLACK}; }}
.stApp {{ background: radial-gradient(circle at 92% 8%, rgba(255,130,0,.10), transparent 30%), linear-gradient(180deg, #FFFFFF 0%, #FFFFFF 76%, #FBF8F3 100%); }}
section[data-testid='stSidebar'] {{ background: #FFFFFF; border-right: 1px solid {WARM}; }}
.block-container {{ max-width: 1240px; padding-top: 1.2rem; padding-bottom: 2.8rem; }}

.brand-card {{ background: #FFFFFF; border: 1px solid {WARM}; border-radius: 30px; padding: 30px 28px; margin-bottom: 28px; box-shadow: 0 24px 64px rgba(0,0,0,.055); overflow: hidden; }}
.brand-signature {{ font-family: Allura, cursive; font-size: clamp(56px, 11vw, 96px); line-height: .88; color: #111111; text-align: center; margin-bottom: 22px; transform: rotate(-1deg); }}
.brand-line {{ height: 2px; width: 84%; margin: 14px auto 18px auto; background: linear-gradient(90deg, transparent, {ORANGE}, transparent); }}
.brand-kicker {{ text-align: center; font-size: clamp(14px, 3vw, 22px); letter-spacing: clamp(4px, 1.4vw, 9px); text-transform: uppercase; font-weight: 800; color: #111111; }}
.brand-intel {{ text-align: center; font-size: clamp(22px, 5vw, 38px); letter-spacing: clamp(5px, 1.6vw, 12px); text-transform: uppercase; color: {ORANGE}; font-weight: 900; line-height: 1.2; word-break: keep-all; }}

.hero {{ border: 1px solid {WARM}; border-radius: 34px; padding: clamp(30px, 5vw, 56px); background: linear-gradient(135deg, #FFFFFF 0%, #FFFFFF 67%, rgba(255,130,0,.08) 100%); box-shadow: 0 28px 78px rgba(0,0,0,.07); margin-bottom: 30px; }}
.eyebrow {{ font-size: 12px; letter-spacing: 3px; text-transform: uppercase; font-weight: 900; display: inline-block; padding-bottom: 8px; border-bottom: 2px solid {ORANGE}; margin-bottom: 24px; color: #333333; }}
.title {{ font-family: Playfair Display, serif; font-size: clamp(40px, 6vw, 82px); line-height: .96; letter-spacing: -2px; margin: 0 0 22px 0; color: #000000; }}
.orange {{ color: {ORANGE}; }}
.copy {{ max-width: 920px; font-size: 18px; line-height: 1.72; color: #242424; }}
.section-title {{ font-family: Playfair Display, serif; font-size: clamp(34px, 5vw, 52px); line-height: 1; letter-spacing: -1px; margin: 42px 0 18px 0; color: #000000; }}

.metric-card {{ border: 1px solid {WARM}; border-left: 5px solid {ORANGE}; border-radius: 22px; background: {SOFT}; padding: 22px; min-height: 128px; }}
.big {{ font-family: Playfair Display, serif; font-size: clamp(34px, 5vw, 50px); font-weight: 900; line-height: .95; color: #111111; }}
.label {{ font-size: 12px; font-weight: 900; letter-spacing: 1.4px; text-transform: uppercase; margin-top: 12px; color: #555555; }}
.card {{ border: 1px solid {WARM}; border-top: 5px solid {ORANGE}; border-radius: 26px; padding: 24px; background: #FFFFFF; box-shadow: 0 18px 48px rgba(0,0,0,.05); height: 100%; }}
.card-title {{ font-family: Playfair Display, serif; font-size: 28px; line-height: 1.08; margin-bottom: 12px; color: #000000; }}
.subtle {{ color: #353535; line-height: 1.68; font-size: 16px; }}
.callout {{ border: 1px solid {WARM}; border-left: 6px solid {ORANGE}; border-radius: 24px; padding: 22px 26px; background: #FFFFFF; box-shadow: 0 18px 44px rgba(0,0,0,.045); margin: 18px 0; color: #111111; }}

.node-grid {{ display: flex; flex-wrap: wrap; gap: 16px; align-items: center; margin-top: 30px; }}
.node {{ width: 62px; height: 62px; border-radius: 999px; border: 2px solid {ORANGE}; display: inline-flex; align-items: center; justify-content: center; color: {ORANGE}; background: #FFFFFF; font-weight: 900; box-shadow: 0 0 0 10px rgba(255,130,0,.07), 0 0 30px rgba(255,130,0,.18); flex: 0 0 auto; }}

.pill-row {{ display: flex; flex-wrap: wrap; gap: 9px; align-items: center; margin-top: 12px; }}
.pill {{ display: inline-flex; align-items: center; justify-content: center; border: 1px solid {ORANGE}; background: rgba(255,130,0,.08); border-radius: 999px; padding: 8px 13px; font-size: 12px; font-weight: 900; letter-spacing: .55px; text-transform: uppercase; color: #111111; white-space: nowrap; }}
.brand-system {{ border: 1px solid {WARM}; border-radius: 20px; background: {SOFT}; padding: 16px; margin-top: 18px; }}
.brand-system-title {{ font-weight: 900; text-transform: uppercase; letter-spacing: 1.5px; font-size: 11px; margin-bottom: 10px; }}
.brand-system-item {{ border-left: 3px solid {ORANGE}; padding: 6px 0 6px 10px; margin: 6px 0; font-size: 13px; font-weight: 700; }}

.footer {{ text-align: center; border-top: 1px solid {WARM}; margin-top: 60px; padding: 36px 0 22px 0; }}
.footer-sig {{ font-family: Allura, cursive; font-size: 50px; color: #111111; line-height: .9; margin-top: 8px; margin-bottom: 14px; }}
.footer-icon-row {{ display: flex; justify-content: center; gap: 12px; align-items: center; margin-top: 10px; }}
.footer-icon {{ border: 1px solid {WARM}; border-radius: 999px; padding: 8px 14px; background: #FFFFFF; font-size: 12px; font-weight: 900; letter-spacing: .7px; text-transform: uppercase; }}
.sidebar-brand {{ text-align: center; border: 1px solid {WARM}; border-radius: 24px; padding: 18px 12px; background: linear-gradient(180deg, #FFFFFF, rgba(255,130,0,.045)); margin-bottom: 18px; }}
.sidebar-sig {{ font-family: Allura, cursive; font-size: 46px; line-height: .85; color: #111111; }}
.sidebar-title {{ font-size: 11px; letter-spacing: 2px; text-transform: uppercase; font-weight: 900; margin-top: 10px; color: #111111; }}
.sidebar-caption {{ font-size: 12px; line-height: 1.55; color: #444444; margin-bottom: 12px; }}

div.stButton > button, div.stDownloadButton > button {{ border-radius: 999px; border: 1px solid {ORANGE}; background: {ORANGE}; color: white; font-weight: 900; padding: .72rem 1.1rem; }}
div.stButton > button:hover, div.stDownloadButton > button:hover {{ background: #111111; border: 1px solid #111111; color: white; }}

textarea {{ border-radius: 18px !important; font-family: Inter, sans-serif !important; line-height: 1.55 !important; }}

@media(max-width:760px) {{
    .brand-card {{ padding: 24px 18px; }}
    .brand-signature {{ font-size: 62px; }}
    .brand-kicker {{ letter-spacing: 4px; font-size: 14px; }}
    .brand-intel {{ letter-spacing: 5px; font-size: 24px; }}
    .hero {{ padding: 32px 24px; }}
    .node-grid {{ gap: 12px; }}
    .node {{ width: 54px; height: 54px; font-size: 13px; }}
    .pill-row {{ gap: 8px; }}
    .pill {{ font-size: 11px; padding: 7px 11px; }}
    .footer-icon-row {{ gap: 10px; }}
}}
</style>
""",
    unsafe_allow_html=True,
)

for key in ["alerts", "pipeline", "case_reviews"]:
    if key not in st.session_state:
        st.session_state[key] = []
if "governance_notes" not in st.session_state:
    st.session_state.governance_notes = ""


def brand_header():
    st.markdown(
        """
        <div class='brand-card'>
            <div class='brand-signature'>Kori Pickle</div>
            <div class='brand-line'></div>
            <div class='brand-kicker'>Healthcare Operations</div>
            <div class='brand-intel'>Intelligence</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def footer():
    st.markdown(
        """
        <div class='footer'>
            <div style='font-weight:900; letter-spacing:.5px;'>Created by Kori Pickle</div>
            <div class='footer-sig'>Kori Pickle</div>
            <div class='footer-icon-row'>
                <span class='footer-icon'>LinkedIn</span>
                <span class='footer-icon'>GitHub</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section(text):
    st.markdown(f"<div class='section-title'>{text}</div>", unsafe_allow_html=True)


def create_data(volume, payer_pressure, documentation_pressure, queue_pressure):
    rng = np.random.default_rng(42)
    data = pd.DataFrame(
        {
            "record_id": [f"CASE {i:04d}" for i in range(1, volume + 1)],
            "payer_group": rng.choice(["Commercial", "Medicaid", "Medicare", "Self Pay"], volume, p=[.44, .22, .28, .06]),
            "workflow_area": rng.choice(["Patient Access", "Prior Authorization", "Health Information", "Revenue Cycle"], volume),
            "service_line": rng.choice(["Orthopedics", "Cardiology", "Rehabilitation", "Imaging", "Primary Care"], volume),
            "documentation_score": rng.integers(55, 100, volume),
            "authorization_age_days": rng.integers(0, 14, volume),
            "queue_age_days": rng.integers(0, 18, volume),
            "handoff_count": rng.integers(1, 6, volume),
        }
    )
    payer_weight = data["payer_group"].map({"Commercial": 4, "Medicaid": 8 + payer_pressure, "Medicare": 6, "Self Pay": 10 + payer_pressure})
    data["risk_score"] = (
        100
        - data["documentation_score"]
        + data["authorization_age_days"] * 4
        + data["queue_age_days"] * 2
        + data["handoff_count"] * 3
        + payer_weight
        + documentation_pressure
        + queue_pressure
    ).clip(0, 100)
    data["risk_level"] = pd.cut(data["risk_score"], [-1, 35, 65, 100], labels=["Low", "Moderate", "High"])
    data["delay_flag"] = np.where(data["risk_score"] >= 60, 1, 0)
    data["recommended_action"] = "Continue standard workflow"
    data.loc[data["risk_score"] >= 55, "recommended_action"] = "Monitor and validate documentation"
    data.loc[data["risk_score"] >= 75, "recommended_action"] = "Escalate for human review"
    return data


def safe_export(data):
    safe = data.copy()
    safe["record_id"] = [f"SAFE {i:05d}" for i in range(1, len(safe) + 1)]
    return safe


def fairness_metrics(data):
    table = (
        data.groupby("payer_group", observed=True)
        .agg(
            records=("record_id", "count"),
            delay_rate=("delay_flag", "mean"),
            average_risk=("risk_score", "mean"),
            average_queue_age=("queue_age_days", "mean"),
        )
        .reset_index()
    )
    table["delay_rate"] = table["delay_rate"].round(3)
    table["average_risk"] = table["average_risk"].round(1)
    table["average_queue_age"] = table["average_queue_age"].round(1)
    high = table["delay_rate"].max()
    low = table["delay_rate"].min()
    ratio = 1.0 if high == 0 else round(low / high, 2)
    return table, ratio


def report_text(data, fairness_ratio, governance_score, pipeline_status, scenario_name):
    high_count = int((data["risk_level"] == "High").sum())
    moderate_count = int((data["risk_level"] == "Moderate").sum())
    return f"""HEALTHCARE OPERATIONS INTELLIGENCE
Created by Kori Pickle

Responsible AI Governance Lab

Executive Summary
This no data risk portfolio artifact uses synthetic healthcare operations records to evaluate workflow risk scoring, explainability, fairness alert readiness, safe export logic, governance controls, and responsible AI boundaries.

Scenario Reviewed
{scenario_name}

Core Metrics
Records reviewed: {len(data)}
High risk records: {high_count}
Moderate risk records: {moderate_count}
Fairness ratio: {fairness_ratio}
Governance readiness: {governance_score} of 10
Pipeline status: {pipeline_status}
Protected data used: No

Operational Interpretation
High risk records represent areas where workflow instability may require human review, documentation validation, payer follow up, or escalation. The fairness ratio supports review of whether operational delays appear uneven across payer groups.

Responsible Use Boundary
This tool does not replace human review, payer policy interpretation, coding validation, compliance oversight, patient communication, clinical judgment, or operational leadership decision making.

Portfolio Value
This artifact demonstrates healthcare operations intelligence through workflow risk scoring, fairness monitoring, safe data handling, governance review, scenario testing, and portfolio ready reporting.

Brand Identity
White background: FFFFFF
Tennessee Orange accent: FF8200
Black typography: 000000
Created by Kori Pickle
Signature: Kori Pickle
Footer: LinkedIn and GitHub
"""


with st.sidebar:
    st.markdown(
        """
        <div class='sidebar-brand'>
            <div class='sidebar-sig'>Kori Pickle</div>
            <div class='sidebar-title'>Healthcare Operations Intelligence</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("<div class='sidebar-caption'>Responsible AI, workflow intelligence, and healthcare operations governance.</div>", unsafe_allow_html=True)
    workspace = st.radio(
        "Choose a workspace",
        [
            "Executive Command Center",
            "Risk Explorer",
            "Explainability Studio",
            "Fairness Alert Lab",
            "Safe Pipeline Simulator",
            "Governance Checklist",
            "Scenario Stress Test",
            "Portfolio Export",
        ],
    )
    st.divider()
    volume = st.slider("Synthetic record volume", 100, 700, 220, 20)
    safety_floor = st.slider("Fairness safety floor", 50, 95, 80, 5)
    payer_pressure = st.slider("Payer friction pressure", 0, 20, 8, 1)
    documentation_pressure = st.slider("Documentation instability", 0, 20, 6, 1)
    queue_pressure = st.slider("Queue aging pressure", 0, 20, 6, 1)
    st.markdown(
        """
        <div class='brand-system'>
            <div class='brand-system-title'>Brand System</div>
            <div class='brand-system-item'>White background: FFFFFF</div>
            <div class='brand-system-item'>Vols Orange accent: FF8200</div>
            <div class='brand-system-item'>Black typography: 000000</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

data = create_data(volume, payer_pressure, documentation_pressure, queue_pressure)
safe = safe_export(data)
fair_table, fairness_ratio = fairness_metrics(data)
risk_high = int((data["risk_level"] == "High").sum())
risk_moderate = int((data["risk_level"] == "Moderate").sum())

brand_header()

if workspace == "Executive Command Center":
    st.markdown(
        """
        <div class='hero'>
            <div class='eyebrow'>Responsible AI Governance Lab</div>
            <div class='title'>A premium command center for <span class='orange'>workflow risk governance</span></div>
            <div class='copy'>This interactive healthcare operations simulator uses synthetic data to evaluate workflow risk, explainability, fairness alert readiness, safe export logic, governance controls, and responsible AI boundaries. It is built as a no data risk portfolio artifact for demonstrating operational judgment, not as a clinical or payer decision tool.</div>
            <div class='node-grid'>
                <span class='node'>AI</span>
                <span class='node'>Risk</span>
                <span class='node'>Fair</span>
                <span class='node'>Data</span>
                <span class='node'>Gov</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown(f"<div class='metric-card'><div class='big'>{len(data)}</div><div class='label'>Synthetic Records</div></div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='metric-card'><div class='big'>{risk_high}</div><div class='label'>High Risk Records</div></div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='metric-card'><div class='big'>{fairness_ratio}</div><div class='label'>Fairness Ratio</div></div>", unsafe_allow_html=True)
    c4.markdown("<div class='metric-card'><div class='big'>No</div><div class='label'>Protected Data Used</div></div>", unsafe_allow_html=True)
    section("Operational Snapshot")
    left, right = st.columns([1.3, 0.7])
    with left:
        st.dataframe(data.head(30), use_container_width=True, hide_index=True)
    with right:
        st.markdown(f"""
        <div class='card'>
            <div class='card-title'>Executive Interpretation</div>
            <div class='subtle'>High risk records show where workflow instability may require human review. The fairness ratio shows whether delay patterns appear uneven across payer groups. The pipeline workspace demonstrates safe export logic using synthetic records only.</div>
            <div class='pill-row'>
                <span class='pill'>High Risk {risk_high}</span>
                <span class='pill'>Moderate Risk {risk_moderate}</span>
                <span class='pill'>Fairness {fairness_ratio}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.download_button("Download synthetic audit data", data.to_csv(index=False), file_name="synthetic_responsible_ai_governance_data.csv", mime="text/csv")

elif workspace == "Risk Explorer":
    section("Risk Explorer")
    st.markdown("<div class='callout'>Use the filters below to inspect where operational pressure is forming by payer group, workflow area, service line, and risk level.</div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    payer_filter = c1.multiselect("Payer group", sorted(data["payer_group"].unique()), default=sorted(data["payer_group"].unique()))
    area_filter = c2.multiselect("Workflow area", sorted(data["workflow_area"].unique()), default=sorted(data["workflow_area"].unique()))
    level_filter = c3.multiselect("Risk level", ["Low", "Moderate", "High"], default=["Low", "Moderate", "High"])
    filtered = data[data["payer_group"].isin(payer_filter) & data["workflow_area"].isin(area_filter) & data["risk_level"].astype(str).isin(level_filter)]
    st.dataframe(filtered, use_container_width=True, hide_index=True)
    st.bar_chart(filtered.groupby("workflow_area", observed=True)["risk_score"].mean())

elif workspace == "Explainability Studio":
    section("Explainability Studio")
    explain = pd.DataFrame({
        "factor": ["Authorization Age", "Documentation Gaps", "Queue Age", "Handoff Count", "Payer Friction"],
        "impact_weight": [34, 28, 18, 12, 8],
        "plain_language_meaning": ["Older authorizations increase downstream risk", "Lower documentation readiness increases preventable rework", "Aging queues indicate operational pressure", "More handoffs can create accountability gaps", "Payer patterns require fairness and access review"],
    })
    left, right = st.columns([0.9, 1.1])
    with left:
        st.bar_chart(explain.set_index("factor")[["impact_weight"]])
    with right:
        st.dataframe(explain, use_container_width=True, hide_index=True)
    selected = st.selectbox("Select a record to explain", data["record_id"].head(80))
    row = data[data["record_id"] == selected].iloc[0]
    st.markdown(f"""
    <div class='callout'>
        Selected record: {selected}<br>
        Risk score: {row['risk_score']}<br>
        Risk level: {row['risk_level']}<br>
        Main signal: authorization age {row['authorization_age_days']} days<br>
        Recommended action: {row['recommended_action']}
    </div>
    """, unsafe_allow_html=True)
    if st.button("Save case review"):
        st.session_state.case_reviews.append({"record_id": selected, "risk_score": int(row["risk_score"]), "action": row["recommended_action"]})
        st.success("Case review saved")

elif workspace == "Fairness Alert Lab":
    section("Fairness Alert Lab")
    st.dataframe(fair_table, use_container_width=True, hide_index=True)
    simulated_ratio = st.slider("Simulated fairness ratio", 0.50, 1.00, float(fairness_ratio), 0.01)
    st.markdown(f"<div class='metric-card'><div class='big'>{simulated_ratio:.2f}</div><div class='label'>Current Fairness Ratio</div></div>", unsafe_allow_html=True)
    if simulated_ratio < safety_floor / 100:
        st.error("Fairness alert triggered. Human review is required before operational use.")
        if st.button("Simulate team alert"):
            alert = {"system": "Responsible AI Governance Lab", "alert_type": "Fairness safety boundary crossed", "current_ratio": round(simulated_ratio, 2), "required_action": "Pause use and review group performance", "created_by": "Kori Pickle"}
            st.session_state.alerts.append(alert)
            st.success("Team alert simulated and logged")
            st.json(alert)
    else:
        st.success("Fairness bounds stable")
    st.dataframe(pd.DataFrame(st.session_state.alerts), use_container_width=True, hide_index=True)

elif workspace == "Safe Pipeline Simulator":
    section("Safe Pipeline Simulator")
    left, right = st.columns(2)
    with left:
        st.markdown("<div class='card-title'>Standard Synthetic Feed</div>", unsafe_allow_html=True)
        st.dataframe(data[["record_id", "payer_group", "workflow_area", "risk_score"]].head(10), use_container_width=True, hide_index=True)
    with right:
        st.markdown("<div class='card-title'>Safe Downstream Export</div>", unsafe_allow_html=True)
        st.dataframe(safe[["record_id", "payer_group", "workflow_area", "risk_score"]].head(10), use_container_width=True, hide_index=True)
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
    section("Governance Checklist")
    items = ["Uses synthetic safe data only", "Requires human review before action", "Explains workflow risk clearly", "Identifies accountable workflow owner", "Checks fairness across groups", "Provides alert logic for safety boundaries", "Creates audit record for activity", "Avoids clinical decision replacement", "Supports portfolio export", "Includes responsible use boundary"]
    completed = []
    cols = st.columns(2)
    for index, item in enumerate(items):
        with cols[index % 2]:
            if st.checkbox(item):
                completed.append(item)
    readiness_score = len(completed)
    st.markdown(f"<div class='metric-card'><div class='big'>{readiness_score} of 10</div><div class='label'>Governance Readiness Score</div></div>", unsafe_allow_html=True)
    if readiness_score >= 8:
        st.success("Strong governance foundation")
    elif readiness_score >= 5:
        st.warning("Partial governance foundation")
    else:
        st.error("High governance risk")
    st.session_state.governance_notes = st.text_area("Governance notes", st.session_state.governance_notes, height=160)

elif workspace == "Scenario Stress Test":
    section("Scenario Stress Test")
    scenario = st.selectbox("Select stress test", ["Payer policy shift", "Documentation backlog", "Authorization staffing shortage", "Queue aging surge"])
    st.markdown(f"<div class='callout'>Current scenario: {scenario}. Adjust the pressure sliders in the sidebar to simulate how workflow instability changes risk volume and fairness results.</div>", unsafe_allow_html=True)
    summary = data.groupby(["workflow_area", "risk_level"], observed=True).size().reset_index(name="records")
    st.dataframe(summary, use_container_width=True, hide_index=True)
    st.bar_chart(data.groupby("workflow_area", observed=True)["risk_score"].mean())
    if st.button("Save stress test snapshot"):
        st.session_state.case_reviews.append({"scenario": scenario, "high_risk_records": risk_high, "fairness_ratio": fairness_ratio})
        st.success("Stress test snapshot saved")

elif workspace == "Portfolio Export":
    section("Portfolio Export")
    governance_score = st.slider("Governance score to include", 0, 10, 8)
    pipeline_status = st.selectbox("Pipeline status", ["Not tested", "Simulated successfully", "Needs review"])
    scenario_name = st.selectbox("Scenario label", ["Baseline simulation", "Payer policy shift", "Documentation backlog", "Authorization staffing shortage", "Queue aging surge"])
    report = report_text(data, fairness_ratio, governance_score, pipeline_status, scenario_name)
    st.text_area("Portfolio ready export", report, height=560)
    st.download_button("Download portfolio report", report, file_name="responsible_ai_governance_lab_report.txt", mime="text/plain")

footer()
