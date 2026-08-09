"""Revenue Cycle Management — upstream failure analysis."""

import streamlit as st
import pandas as pd
import plotly.express as px
from components.styles import inject_global_css
from components.header import render_sidebar_header

st.set_page_config(page_title="Revenue Cycle | Kori Pickle", page_icon="💰", layout="wide")
inject_global_css()
render_sidebar_header()

st.markdown("""
<div class='page-header'>
    <div class='page-header-eyebrow'>Section 01 · RCM Analysis</div>
    <div class='page-header-title'>Revenue Cycle Management</div>
    <div class='page-header-sub'>
        Upstream failure mapping · Clean claim improvement · Front-end validation strategy
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='orange-callout'>
    <strong>Core Argument:</strong> Most revenue cycle failures do not start in billing.
    They start upstream — in intake, eligibility, authorization, and documentation.
    Finding those upstream breaks before submission is the job.
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📊 Denial Breakdown", "🗺️ Upstream Failures", "✅ Prevention Strategy"])

with tab1:
    st.markdown("### Where Denials Come From")
    data = {
        "Denial Category": [
            "Eligibility / Coverage", "Prior Authorization",
            "Missing Documentation", "Coding Errors",
            "Duplicate Claim", "Medical Necessity", "Other"
        ],
        "Percentage": [31, 24, 18, 13, 7, 5, 2],
        "Upstream": ["Yes","Yes","Yes","Partial","No","Partial","No"]
    }
    df = pd.DataFrame(data)
    fig = px.bar(
        df, x="Denial Category", y="Percentage",
        color="Upstream",
        color_discrete_map={"Yes": "#FF8200", "Partial": "#FFB366", "No": "#CCCCCC"},
        title="Denial Root Causes — Upstream vs. Downstream",
        text="Percentage"
    )
    fig.update_traces(texttemplate="%{text}%", textposition="outside")
    fig.update_layout(
        plot_bgcolor="white", paper_bgcolor="white",
        font_family="Inter", title_font_size=15,
        xaxis_title="", yaxis_title="% of Denials",
        legend_title="Upstream Origin"
    )
    st.plotly_chart(fig, use_container_width=True)

    c1, c2, c3, c4 = st.columns(4)
    for col, val, label in zip(
        [c1, c2, c3, c4],
        ["73%", "31%", "$25–$118", "1–3 Days"],
        ["Preventable Upstream", "Eligibility-Related", "Cost Per Denial", "Avg Rework Time"]
    ):
        col.metric(label, val)

with tab2:
    st.markdown("### Revenue Cycle Failure Points")
    steps = [
        ("Patient Scheduling", "Missing insurance info, incorrect demographics captured at first contact."),
        ("Eligibility Verification", "Coverage not verified in real time. Inactive or wrong plan moves forward."),
        ("Prior Authorization", "Auth not obtained or expired before service. Retroactive requests often denied."),
        ("Clinical Documentation", "Incomplete notes create medical necessity gaps that payers flag."),
        ("Charge Capture", "Services rendered but not captured. Revenue lost before billing starts."),
        ("Claim Submission", "Coding errors, missing modifiers, wrong payer ID delay adjudication."),
        ("Denial Management", "Reactive follow-up instead of root cause prevention. Cycle repeats."),
    ]
    for i, (title, desc) in enumerate(steps, 1):
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
    st.markdown("### Denial Prevention Checkpoints")
    strategies = [
        ("Real-Time Eligibility Verification", "Verify coverage at scheduling AND day of service. Flag mismatches before the patient arrives."),
        ("Authorization Tracking Board", "Track PA status, expiration dates, and payer timelines. Never let an auth age out unnoticed."),
        ("Documentation Completeness Check", "Pre-bill review for medical necessity language, diagnosis specificity, and payer-required fields."),
        ("Clean Claim Rate Monitoring", "Track first-pass acceptance rate by payer, provider, and service type. Identify patterns, not just incidents."),
        ("Feedback Loop to Front End", "Denials should travel back upstream. If eligibility causes 31 percent of denials, registration needs to know."),
    ]
    for title, desc in strategies:
        st.markdown(f"""
        <div class='info-card'>
            <div class='info-card-title'>✅ {title}</div>
            <div class='info-card-body'>{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div class='footer'>Kori Pickle · Healthcare Operations Portfolio · All data synthetic · No PHI</div>
""", unsafe_allow_html=True)
