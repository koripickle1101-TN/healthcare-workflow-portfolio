"""Patient Access & Eligibility Verification Analysis."""

import streamlit as st
import pandas as pd
import plotly.express as px
from components.styles import inject_global_css
from components.header import render_sidebar_header

st.set_page_config(page_title="Patient Access | Kori Pickle", page_icon="🏥", layout="wide")
inject_global_css()
render_sidebar_header()

st.markdown("""
<div class='page-header'>
    <div class='page-header-eyebrow'>Section 02 · Access Operations</div>
    <div class='page-header-title'>Patient Access & Eligibility</div>
    <div class='page-header-sub'>
        Insurance verification accuracy · Intake quality controls · Coverage validation gaps
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='orange-callout'>
    <strong>Core Problem:</strong> Incorrect or incomplete insurance data entered at registration
    travels forward undetected — and becomes a denial weeks later. The fix happens at the front door,
    not the billing office.
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📊 Eligibility Data", "⚠️ Failure Points", "✅ Verification Checklist"])

with tab1:
    st.markdown("### Eligibility-Related Denial Breakdown")
    data = {
        "Root Cause": [
            "Insurance inactive at DOS",
            "Wrong payer on file",
            "Coverage type mismatch",
            "Subscriber ID error",
            "Plan requires referral",
            "Coordination of benefits",
            "Other eligibility"
        ],
        "Denial Rate (%)": [28, 22, 18, 14, 9, 6, 3]
    }
    df = pd.DataFrame(data)
    fig = px.pie(
        df, names="Root Cause", values="Denial Rate (%)",
        color_discrete_sequence=["#FF8200","#CC6800","#FFB366","#111111",
                                  "#444444","#888888","#DDDDDD"],
        title="Eligibility Denial Breakdown by Root Cause"
    )
    fig.update_layout(font_family="Inter", title_font_size=15)
    st.plotly_chart(fig, use_container_width=True)

    c1, c2, c3, c4 = st.columns(4)
    for col, val, label in zip(
        [c1, c2, c3, c4],
        ["31%", "72hrs", "$42 avg", "68%"],
        ["Of All Denials", "Avg Discovery Delay", "Cost to Rework", "Preventable at Intake"]
    ):
        col.metric(label, val)

with tab2:
    st.markdown("### Where Patient Access Breaks Down")
    failures = [
        ("Scheduling", "Insurance info collected verbally without real-time verification. Errors enter the system here."),
        ("Pre-Registration", "Demographics and coverage not confirmed against payer database before appointment."),
        ("Day-of-Service Check-In", "No second eligibility check. Changed coverage or lapsed policies go undetected."),
        ("Authorization Alignment", "Services requiring PA not flagged at scheduling. Auth obtained too late or not at all."),
        ("Referral Tracking", "Referral requirement missed because payer plan rules not embedded in workflow."),
        ("Coordination of Benefits", "Primary vs. secondary payer order not confirmed. Claims submitted to wrong payer."),
    ]
    for i, (title, desc) in enumerate(failures, 1):
        st.markdown(f"""
        <div class='process-step'>
            <div class='step-num'>{i}</div>
            <div class='step-body'>
                <div class='step-title'>{title}</div>
                <div class='step-desc'>{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("### Eligibility Verification Checklist")
    checks = [
        ("Verify eligibility at scheduling AND day of service",
         "One check is not enough. Coverage can lapse between scheduling and the appointment date."),
        ("Confirm subscriber ID and group number against payer portal",
         "Verbal collection creates transcription errors. Always confirm against source."),
        ("Identify plan type and referral requirements",
         "HMO, EPO, and managed Medicaid plans have referral rules that vary by payer."),
        ("Flag coordination of benefits at registration",
         "Ask about secondary insurance every visit. COB order changes and affects adjudication."),
        ("Document real-time eligibility response in the account",
         "If you verified it, document it. Undocumented verification creates dispute problems."),
        ("Alert scheduling if authorization is required before service",
         "PA requirements must trigger immediately at scheduling — not after the appointment."),
    ]
    for title, desc in checks:
        st.markdown(f"""
        <div class='info-card'>
            <div class='info-card-title'>✅ {title}</div>
            <div class='info-card-body'>{desc}</div>
        </div>
        ""
