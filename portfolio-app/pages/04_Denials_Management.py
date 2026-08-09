"""Denials Management — root cause analysis and prevention."""

import streamlit as st
import pandas as pd
import plotly.express as px
from components.styles import inject_global_css
from components.header import render_sidebar_header

st.set_page_config(page_title="Denials Management | Kori Pickle", page_icon="🚫", layout="wide")
inject_global_css()
render_sidebar_header()

st.markdown("""
<div class='page-header'>
    <div class='page-header-eyebrow'>Section 04 · Denial Prevention</div>
    <div class='page-header-title'>Denials Management</div>
    <div class='page-header-sub'>
        Root cause pattern analysis · Repeat denial identification · Prevention checkpoints
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='orange-callout'>
    <strong>Core Argument:</strong> Denials are not random. They are patterns.
    When the same denial type repeats across multiple payers or providers,
    it is a workflow problem — not a billing problem. Fix the workflow, not just the claim.
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📊 Denial Patterns", "🔁 Repeat Denials", "🛡️ Prevention Plan"])

with tab1:
    st.markdown("### Denial Volume by Category and Payer (Synthetic)")
    data = {
        "Payer": ["Aetna","Aetna","BCBS","BCBS","Humana","Humana",
                  "Medicaid","Medicaid","UHC","UHC"],
        "Denial Type": ["Eligibility","Prior Auth","Eligibility","Documentation",
                        "Prior Auth","Coding","Eligibility","Prior Auth",
                        "Documentation","Coding"],
        "Volume": [42, 31, 38, 25, 55, 18, 67, 48, 29, 22],
        "Avg Days to Resolve": [8, 21, 6, 14, 25, 10, 30, 28, 12, 9]
    }
    df = pd.DataFrame(data)
    fig = px.bar(
        df, x="Payer", y="Volume", color="Denial Type",
        barmode="group",
        color_discrete_sequence=["#FF8200","#CC6800","#111111","#888888","#FFB366"],
        title="Denial Volume by Payer and Type"
    )
    fig.update_layout(
        plot_bgcolor="white", paper_bgcolor="white",
        font_family="Inter", xaxis_title="", yaxis_title="Denial Count"
    )
    st.plotly_chart(fig, use_container_width=True)

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Denials (Sample)", "375")
    c2.metric("Medicaid — Highest Volume", "115 denials")
    c3.metric("Avg Resolution Time", "16.3 days")
    c4.metric("Prior Auth — Longest Resolve", "24.7 days avg")

with tab2:
    st.markdown("### Repeat Denial Pattern Tracker")
    repeat_data = {
        "Denial Type": ["Prior Auth — Medicaid", "Eligibility — Humana",
                        "Documentation — UHC", "Prior Auth — Humana",
                        "Eligibility — Medicaid", "Coding — Aetna"],
        "Occurrences (90 Days)": [48, 38, 29, 27, 22, 18],
        "Risk Level": ["Critical","High","High","High","Medium","Low"],
        "Root Cause": [
            "PA not initiated at scheduling",
            "Coverage lapsed, not reverified",
            "Missing medical necessity language",
            "Auth expired before service date",
            "Inactive insurance on file",
            "Modifier missing on claim"
        ]
    }
    df2 = pd.DataFrame(repeat_data)
    fig2 = px.bar(
        df2, x="Occurrences (90 Days)", y="Denial Type",
        orientation="h", color="Risk Level",
        color_discrete_map={
            "Critical": "#CC0000", "High": "#FF8200",
            "Medium": "#FFB366", "Low": "#AAAAAA"
        },
        title="Top Repeat Denial Patterns — Last 90 Days"
    )
    fig2.update_layout(
        plot_bgcolor="white", paper_bgcolor="white",
        font_family="Inter", yaxis_title="", xaxis_title="Occurrences"
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### Root Cause Detail")
    for _, row in df2.iterrows():
        st.markdown(f"""
        <div class='info-card'>
            <div class='info-card-title'>⚠️ {row['Denial Type']} — {row['Occurrences (90 Days)']} occurrences</div>
            <div class='info-card-body'><b>Root Cause:</b> {row['Root Cause']}</div>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("### Denial Prevention Checkpoints")
    prevention = [
        ("Embed PA Rules at Scheduling",
         "Prior auth requirements must be identified and triggered the moment the appointment is scheduled — not after."),
        ("Real-Time Eligibility at Two Touch Points",
         "Verify at scheduling and again at check-in. Coverage changes between appointment creation and service date."),
        ("Documentation Review Before Submission",
         "Pre-bill review for medical necessity language catches documentation gaps before the claim reaches the payer."),
        ("Denial Feedback Loop to Registration",
         "Every denial root cause must travel back to the originating step. Registration needs to see eligibility denial data."),
        ("Repeat Denial Escalation Protocol",
         "Any denial type appearing more than 10 times in 30 days should trigger a workflow review — not just a rebill."),
        ("Payer-Specific Rule Maintenance",
         "Payer rules change. Auth requirements, covered codes, and documentation standards must be updated in workflow tools quarterly."),
    ]
    for title, desc in prevention:
        st.markdown(f"""
        <div class='info-card'>
            <div class='info-card-title'>🛡️ {title}</div>
            <div class='info-card-body'>{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div class='footer'>Kori Pickle · Healthcare Operations Portfolio · All data synthetic · No PHI</div>
""", unsafe_allow_html=True)
