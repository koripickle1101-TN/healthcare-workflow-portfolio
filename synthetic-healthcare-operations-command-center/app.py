import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Synthetic Healthcare Operations Command Center",
    page_icon="🟧",
    layout="wide",
    initial_sidebar_state="expanded",
)

ORANGE = "#FF8200"
BLACK = "#000000"
WHITE = "#FFFFFF"
WARM = "#E8E3DC"
SOFT = "#F7F4EF"

LINKEDIN_URL = "https://www.linkedin.com/in/kori-p-865jct"
GITHUB_URL = "https://github.com/koripickle1101-TN"
REPO_URL = "https://github.com/koripickle1101-TN/healthcare-workflow-portfolio"

st.markdown(
    f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:wght@700;800;900&family=Allura&display=swap');

html, body, [class*='css'] {{ font-family: Inter, sans-serif; color: {BLACK}; }}
.stApp {{ background: radial-gradient(circle at 92% 4%, rgba(255,130,0,.10), transparent 28%), linear-gradient(180deg, #FFFFFF 0%, #FFFFFF 72%, #FBF8F3 100%); }}
.block-container {{ max-width: 1280px; padding-top: 1.1rem; padding-bottom: 3rem; }}
section[data-testid='stSidebar'] {{ background: #FFFFFF; border-right: 1px solid {WARM}; }}

.brand-card {{ background: #FFFFFF; border: 1px solid {WARM}; border-radius: 30px; padding: 28px 24px; margin-bottom: 28px; box-shadow: 0 24px 64px rgba(0,0,0,.055); overflow: hidden; }}
.brand-signature {{ font-family: Allura, cursive; font-size: clamp(56px, 10vw, 96px); line-height: .88; color: #111111; text-align: center; margin-bottom: 22px; transform: rotate(-1deg); }}
.brand-line {{ height: 2px; width: 84%; margin: 14px auto 18px auto; background: linear-gradient(90deg, transparent, {ORANGE}, transparent); }}
.brand-kicker {{ text-align: center; font-size: clamp(14px, 3vw, 22px); letter-spacing: clamp(4px, 1.4vw, 9px); text-transform: uppercase; font-weight: 800; color: #111111; }}
.brand-intel {{ text-align: center; font-size: clamp(22px, 5vw, 38px); letter-spacing: clamp(5px, 1.6vw, 12px); text-transform: uppercase; color: {ORANGE}; font-weight: 900; line-height: 1.2; }}

.hero {{ border: 1px solid {WARM}; border-radius: 34px; padding: clamp(30px, 5vw, 58px); background: linear-gradient(135deg, #FFFFFF 0%, #FFFFFF 65%, rgba(255,130,0,.08) 100%); box-shadow: 0 28px 78px rgba(0,0,0,.07); margin-bottom: 30px; }}
.eyebrow {{ font-size: 12px; letter-spacing: 3px; text-transform: uppercase; font-weight: 900; display: inline-block; padding-bottom: 8px; border-bottom: 2px solid {ORANGE}; margin-bottom: 24px; color: #333333; }}
.title {{ font-family: Playfair Display, serif; font-size: clamp(40px, 6vw, 82px); line-height: .96; letter-spacing: -2px; margin: 0 0 22px 0; color: #000000; }}
.orange {{ color: {ORANGE}; }}
.copy {{ max-width: 940px; font-size: 18px; line-height: 1.72; color: #242424; }}
.section-title {{ font-family: Playfair Display, serif; font-size: clamp(34px, 5vw, 54px); line-height: 1; letter-spacing: -1px; margin: 42px 0 18px 0; color: #000000; }}

.metric-card {{ border: 1px solid {WARM}; border-left: 5px solid {ORANGE}; border-radius: 22px; background: {SOFT}; padding: 22px; min-height: 130px; box-shadow: 0 14px 34px rgba(0,0,0,.035); }}
.big {{ font-family: Playfair Display, serif; font-size: clamp(34px, 5vw, 50px); font-weight: 900; line-height: .95; color: #111111; }}
.label {{ font-size: 12px; font-weight: 900; letter-spacing: 1.4px; text-transform: uppercase; margin-top: 12px; color: #555555; }}
.card {{ border: 1px solid {WARM}; border-top: 5px solid {ORANGE}; border-radius: 26px; padding: 24px; background: #FFFFFF; box-shadow: 0 18px 48px rgba(0,0,0,.05); height: 100%; }}
.card-title {{ font-family: Playfair Display, serif; font-size: 29px; line-height: 1.08; margin-bottom: 12px; color: #000000; }}
.subtle {{ color: #353535; line-height: 1.68; font-size: 16px; }}
.callout {{ border: 1px solid {WARM}; border-left: 6px solid {ORANGE}; border-radius: 24px; padding: 22px 26px; background: #FFFFFF; box-shadow: 0 18px 44px rgba(0,0,0,.045); margin: 18px 0; color: #111111; }}

.node-grid {{ display: flex; flex-wrap: wrap; gap: 16px; align-items: center; margin-top: 30px; }}
.node {{ width: 64px; height: 64px; border-radius: 999px; border: 2px solid {ORANGE}; display: inline-flex; align-items: center; justify-content: center; color: {ORANGE}; background: #FFFFFF; font-weight: 900; box-shadow: 0 0 0 10px rgba(255,130,0,.07), 0 0 30px rgba(255,130,0,.18); flex: 0 0 auto; }}
.pill-row {{ display: flex; flex-wrap: wrap; gap: 10px; align-items: center; margin-top: 14px; }}
.pill {{ display: inline-flex; align-items: center; justify-content: center; border: 1px solid {ORANGE}; background: rgba(255,130,0,.08); border-radius: 999px; padding: 8px 14px; font-size: 12px; font-weight: 900; letter-spacing: .55px; text-transform: uppercase; color: #111111; white-space: nowrap; }}

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
    .footer-link {{ min-width: 112px; padding: 10px 14px; font-size: 12px; }}
}}
</style>
""",
    unsafe_allow_html=True,
)

for key in ["saved_cases", "alert_log", "pipeline_log", "governance_notes"]:
    if key not in st.session_state:
        st.session_state[key] = [] if key != "governance_notes" else ""


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


def create_synthetic_operations_data(volume, payer_pressure, documentation_pressure, staffing_pressure, queue_pressure):
    rng = np.random.default_rng(1101)
    start_date = datetime.today() - timedelta(days=21)
    records = pd.DataFrame(
        {
            "case_id": [f"AUTH {i:05d}" for i in range(1, volume + 1)],
            "payer_group": rng.choice(["Commercial", "Medicare", "Medicaid", "Marketplace", "Self Pay"], volume, p=[.38, .25, .20, .11, .06]),
            "workflow_area": rng.choice(["Eligibility Verification", "Prior Authorization", "Patient Access", "Documentation Review", "Denial Prevention"], volume, p=[.20, .30, .20, .18, .12]),
            "service_line": rng.choice(["Orthopedics", "Cardiology", "Rehabilitation", "Imaging", "Primary Care", "Specialty Pharmacy"], volume),
            "request_age_days": rng.integers(0, 18, volume),
            "queue_age_days": rng.integers(0, 20, volume),
            "documentation_score": rng.integers(52, 100, volume),
            "eligibility_status": rng.choice(["Verified", "Needs Recheck", "Mismatch", "Missing"], volume, p=[.58, .20, .15, .07]),
            "authorization_status": rng.choice(["Not Started", "Pending", "Submitted", "Approved", "Escalated"], volume, p=[.15, .32, .25, .20, .08]),
            "staffing_capacity": rng.integers(58, 101, volume),
            "handoff_count": rng.integers(1, 7, volume),
        }
    )
    records["created_date"] = [(start_date + timedelta(days=int(x))).strftime("%Y-%m-%d") for x in rng.integers(0, 21, volume)]
    payer_weight = records["payer_group"].map({"Commercial": 3, "Medicare": 5, "Medicaid": 8 + payer_pressure, "Marketplace": 7 + payer_pressure, "Self Pay": 9 + payer_pressure})
    eligibility_weight = records["eligibility_status"].map({"Verified": 0, "Needs Recheck": 10, "Mismatch": 18, "Missing": 22})
    status_weight = records["authorization_status"].map({"Approved": 0, "Submitted": 8, "Pending": 14, "Not Started": 19, "Escalated": 24})
    records["risk_score"] = (
        100
        - records["documentation_score"]
        + records["request_age_days"] * 3
        + records["queue_age_days"] * 2
        + records["handoff_count"] * 3
        + (100 - records["staffing_capacity"]) * 0.25
        + payer_weight
        + eligibility_weight
        + status_weight
        + documentation_pressure
        + staffing_pressure
        + queue_pressure
    ).round(0).clip(0, 100).astype(int)
    records["risk_level"] = pd.cut(records["risk_score"], bins=[-1, 39, 69, 100], labels=["Low", "Moderate", "High"])
    records["delay_flag"] = np.where(records["risk_score"] >= 65, 1, 0)
    records["recommended_action"] = "Continue standard monitoring"
    records.loc[records["risk_score"] >= 50, "recommended_action"] = "Review documentation and queue status"
    records.loc[records["risk_score"] >= 70, "recommended_action"] = "Escalate for human review"
    records.loc[records["risk_score"] >= 85, "recommended_action"] = "Immediate workflow intervention required"
    return records


def fairness_summary(records):
    table = records.groupby("payer_group", observed=True).agg(
        records=("case_id", "count"),
        delay_rate=("delay_flag", "mean"),
        average_risk=("risk_score", "mean"),
        average_queue_age=("queue_age_days", "mean"),
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


def make_report(records, fairness_ratio, scenario, governance_score, pipeline_status):
    high = int((records["risk_level"] == "High").sum())
    moderate = int((records["risk_level"] == "Moderate").sum())
    avg_risk = round(float(records["risk_score"].mean()), 1)
    top_area = records.groupby("workflow_area", observed=True)["risk_score"].mean().sort_values(ascending=False).index[0]
    return f"""HEALTHCARE OPERATIONS INTELLIGENCE
Created by Kori Pickle

Synthetic Healthcare Operations Command Center

Executive Summary
This no PHI healthcare operations tool uses synthetic records to simulate patient access, eligibility verification, prior authorization, documentation review, and denial prevention workflow risk. It is designed to demonstrate real operational logic without using real patient data.

Scenario Reviewed
{scenario}

Core Metrics
Synthetic records reviewed: {len(records)}
Average risk score: {avg_risk}
High risk records: {high}
Moderate risk records: {moderate}
Fairness ratio: {fairness_ratio}
Primary pressure area: {top_area}
Governance readiness score: {governance_score} of 10
Pipeline status: {pipeline_status}
Protected data used: No

Operational Interpretation
The tool identifies where synthetic workflow records show elevated risk because of delayed authorization activity, queue aging, documentation instability, eligibility issues, payer friction, handoff burden, or staffing pressure. High risk records are not automatic decisions. They are review signals that require human validation.

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
    st.markdown("<div class='sidebar-caption'>Synthetic no PHI operations data, workflow risk scoring, prior authorization, patient access, and denial prevention governance.</div>", unsafe_allow_html=True)
    workspace = st.radio(
        "Choose a workspace",
        [
            "Executive Command Center",
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
    volume = st.slider("Synthetic record volume", 100, 900, 260, 20)
    payer_pressure = st.slider("Payer friction pressure", 0, 25, 8, 1)
    documentation_pressure = st.slider("Documentation instability", 0, 25, 7, 1)
    staffing_pressure = st.slider("Staffing pressure", 0, 25, 8, 1)
    queue_pressure = st.slider("Queue aging pressure", 0, 25, 8, 1)
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

records = create_synthetic_operations_data(volume, payer_pressure, documentation_pressure, staffing_pressure, queue_pressure)
fair_table, fairness_ratio = fairness_summary(records)
safe_records = safe_export(records)
high_count = int((records["risk_level"] == "High").sum())
moderate_count = int((records["risk_level"] == "Moderate").sum())
average_risk = round(float(records["risk_score"].mean()), 1)
escalations = int((records["recommended_action"] == "Immediate workflow intervention required").sum())

brand_header()

if workspace == "Executive Command Center":
    st.markdown(
        """
        <div class='hero'>
            <div class='eyebrow'>Synthetic Healthcare Operations Command Center</div>
            <div class='title'>A real workflow tool powered by <span class='orange'>synthetic no PHI data</span></div>
            <div class='copy'>This interactive command center simulates patient access, eligibility verification, prior authorization, documentation review, and denial prevention workflows. It calculates operational risk, highlights high risk cases, monitors fairness patterns, and exports portfolio ready reports without using real patient data.</div>
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
    c1.markdown(f"<div class='metric-card'><div class='big'>{len(records)}</div><div class='label'>Synthetic Records</div></div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='metric-card'><div class='big'>{high_count}</div><div class='label'>High Risk Cases</div></div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='metric-card'><div class='big'>{average_risk}</div><div class='label'>Average Risk Score</div></div>", unsafe_allow_html=True)
    c4.markdown(f"<div class='metric-card'><div class='big'>{fairness_ratio}</div><div class='label'>Fairness Ratio</div></div>", unsafe_allow_html=True)
    section("Operational Snapshot")
    left, right = st.columns([1.25, .75])
    with left:
        st.dataframe(records.head(35), use_container_width=True, hide_index=True)
    with right:
        st.markdown(
            f"""
            <div class='card'>
                <div class='card-title'>Executive Interpretation</div>
                <div class='subtle'>The command center is showing {high_count} high risk synthetic records and {escalations} immediate intervention signals. These are not automated decisions. They are workflow review signals for operational prioritization, documentation validation, payer follow up, and safe escalation.</div>
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
    st.download_button("Download synthetic operations data", records.to_csv(index=False), file_name="synthetic_healthcare_operations_data.csv", mime="text/csv")

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
    st.markdown(f"<div class='metric-card'><div class='big'>{fairness_ratio}</div><div class='label'>Current Fairness Ratio</div></div>", unsafe_allow_html=True)
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
        "risk_driver": ["Authorization or request age", "Documentation instability", "Queue aging", "Eligibility issue", "Payer friction", "Staffing capacity", "Handoff count"],
        "operational_meaning": ["Older requests are more likely to create delay pressure", "Lower documentation readiness increases rework risk", "Older queues indicate backlog pressure", "Mismatches and missing verification increase downstream risk", "Some payer groups require closer monitoring", "Lower capacity increases operational strain", "More handoffs can create ownership gaps"],
        "governance_question": ["Has the case aged beyond the local threshold", "Is documentation complete enough for next step", "Who owns the backlog", "Has eligibility been verified before service", "Is delay uneven across payer groups", "Does staffing capacity support workload", "Is accountability clear"],
    })
    st.dataframe(explanation, use_container_width=True, hide_index=True)
    st.bar_chart(records.groupby("workflow_area", observed=True)["risk_score"].mean())
    selected_case = st.selectbox("Select a case to explain", records["case_id"].head(100).tolist())
    row = records[records["case_id"] == selected_case].iloc[0]
    st.markdown(f"""
    <div class='card'>
        <div class='card-title'>Case Explanation</div>
        <div class='subtle'>This case has a risk score of {row['risk_score']} because the workflow includes request age of {row['request_age_days']} days, queue age of {row['queue_age_days']} days, documentation score of {row['documentation_score']}, staffing capacity of {row['staffing_capacity']}, and {row['handoff_count']} handoffs. The recommended action is: {row['recommended_action']}.</div>
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
    scenario = st.selectbox("Scenario reviewed", ["Baseline operations simulation", "Payer friction surge", "Documentation backlog", "Staffing capacity pressure", "Queue aging surge"])
    governance_score = st.slider("Governance score to include", 0, 10, 8)
    pipeline_status = st.selectbox("Pipeline status", ["Not tested", "Simulated successfully", "Needs review"])
    report = make_report(records, fairness_ratio, scenario, governance_score, pipeline_status)
    st.text_area("Portfolio ready report", report, height=620)
    st.download_button("Download portfolio report", report, file_name="synthetic_healthcare_operations_command_center_report.txt", mime="text/plain")

footer()
