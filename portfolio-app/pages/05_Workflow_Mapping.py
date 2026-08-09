"""Workflow Mapping — end-to-end revenue cycle process integrity."""

import streamlit as st
import plotly.graph_objects as go
from components.styles import inject_global_css
from components.header import render_sidebar_header

st.set_page_config(page_title="Workflow Mapping | Kori Pickle", page_icon="🗺️", layout="wide")
inject_global_css()
render_sidebar_header()

st.markdown("""
<div class='page-header'>
    <div class='page-header-eyebrow'>Section 05 · Process Integrity</div>
    <div class='page-header-title'>Workflow Mapping</div>
    <div class='page-header-sub'>
        End-to-end revenue cycle visualization · Failure point identification · Process integrity
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='orange-callout'>
    <strong>Core Argument:</strong> You cannot fix what you cannot see.
    Mapping the full revenue cycle workflow — from scheduling to payment —
    exposes where handoffs fail, where errors move forward undetected,
    and where validation checkpoints are missing.
</div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🗺️ Workflow Map", "⚠️ Failure Point Analysis"])

with tab1:
    st.markdown("### End-to-End Revenue Cycle Workflow")

    steps = [
        "Scheduling", "Pre-Registration", "Eligibility Verification",
        "Prior Authorization", "Day-of-Service Check-In",
        "Clinical Documentation", "Charge Capture", "Coding Review",
        "Claim Submission", "Adjudication", "Payment Posting", "Denial Management"
    ]
    risk = [3, 4, 5, 5, 3, 4, 3, 3, 2, 1, 1, 5]
    upstream = ["Yes","Yes","Yes","Yes","Yes","Yes","Partial","Partial","No","No","No","No"]
    colors = ["#FF8200" if r >= 4 else "#FFB366" if r == 3 else "#CCCCCC" for r in risk]

    fig = go.Figure(go.Bar(
        x=steps, y=risk,
        marker_color=colors,
        text=[f"Risk: {r}/5" for r in risk],
        textposition="outside",
        hovertemplate="<b>%{x}</b><br>Risk Score: %{y}/5<extra></extra>"
    ))
    fig.update_layout(
        title="Revenue Cycle Step Risk Score (5 = Highest Failure Risk)",
        plot_bgcolor="white", paper_bgcolor="white",
        font_family="Inter", xaxis_title="", yaxis_title="Risk Score",
        yaxis_range=[0, 6],
        xaxis_tickangle=-30
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Workflow Steps Detail")
    details = [
        ("Scheduling", 3, "Upstream", "PA requirements and insurance collection begin here. Errors at this step compound forward."),
        ("Pre-Registration", 4, "Upstream", "Demographics, insurance, and referral data captured. High error rate when done manually."),
        ("Eligibility Verification", 5, "Upstream", "Highest failure risk. Coverage must be verified in real time — not assumed from prior visits."),
        ("Prior Authorization", 5, "Upstream", "Second highest risk. Late initiation and poor tracking cause the majority of PA denials."),
        ("Day-of-Service Check-In", 3, "Upstream", "Last chance to catch eligibility or auth issues before service is rendered."),
        ("Clinical Documentation", 4, "Upstream", "Incomplete notes create medical necessity gaps that payers use to deny claims."),
        ("Charge Capture", 3, "Partial", "Missed charges are lost revenue. CDM alignment and charge reconciliation reduce risk."),
        ("Coding Review", 3, "Partial", "Coding errors and missing modifiers create downstream denials that require rework."),
        ("Claim Submission", 2, "Downstream", "If upstream steps are clean, submission risk is low. Most errors here trace back upstream."),
        ("Adjudication", 1, "Downstream", "Payer-controlled. Denial rates reflect upstream workflow quality."),
        ("Payment Posting", 1, "Downstream", "Posting errors affect financial reporting but rarely originate in clinical workflow."),
        ("Denial Management", 5, "Reactive", "High effort, low leverage. Prevention upstream eliminates most work that lands here."),
    ]

    for step, risk_score, origin, desc in details:
        color = "#FF8200" if risk_score >= 4 else "#FFB366" if risk_score == 3 else "#AAAAAA"
        st.markdown(f"""
        <div class='info-card' style='border-left:4px solid {color};'>
            <div class='info-card-title'>{step}
                <span style='float:right;font-size:0.7rem;color:{color};font-weight:700;'>
                    Risk {risk_score}/5 · {origin}
                </span>
            </div>
            <div class='info-card-body'>{desc}</div>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("### Top Failure Points and Fixes")
    failures = [
        ("Eligibility Not Verified in Real Time",
         "Checking eligibility once at scheduling is not enough. Coverage changes. Run verification at scheduling AND check-in.",
         "Critical"),
        ("PA Not Initiated at Scheduling",
         "Authorization requests submitted after scheduling confirmation waste days. Embed payer rules in scheduling workflow.",
         "Critical"),
        ("Documentation Gaps Not Caught Pre-Bill",
         "Missing medical necessity language passes through coding unchecked. Add a pre-bill documentation review step.",
         "High"),
        ("Denial Root Cause Not Sent Upstream",
         "Billing resolves the denial but registration never hears about it. Build a structured feedback loop.",
         "High"),
        ("Charge Capture Reconciliation Gaps",
         "Services rendered but not charged represent silent revenue loss. Daily charge reconciliation closes the gap.",
         "Medium"),
        ("No Repeat Denial Escalation Protocol",
         "The same denial pattern repeats 20 times before anyone notices. Set a threshold and trigger a workflow review.",
         "High"),
    ]
    for title, fix, severity in failures:
        color = "#CC0000" if severity == "Critical" else "#FF8200" if severity == "High" else "#888888"
        st.markdown(f"""
        <div class='info-card' style='border-left:4px solid {color};'>
            <div class='info-card-title' style='color:{color};'>
                ⚠️ {title} — <span style='font-size:0.75rem;'>{severity}</span>
            </div>
            <div class='info-card-body'>{fix}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div class='footer'>Kori Pickle · Healthcare Operations Portfolio · All data synthetic · No PHI</div>
""", unsafe_allow_html=True)
