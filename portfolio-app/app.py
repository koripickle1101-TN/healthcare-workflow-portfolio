"""
Healthcare Workflow Intelligence Engine
Kori Pickle — Portfolio Home
"""

import streamlit as st
from components.styles import inject_global_css
from components.header import render_sidebar_header

st.set_page_config(
    page_title="Kori Pickle | Healthcare Operations Portfolio",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_global_css()
render_sidebar_header()

st.markdown("""
<div class='hero-banner'>
    <div class='hero-eyebrow'>Healthcare Operations Intelligence Engine</div>
    <div class='hero-name'>Kori <span>Pickle</span></div>
    <div class='hero-subtitle'>
        Revenue Cycle Management · Prior Authorization · Denial Prevention ·
        Patient Access · Workflow Integrity · Responsible AI in Healthcare
    </div>
    <div class='hero-tags'>
        <span class='hero-tag'>RCM</span>
        <span class='hero-tag'>Prior Auth</span>
        <span class='hero-tag'>Denial Prevention</span>
        <span class='hero-tag'>Patient Access</span>
        <span class='hero-tag'>Workflow Analysis</span>
        <span class='hero-tag'>Remote Ready</span>
        <span class='hero-tag'>Tennessee</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='signature-question'>
    <span class='sq-label'>Portfolio Signature Question</span>
    <span class='sq-text'>
        "Where does the workflow break — and how do we stop it before it becomes a denial?"
    </span>
</div>
""", unsafe_allow_html=True)

st.markdown("## About This Portfolio")
st.markdown("""
<div class='body-text'>
This portfolio demonstrates practical healthcare operations expertise across revenue cycle
management, prior authorization, patient access, denial prevention, and workflow integrity.
Every section contains real analysis, synthetic data tools, and documented thinking —
not placeholder content.
<br/><br/>
<b>The core argument:</b> Most revenue cycle failures do not start in billing.
They start upstream — in intake, eligibility, authorization, and documentation.
This portfolio is built around finding those upstream breaks before they cost the organization money.
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("## Portfolio Sections")

cols = st.columns(3)
sections = [
    ("💰", "Revenue Cycle Management", "RCM ANALYSIS",
     "Upstream failure mapping, clean claim rate improvement, and front-end validation strategy."),
    ("🏥", "Patient Access & Eligibility", "ACCESS OPERATIONS",
     "Insurance verification accuracy, eligibility workflow gaps, and intake quality controls."),
    ("📋", "Prior Authorization", "AUTH OPERATIONS",
     "Authorization aging, payer friction patterns, and PA workflow risk scoring."),
    ("🚫", "Denials Management", "DENIAL PREVENTION",
     "Root cause pattern analysis, repeat denial identification, and prevention checkpoints."),
    ("🗺️", "Workflow Mapping", "PROCESS INTEGRITY",
     "End-to-end revenue cycle workflow visualization and failure point identification."),
    ("🤖", "AI-Assisted Operations", "RESPONSIBLE AI",
     "AI workflow visibility tools with clear human oversight boundaries and governance."),
]

for i, (icon, title, tag, desc) in enumerate(sections):
    with cols[i % 3]:
        st.markdown(f"""
        <div class='section-card'>
            <div class='sc-icon'>{icon}</div>
            <div class='sc-title'>{title}</div>
            <div class='sc-tag'>{tag}</div>
            <div class='sc-desc'>{desc}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("## Portfolio At a Glance")

k1, k2, k3, k4 = st.columns(4)
kpis = [
    ("7", "Portfolio Sections"),
    ("6", "Workflow Analysis Tools"),
    ("100%", "No-PHI Synthetic Data"),
    ("Remote", "Work Ready"),
]
for col, (val, label) in zip([k1, k2, k3, k4], kpis):
    with col:
        st.markdown(f"""
        <div class='kpi-box'>
            <div class='kpi-value'>{val}</div>
            <div class='kpi-label'>{label}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div class='footer'>
    Created by <b>Kori Pickle</b> · Healthcare Operations Portfolio · Tennessee · Remote Ready<br/>
    <a href='https://github.com/koripickle1101-TN/healthcare-workflow-portfolio'
       target='_blank' style='color:#FF8200;'>GitHub</a>
    &nbsp;·&nbsp;
    <span style='color:#aaa;font-size:0.7rem;'>
        All data is synthetic. No PHI. No clinical decisions.
    </span>
</div>
""", unsafe_allow_html=True)
