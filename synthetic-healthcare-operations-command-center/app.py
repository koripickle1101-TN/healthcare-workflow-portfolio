import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Healthcare Operations Command Center",
    page_icon="🟧",
    layout="wide",
    initial_sidebar_state="expanded",
)

ORANGE = "#FF8200"
BLACK = "#000000"
WHITE = "#FFFFFF"
WARM = "#E8E3DC"
SOFT = "#F7F4EF"
CHARCOAL = "#151515"

LINKEDIN_URL = "https://www.linkedin.com/in/kori-p-865jct"
GITHUB_URL = "https://github.com/koripickle1101-TN"
REPO_URL = "https://github.com/koripickle1101-TN/healthcare-workflow-portfolio"

st.markdown(
    f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Allura&family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:wght@700;800;900&display=swap');

html, body, [class*='css'] {{ font-family: Inter, sans-serif; color: {BLACK}; }}
.stApp {{ background: radial-gradient(circle at 93% 3%, rgba(255,130,0,.10), transparent 28%), linear-gradient(180deg, #FFFFFF 0%, #FFFFFF 68%, #FBF8F3 100%); }}
.block-container {{ max-width: 1320px; padding-top: 1.1rem; padding-bottom: 3.2rem; }}
section[data-testid='stSidebar'] {{ background: #FFFFFF; border-right: 1px solid {WARM}; }}
section[data-testid='stSidebar'] .block-container {{ padding-top: 1.2rem; }}

.brand-card {{ background: #FFFFFF; border: 1px solid {WARM}; border-radius: 30px; padding: 28px 24px; margin-bottom: 28px; box-shadow: 0 24px 64px rgba(0,0,0,.055); overflow: hidden; }}
.brand-signature {{ font-family: Allura, cursive; font-size: clamp(56px, 10vw, 96px); line-height: .88; color: #111111; text-align: center; margin-bottom: 22px; transform: rotate(-1deg); }}
.brand-line {{ height: 2px; width: 84%; margin: 14px auto 18px auto; background: linear-gradient(90deg, transparent, {ORANGE}, transparent); }}
.brand-kicker {{ text-align: center; font-size: clamp(14px, 3vw, 22px); letter-spacing: clamp(4px, 1.4vw, 9px); text-transform: uppercase; font-weight: 800; color: #111111; }}
.brand-intel {{ text-align: center; font-size: clamp(22px, 5vw, 38px); letter-spacing: clamp(5px, 1.6vw, 12px); text-transform: uppercase; color: {ORANGE}; font-weight: 900; line-height: 1.2; }}

.hero {{ border: 1px solid {WARM}; border-radius: 34px; padding: clamp(30px, 5vw, 58px); background: linear-gradient(135deg, #FFFFFF 0%, #FFFFFF 68%, rgba(255,130,0,.085) 100%); box-shadow: 0 28px 78px rgba(0,0,0,.07); margin-bottom: 30px; }}
.eyebrow {{ font-size: 12px; letter-spacing: 3px; text-transform: uppercase; font-weight: 900; display: inline-block; padding-bottom: 8px; border-bottom: 2px solid {ORANGE}; margin-bottom: 24px; color: #333333; }}
.title {{ font-family: Playfair Display, serif; font-size: clamp(39px, 6vw, 78px); line-height: .96; letter-spacing: -2px; margin: 0 0 22px 0; color: #000000; }}
.orange {{ color: {ORANGE}; }}
.copy {{ max-width: 960px; font-size: 18px; line-height: 1.72; color: #242424; }}
.section-title {{ font-family: Playfair Display, serif; font-size: clamp(33px, 5vw, 54px); line-height: 1; letter-spacing: -1px; margin: 42px 0 18px 0; color: #000000; }}

.metric-card {{ border: 1px solid {WARM}; border-left: 5px solid {ORANGE}; border-radius: 22px; background: {SOFT}; padding: 22px; min-height: 132px; box-shadow: 0 14px 34px rgba(0,0,0,.035); }}
.big {{ font-family: Inter, sans-serif; font-size: clamp(32px, 4.3vw, 48px); font-weight: 900; letter-spacing: -1.5px; line-height: .95; color: #111111; }}
.label {{ font-size: 12px; font-weight: 900; letter-spacing: 1.4px; text-transform: uppercase; margin-top: 12px; color: #555555; }}
.metric-note {{ font-size: 12px; color: #666666; margin-top: 8px; line-height: 1.35; }}
.card {{ border: 1px solid {WARM}; border-top: 5px solid {ORANGE}; border-radius: 26px; padding: 24px; background: #FFFFFF; box-shadow: 0 18px 48px rgba(0,0,0,.05); height: 100%; }}
.card-title {{ font-family: Playfair Display, serif; font-size: 29px; line-height: 1.08; margin-bottom: 12px; color: #000000; }}
.subtle {{ color: #353535; line-height: 1.68; font-size: 16px; }}
.callout {{ border: 1px solid {WARM}; border-left: 6px solid {ORANGE}; border-radius: 24px; padding: 22px 26px; background: #FFFFFF; box-shadow: 0 18px 44px rgba(0,0,0,.045); margin: 18px 0; color: #111111; line-height: 1.65; }}
.black-panel {{ background: {CHARCOAL}; color: #FFFFFF; border-radius: 24px; padding: 24px; box-shadow: 0 24px 52px rgba(0,0,0,.12); }}
.black-panel-title {{ font-family: Playfair Display, serif; font-size: 31px; color: #FFFFFF; margin-bottom: 10px; }}
.black-panel-copy {{ color: #F3F3F3; line-height: 1.65; }}

.node-grid {{ display: flex; flex-wrap: wrap; gap: 18px; align-items: center; margin-top: 30px; }}
.node {{ width: 66px; height: 66px; border-radius: 999px; border: 2px solid {ORANGE}; display: inline-flex; align-items: center; justify-content: center; color: {ORANGE}; background: #FFFFFF; font-weight: 900; box-shadow: 0 0 0 10px rgba(255,130,0,.07), 0 0 30px rgba(255,130,0,.18); flex: 0 0 auto; }}
.pill-row {{ display: flex; flex-wrap: wrap; gap: 12px; align-items: center; margin-top: 16px; }}
.pill {{ display: inline-flex; align-items: center; justify-content: center; border: 1px solid {ORANGE}; background: rgba(255,130,0,.08); border-radius: 999px; padding: 8px 14px; font-size: 12px; font-weight: 900; letter-spacing: .55px; text-transform: uppercase; color: #111111; white-space: nowrap; }}
.status-dot {{ display: inline-block; width: 10px; height: 10px; border-radius: 99px; background: {ORANGE}; margin-right: 8px; box-shadow: 0 0 0 7px rgba(255,130,0,.12); }}

.brand-system {{ border: 1px solid {WARM}; border-radius: 20px; background: {SOFT}; padding: 16px; margin-top: 18px; }}
.brand-system-title {{ font-weight: 900; text-transform: uppercase; letter-spacing: 1.5px; font-size: 11px; margin-bottom: 10px; }}
.brand-system-item {{ border-left: 3px solid {ORANGE}; padding: 6px 0 6px 10px; margin: 6px 0; font-size: 13px; font-weight: 700; }}
.sidebar-brand {{ text-align: center; border: 1px solid {WARM}; border-radius: 24px; padding: 18px 12px; background: linear-gradient(180deg, #FFFFFF, rgba(255,130,0,.045)); margin-bottom: 18px; }}
.sidebar-sig {{ font-family: Allura, cursive; font-size: 46px; line-height: .85; color: #111111; }}
.sidebar-title {{ font-size: 11px; letter-spacing: 2px; text-transform: uppercase; font-weight: 900; margin-top: 10px; color: #111111; }}
.sidebar-caption {{ font-size: 12px; line-height: 1.55; color: #444444; margin-bottom: 12px; }}

.footer {{ text-align: center; border-top: 1px solid {WARM}; margin-top: 60px; padding: 38px 0 28px 0; }}
.footer-created {{ font-weight: 900; letter-spacing: .5px; color: #111111; }}
.footer-sig {{ font-family: Allura, cursive; font-size: 54px; color: #111111; line-height: .9; margin-top: 8px; margin-bottom: 18px; }}
.footer-icon-row {{ display: flex; justify-content: center; gap: 14px; align-items: center; margin-top: 12px; flex-wrap: wrap; }}
.footer-link {{ display: inline-flex; align-items: center; justify-content: center; border: 1.5px solid {ORANGE}; border-radius: 999px; padding: 10px 18px; background: #FFFFFF; color: #111111 !important; font-size: 13px; font-weight: 900; letter-spacing: .7px; text-transform: uppercase; text-decoration: none !important; box-shadow: 0 12px 28px rgba(255,130,0,.10); }}
.footer-link:hover {{ background: {ORANGE}; color: #FFFFFF !important; }}
.footer-url {{ margin-top: 14px; font-size: 12px; color: #333333; word-break: break-word; }}
.footer-url a {{ color: #111111 !important; font-weight: 800; text-decoration: underline; text-decoration-color: {ORANGE}; }}

div.stButton > button, div.stDownloadButton > button {{ border-radius: 999px; border: 1px solid {ORANGE}; background: {ORANGE}; color: white; font-weight: 900; padding: .72rem 1.1rem; }}
div.stButton > button:hover, div.stDownloadButton > button:hover {{ background: #111111; border: 1px solid #111111; color: white; }}
textarea {{ border-radius: 18px !important; font-family: Inter, sans-serif !important; line-height: 1.55 !important; }}
[data-testid='stDataFrame'] {{ border: 1px solid {WARM}; border-radius: 18px; overflow: hidden; }}

@media(max-width:760px) {{
    .brand-card {{ padding: 24px 18px; }}
    .brand-signature {{ font-size: 62px; }}
    .brand-kicker {{ letter-spacing: 4px; font-size: 14px; }}
    .brand-intel {{ letter-spacing: 5px; font-size: 24px; }}
    .hero {{ padding: 32px 24px; }}
    .node-grid {{ gap: 12px; }}
    .node {{ width: 56px; height: 56px; font-size: 13px; }}
    .pill-row {{ gap: 9px; }}
    .pill {{ font-size: 11px; padding: 7px 11px; }}
    .footer-link {{ min-width: 112px; padding: 10px 14px; font-size: 12px; }}
}}
</style>
""",
    unsafe_allow_html=True,
)

for key in ["saved_cases", "alert_log", "pipeline_log", "governance_notes", "command_notes"]:
    if key not in st.session_state:
        st.session_state[key] = [] if key not in ["governance_notes", "command_notes"] else ""


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
        f"""
        <div class='footer'>
            <div class='footer-created'>Created by Kori Pickle</div>
            <div class='footer-sig'>Kori Pickle</div>
            <div class='footer-icon-row'>
                <a class='footer-link' href='{LINKEDIN_URL}' target='_blank' rel='noopener noreferrer'>Open LinkedIn</a>
                <a class='footer-link' href='{GITHUB_URL}' target='_blank' rel='noopener noreferrer'>Open GitHub</a>
            </div>
            <div class='footer-url'>Portfolio repository: <a href='{REPO_URL}' target='_blank' rel='noopener noreferrer'>healthcare workflow portfolio</a></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section(text):
    st.markdown(f"<div class='section-title'>{text}</div>", unsafe_allow_html=True)


def create_synthetic_operations_data(volume, payer_pressure, documentation_pressure, staffing_pressure, queue_pressure, denial_pressure, operating_mode, service_focus):
    rng = np.random.default_rng(1101)
    start_date = datetime.today() - timedelta(days=30)
    payer_mix = {
        "Balanced": [.36, .25, .21, .11, .07],
        "Government Heavy": [.22, .36, .30, .07, .05],
        "Commercial Heavy": [.55, .18, .13, .10, .04],
        "High Self Pay Exposure": [.30, .22, .18, .10, .20],
    }.get(operating_mode, [.36, .25, .21, .11, .07])
    service_lines = ["Orthopedics", "Cardiology", "Rehabilitation", "Imaging", "Primary Care", "Specialty Pharmacy"]
    service_probs = np.ones(len(service_lines)) / len(service_lines)
    if service_focus in service_lines:
        service_probs = np.array([.10, .10, .10, .10, .10, .10])
        service_probs[service_lines.index(service_focus)] = .50
        service_probs = service_probs / service_probs.sum()

    records = pd.DataFrame(
        {
            "case_id": [f"AUTH {i:05d}" for i in range(1, volume + 1)],
            "payer_group": rng.choice(["Commercial", "Medicare", "Medicaid", "Marketplace", "Self Pay"], volume, p=payer_mix),
            "workflow_area": rng.choice(["Eligibility Verification", "Prior Authorization", "Patient Access", "Documentation Review", "Denial Prevention"], volume, p=[.19, .31, .20, .18, .12]),
            "service_line": rng.choice(service_lines, volume, p=service_probs),
            "request_age_days": rng.integers(0, 18, volume),
            "queue_age_days": rng.integers(0, 20, volume),
            "documentation_score": rng.integers(58, 100, volume),
            "eligibility_status": rng.choice(["Verified", "Needs Recheck", "Mismatch", "Missing"], volume, p=[.61, .20, .13, .06]),
            "authorization_status": rng.choice(["Not Started", "Pending", "Submitted", "Approved", "Escalated"], volume, p=[.13, .31, .27, .22, .07]),
            "staffing_capacity": rng.integers(62, 101, volume),
            "handoff_count": rng.integers(1, 7, volume),
            "days_to_visit": rng.integers(0, 21, volume),
            "expected_revenue": rng.integers(450, 14500, volume),
        }
    )
    records["created_date"] = [(start_date + timedelta(days=int(x))).strftime("%Y-%m-%d") for x in rng.integers(0, 30, volume)]

    payer_weight = records["payer_group"].map({"Commercial": 2, "Medicare": 4, "Medicaid": 6, "Marketplace": 6, "Self Pay": 8}) + payer_pressure * 0.65
    eligibility_weight = records["eligibility_status"].map({"Verified": 0, "Needs Recheck": 6, "Mismatch": 12, "Missing": 15})
    status_weight = records["authorization_status"].map({"Approved": 0, "Submitted": 5, "Pending": 9, "Not Started": 13, "Escalated": 16})
    workflow_weight = records["workflow_area"].map({"Eligibility Verification": 5, "Prior Authorization": 9, "Patient Access": 4, "Documentation Review": 7, "Denial Prevention": 8})

    raw_score = (
        22
        + (100 - records["documentation_score"]) * 0.45
        + records["request_age_days"] * 1.65
        + records["queue_age_days"] * 1.35
        + records["handoff_count"] * 2.1
        + (100 - records["staffing_capacity"]) * 0.28
        + np.maximum(0, 7 - records["days_to_visit"]) * 1.15
        + payer_weight
        + eligibility_weight
        + status_weight
        + workflow_weight
        + documentation_pressure * 0.70
        + staffing_pressure * 0.65
        + queue_pressure * 0.72
        + denial_pressure * 0.58
    )
    records["risk_score"] = raw_score.round(0).clip(0, 100).astype(int)
    records["risk_level"] = pd.cut(records["risk_score"], bins=[-1, 39, 69, 100], labels=["Low", "Moderate", "High"])
    records["delay_flag"] = np.where(records["risk_score"] >= 65, 1, 0)
    records["financial_exposure"] = np.where(records["risk_score"] >= 70, records["expected_revenue"] * (records["risk_score"] / 100) * 0.38, records["expected_revenue"] * .06).round(0).astype(int)
    records["recommended_action"] = "Continue standard monitoring"
    records.loc[records["risk_score"] >= 48, "recommended_action"] = "Review documentation and queue status"
    records.loc[records["risk_score"] >= 70, "recommended_action"] = "Escalate for human review"
    records.loc[records["risk_score"] >= 86, "recommended_action"] = "Immediate workflow intervention required"
    records["owner_queue"] = np.select(
        [
            records["workflow_area"].eq("Prior Authorization"),
            records["workflow_area"].eq("Eligibility Verification"),
            records["workflow_area"].eq("Documentation Review"),
            records["workflow_area"].eq("Denial Prevention"),
        ],
        ["Authorization Team", "Patient Access", "HIM Documentation", "Revenue Cycle Review"],
        default="Front Office Operations",
    )
    return records


def fairness_summary(records):
    table = records.groupby("payer_group", observed=True).agg(
        records=("case_id", "count"),
        delay_rate=("delay_flag", "mean"),
        average_risk=("risk_score", "mean"),
        average_queue_age=("queue_age_days", "mean"),
        exposure=("financial_exposure", "sum"),
        escalation_volume=("recommended_action", lambda x: (x == "Immediate workflow intervention required").sum()),
    ).reset_index()
    table["delay_rate"] = table["delay_rate"].round(3)
    table["average_risk"] = table["average_risk"].round(1)
    table["average_queue_age"] = table["average_queue_age"].round(1)
    high = table["delay_rate"].max()
    low = table["delay_rate"].min()
    ratio = 1.0 if high == 0 else round(low / high, 2)
    return table, ratio


def safe_export(records):
    safe = records.copy()
    safe["case_id"] = [f"SAFE AUTH {i:05d}" for i in range(1, len(safe) + 1)]
    safe["created_date"] = "Synthetic date bucket"
    return safe


def make_report(records, fairness_ratio, scenario, governance_score, pipeline_status, operating_mode, service_focus):
    high = int((records["risk_level"] == "High").sum())
    moderate = int((records["risk_level"] == "Moderate").sum())
    avg_risk = round(float(records["risk_score"].mean()), 1)
    exposure = int(records["financial_exposure"].sum())
    top_area = records.groupby("workflow_area", observed=True)["risk_score"].mean().sort_values(ascending=False).index[0]
    return f"""HEALTHCARE OPERATIONS INTELLIGENCE
Created by Kori Pickle

Synthetic Healthcare Operations Command Center

Executive Summary
This no PHI healthcare operations command center uses synthetic records to simulate patient access, eligibility verification, prior authorization, documentation review, and denial prevention workflow risk. It is designed to demonstrate operational judgment, workflow visibility, responsible AI governance, and safe data logic without using real patient records.

Scenario Reviewed
{scenario}

Operating Mode
{operating_mode}

Service Line Focus
{service_focus}

Core Metrics
Synthetic records reviewed: {len(records)}
Average risk score: {avg_risk}
High risk records: {high}
Moderate risk records: {moderate}
Estimated synthetic financial exposure: ${exposure:,}
Fairness ratio: {fairness_ratio}
Primary pressure area: {top_area}
Governance readiness score: {governance_score} of 10
Pipeline status: {pipeline_status}
Protected data used: No

Operational Interpretation
The command center identifies where synthetic workflow records show elevated risk because of delayed authorization activity, queue aging, documentation instability, eligibility issues, payer friction, handoff burden, or staffing pressure. High risk records are not automated decisions. They are review signals requiring human validation.

Responsible Use Boundary
This tool does not replace human review, payer policy interpretation, clinical judgment, coding validation, compliance oversight, patient communication, or leadership decision making. It is a portfolio demonstration of healthcare operations logic using synthetic data only.

Recommended Next Steps
Review high risk authorization and patient access records first.
Validate documentation readiness before downstream claim submission.
Monitor payer groups with uneven delay patterns.
Use safe export records for reporting and portfolio demonstration only.
Document governance review before presenting AI supported operational findings.

Brand Identity
White background: FFFFFF
Tennessee Orange accent: FF8200
Black typography: 000000
Created by Kori Pickle
LinkedIn: {LINKEDIN_URL}
GitHub: {GITHUB_URL}
Portfolio Repository: {REPO_URL}
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
    st.markdown("<div class='sidebar-caption'>Synthetic no PHI operations data, workflow risk scoring, prior authorization, patient access, denial prevention, and responsible AI governance.</div>", unsafe_allow_html=True)
    workspace = st.radio(
        "Choose a workspace",
        [
            "Executive Command Center",
            "Live Operations Board",
            "Synthetic Data Lab",
            "Prior Authorization Risk Queue",
            "Payer Fairness Monitor",
            "Explainability Studio",
            "Safe Export Pipeline",
            "Governance Checklist",
            "Portfolio Report Builder",
        ],
    )
    st.divider()
    operating_mode = st.selectbox("Operating mode", ["Balanced", "Government Heavy", "Commercial Heavy", "High Self Pay Exposure"])
    service_focus = st.selectbox("Service line focus", ["Balanced", "Orthopedics", "Cardiology", "Rehabilitation", "Imaging", "Primary Care", "Specialty Pharmacy"])
    volume = st.slider("Synthetic record volume", 100, 900, 260, 20)
    payer_pressure = st.slider("Payer friction pressure", 0, 25, 8, 1)
    documentation_pressure = st.slider("Documentation instability", 0, 25, 7, 1)
    staffing_pressure = st.slider("Staffing pressure", 0, 25, 8, 1)
    queue_pressure = st.slider("Queue aging pressure", 0, 25, 8, 1)
    denial_pressure = st.slider("Denial trend pressure", 0, 25, 6, 1)
    safety_floor = st.slider("Fairness safety floor", 50, 95, 80, 5)
    st.markdown(
        """
        <div class='brand-system'>
            <div class='brand-system-title'>Data Safety Standard</div>
            <div class='brand-system-item'>Synthetic records only</div>
            <div class='brand-system-item'>No patient identifiers</div>
            <div class='brand-system-item'>No protected health information</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

records = create_synthetic_operations_data(volume, payer_pressure, documentation_pressure, staffing_pressure, queue_pressure, denial_pressure, operating_mode, service_focus)
fair_table, fairness_ratio = fairness_summary(records)
safe_records = safe_export(records)
high_count = int((records["risk_level"] == "High").sum())
moderate_count = int((records["risk_level"] == "Moderate").sum())
low_count = int((records["risk_level"] == "Low").sum())
average_risk = round(float(records["risk_score"].mean()), 1)
escalations = int((records["recommended_action"] == "Immediate workflow intervention required").sum())
exposure = int(records["financial_exposure"].sum())
sla_at_risk = int(((records["request_age_days"] >= 7) & (records["authorization_status"] != "Approved")).sum())

brand_header()

if workspace == "Executive Command Center":
    st.markdown(
        """
        <div class='hero'>
            <div class='eyebrow'>Synthetic Healthcare Operations Command Center</div>
            <div class='title'>A real workflow tool powered by <span class='orange'>synthetic no PHI data</span></div>
            <div class='copy'>This interactive command center simulates patient access, eligibility verification, prior authorization, documentation review, and denial prevention workflows. It calculates operational risk, prioritizes review queues, estimates synthetic financial exposure, monitors payer fairness patterns, and exports portfolio ready reports without using real patient data.</div>
            <div class='node-grid'>
                <span class='node'>PA</span>
                <span class='node'>EV</span>
                <span class='node'>RCM</span>
                <span class='node'>HIM</span>
                <span class='node'>Gov</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown(f"<div class='metric-card'><div class='big'>{len(records)}</div><div class='label'>Synthetic Records</div><div class='metric-note'>No PHI used</div></div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='metric-card'><div class='big'>{high_count}</div><div class='label'>High Risk Cases</div><div class='metric-note'>Require operational review</div></div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='metric-card'><div class='big'>{average_risk}</div><div class='label'>Average Risk Score</div><div class='metric-note'>Interpreted as workflow pressure</div></div>", unsafe_allow_html=True)
    c4.markdown(f"<div class='metric-card'><div class='big'>${exposure:,}</div><div class='label'>Synthetic Exposure</div><div class='metric-note'>Demo revenue risk estimate</div></div>", unsafe_allow_html=True)
    c5, c6, c7, c8 = st.columns(4)
    c5.markdown(f"<div class='metric-card'><div class='big'>{fairness_ratio}</div><div class='label'>Fairness Ratio</div><div class='metric-note'>Payer delay pattern check</div></div>", unsafe_allow_html=True)
    c6.markdown(f"<div class='metric-card'><div class='big'>{sla_at_risk}</div><div class='label'>SLA At Risk</div><div class='metric-note'>Open requests older than 7 days</div></div>", unsafe_allow_html=True)
    c7.markdown(f"<div class='metric-card'><div class='big'>{escalations}</div><div class='label'>Intervention Signals</div><div class='metric-note'>Human review required</div></div>", unsafe_allow_html=True)
    c8.markdown(f"<div class='metric-card'><div class='big'>No</div><div class='label'>Protected Data Used</div><div class='metric-note'>Synthetic records only</div></div>", unsafe_allow_html=True)

    section("Operational Snapshot")
    left, right = st.columns([1.25, .75])
    with left:
        st.dataframe(records.sort_values("risk_score", ascending=False).head(40), use_container_width=True, hide_index=True)
    with right:
        risk_mix = pd.DataFrame({"Risk Level": ["High", "Moderate", "Low"], "Records": [high_count, moderate_count, low_count]})
        st.markdown(
            f"""
            <div class='black-panel'>
                <div class='black-panel-title'>Executive Interpretation</div>
                <div class='black-panel-copy'><span class='status-dot'></span>The command center is showing {high_count} high risk records, {sla_at_risk} SLA at risk records, and ${exposure:,} in synthetic exposure. These are not automated decisions. They are review signals for prioritization, documentation validation, payer follow up, and safe escalation.</div>
                <div class='pill-row'>
                    <span class='pill'>High Risk {high_count}</span>
                    <span class='pill'>Moderate {moderate_count}</span>
                    <span class='pill'>Escalations {escalations}</span>
                    <span class='pill'>No PHI</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.bar_chart(risk_mix.set_index("Risk Level"))
    st.download_button("Download synthetic operations data", records.to_csv(index=False), file_name="synthetic_healthcare_operations_data.csv", mime="text/csv")

elif workspace == "Live Operations Board":
    section("Live Operations Board")
    st.markdown("<div class='callout'>This workspace turns the synthetic records into an operational huddle board. Use it to show what a revenue cycle or patient access leader might review first each morning.</div>", unsafe_allow_html=True)
    board = records.sort_values(["risk_score", "financial_exposure"], ascending=False).head(20)[["case_id", "owner_queue", "payer_group", "workflow_area", "service_line", "request_age_days", "queue_age_days", "risk_score", "financial_exposure", "recommended_action"]]
    st.dataframe(board, use_container_width=True, hide_index=True)
    a, b, c = st.columns(3)
    a.markdown(f"<div class='card'><div class='card-title'>First Action</div><div class='subtle'>Start with {board.iloc[0]['case_id']} because it has the highest combined workflow risk and synthetic exposure.</div></div>", unsafe_allow_html=True)
    b.markdown(f"<div class='card'><div class='card-title'>Owner Queue</div><div class='subtle'>{board.iloc[0]['owner_queue']} should validate status, documentation readiness, and next escalation step.</div></div>", unsafe_allow_html=True)
    c.markdown(f"<div class='card'><div class='card-title'>Huddle Question</div><div class='subtle'>Which high risk records can be moved today through documentation completion, payer follow up, or ownership clarification?</div></div>", unsafe_allow_html=True)
    st.session_state.command_notes = st.text_area("Daily command center notes", st.session_state.command_notes, height=160)

elif workspace == "Synthetic Data Lab":
    section("Synthetic Data Lab")
    st.markdown("<div class='callout'>This lab generates healthcare operations records that look realistic enough for workflow testing but contain no real patient identifiers, no real claim numbers, no real member IDs, and no protected health information.</div>", unsafe_allow_html=True)
    st.dataframe(records, use_container_width=True, hide_index=True)
    st.download_button("Download generated synthetic dataset", records.to_csv(index=False), file_name="synthetic_no_phi_operations_dataset.csv", mime="text/csv")
    with st.expander("Data Use Statement"):
        st.write("This dataset is synthetic and no PHI. It was generated for healthcare operations workflow analysis practice, portfolio demonstration, risk scoring, and responsible AI governance simulation. It must not be interpreted as real patient, payer, claim, authorization, or medical record data.")

elif workspace == "Prior Authorization Risk Queue":
    section("Prior Authorization Risk Queue")
    auth = records[records["workflow_area"].isin(["Prior Authorization", "Eligibility Verification", "Patient Access"])]
    c1, c2, c3 = st.columns(3)
    selected_payer = c1.multiselect("Payer group", sorted(auth["payer_group"].unique()), default=sorted(auth["payer_group"].unique()))
    selected_level = c2.multiselect("Risk level", ["Low", "Moderate", "High"], default=["Moderate", "High"])
    selected_status = c3.multiselect("Authorization status", sorted(auth["authorization_status"].unique()), default=sorted(auth["authorization_status"].unique()))
    view = auth[auth["payer_group"].isin(selected_payer) & auth["risk_level"].astype(str).isin(selected_level) & auth["authorization_status"].isin(selected_status)]
    st.dataframe(view.sort_values("risk_score", ascending=False), use_container_width=True, hide_index=True)
    if len(view) > 0:
        selected_case = st.selectbox("Select case for review", view["case_id"].tolist())
        row = view[view["case_id"] == selected_case].iloc[0]
        st.markdown(f"""
        <div class='callout'>
        Case selected: {selected_case}<br>
        Workflow area: {row['workflow_area']}<br>
        Payer group: {row['payer_group']}<br>
        Risk score: {row['risk_score']}<br>
        Synthetic exposure: ${int(row['financial_exposure']):,}<br>
        Recommended action: {row['recommended_action']}
        </div>
        """, unsafe_allow_html=True)
        if st.button("Save case review note"):
            st.session_state.saved_cases.append({"case_id": selected_case, "risk_score": int(row["risk_score"]), "recommended_action": row["recommended_action"]})
            st.success("Case review saved")
    st.dataframe(pd.DataFrame(st.session_state.saved_cases), use_container_width=True, hide_index=True)

elif workspace == "Payer Fairness Monitor":
    section("Payer Fairness Monitor")
    st.dataframe(fair_table, use_container_width=True, hide_index=True)
    st.markdown(f"<div class='metric-card'><div class='big'>{fairness_ratio}</div><div class='label'>Current Fairness Ratio</div><div class='metric-note'>Safety floor selected: {safety_floor / 100:.2f}</div></div>", unsafe_allow_html=True)
    if fairness_ratio < safety_floor / 100:
        st.error("Fairness review triggered because payer delay patterns are below the selected safety floor.")
    else:
        st.success("Fairness ratio is above the selected safety floor.")
    simulated_ratio = st.slider("Simulate fairness ratio", 0.50, 1.00, float(fairness_ratio), 0.01)
    if simulated_ratio < safety_floor / 100:
        if st.button("Log fairness alert"):
            alert = {"alert_type": "Fairness review", "current_ratio": round(simulated_ratio, 2), "safety_floor": safety_floor / 100, "action": "Pause automated use and validate payer group delay patterns"}
            st.session_state.alert_log.append(alert)
            st.success("Fairness alert logged")
    st.dataframe(pd.DataFrame(st.session_state.alert_log), use_container_width=True, hide_index=True)

elif workspace == "Explainability Studio":
    section("Explainability Studio")
    explanation = pd.DataFrame({
        "risk_driver": ["Authorization or request age", "Documentation instability", "Queue aging", "Eligibility issue", "Payer friction", "Staffing capacity", "Handoff count", "Days to visit", "Denial trend pressure"],
        "operational_meaning": ["Older requests are more likely to create delay pressure", "Lower documentation readiness increases rework risk", "Older queues indicate backlog pressure", "Mismatches and missing verification increase downstream risk", "Some payer groups require closer monitoring", "Lower capacity increases operational strain", "More handoffs can create ownership gaps", "Shorter time to visit increases urgency", "Rising denial patterns increase prevention pressure"],
        "governance_question": ["Has the case aged beyond the local threshold", "Is documentation complete enough for next step", "Who owns the backlog", "Has eligibility been verified before service", "Is delay uneven across payer groups", "Does staffing capacity support workload", "Is accountability clear", "Will delay affect access or revenue before visit", "Is prevention occurring upstream"],
    })
    st.dataframe(explanation, use_container_width=True, hide_index=True)
    st.bar_chart(records.groupby("workflow_area", observed=True)["risk_score"].mean())
    selected_case = st.selectbox("Select a case to explain", records["case_id"].head(150).tolist())
    row = records[records["case_id"] == selected_case].iloc[0]
    st.markdown(f"""
    <div class='card'>
        <div class='card-title'>Case Explanation</div>
        <div class='subtle'>This case has a risk score of {row['risk_score']} because the workflow includes request age of {row['request_age_days']} days, queue age of {row['queue_age_days']} days, documentation score of {row['documentation_score']}, staffing capacity of {row['staffing_capacity']}, {row['handoff_count']} handoffs, and {row['days_to_visit']} days to visit. The recommended action is: {row['recommended_action']}.</div>
    </div>
    """, unsafe_allow_html=True)

elif workspace == "Safe Export Pipeline":
    section("Safe Export Pipeline")
    left, right = st.columns(2)
    with left:
        st.markdown("<div class='card-title'>Synthetic Intake View</div>", unsafe_allow_html=True)
        st.dataframe(records[["case_id", "payer_group", "workflow_area", "created_date", "risk_score"]].head(12), use_container_width=True, hide_index=True)
    with right:
        st.markdown("<div class='card-title'>Safe Export View</div>", unsafe_allow_html=True)
        st.dataframe(safe_records[["case_id", "payer_group", "workflow_area", "created_date", "risk_score"]].head(12), use_container_width=True, hide_index=True)
    if st.button("Run safe export simulation"):
        progress = st.progress(0)
        for i in range(100):
            time.sleep(.003)
            progress.progress(i + 1)
        event = {"status": "Completed", "records_exported": len(safe_records), "data_type": "Synthetic no PHI", "export_rule": "Safe case IDs and synthetic date buckets"}
        st.session_state.pipeline_log.append(event)
        st.success("Safe export simulation completed")
    st.dataframe(pd.DataFrame(st.session_state.pipeline_log), use_container_width=True, hide_index=True)
    st.download_button("Download safe export", safe_records.to_csv(index=False), file_name="safe_synthetic_operations_export.csv", mime="text/csv")

elif workspace == "Governance Checklist":
    section("Governance Checklist")
    checklist = [
        "Uses synthetic no PHI records only",
        "Avoids names addresses phone numbers and real identifiers",
        "Requires human review before operational action",
        "Explains why a case is high risk",
        "Checks payer group fairness patterns",
        "Provides safe export logic",
        "Includes responsible use boundary",
        "Does not replace payer policy interpretation",
        "Does not replace clinical judgment",
        "Creates portfolio ready documentation",
    ]
    completed = []
    cols = st.columns(2)
    for i, item in enumerate(checklist):
        with cols[i % 2]:
            if st.checkbox(item):
                completed.append(item)
    score = len(completed)
    st.markdown(f"<div class='metric-card'><div class='big'>{score} of 10</div><div class='label'>Governance Readiness Score</div></div>", unsafe_allow_html=True)
    if score >= 8:
        st.success("Strong governance foundation")
    elif score >= 5:
        st.warning("Partial governance foundation")
    else:
        st.error("High governance risk")
    st.session_state.governance_notes = st.text_area("Governance notes", st.session_state.governance_notes, height=160)

elif workspace == "Portfolio Report Builder":
    section("Portfolio Report Builder")
    scenario = st.selectbox("Scenario reviewed", ["Baseline operations simulation", "Payer friction surge", "Documentation backlog", "Staffing capacity pressure", "Queue aging surge", "Prior authorization aging spike", "Denial prevention review"])
    governance_score = st.slider("Governance score to include", 0, 10, 8)
    pipeline_status = st.selectbox("Pipeline status", ["Not tested", "Simulated successfully", "Needs review"])
    report = make_report(records, fairness_ratio, scenario, governance_score, pipeline_status, operating_mode, service_focus)
    st.text_area("Portfolio ready report", report, height=620)
    st.download_button("Download portfolio report", report, file_name="synthetic_healthcare_operations_command_center_report.txt", mime="text/plain")

footer()
