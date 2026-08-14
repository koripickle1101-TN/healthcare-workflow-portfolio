"""
Healthcare Workflow Intelligence Engine
Kori Pickle — Portfolio Home
"""

import streamlit as st
from components.styles import inject_global_css
from components.header import render_sidebar_header

st.set_page_config(page_title="Kori Pickle | Healthcare Operations Portfolio", page_icon="🏥", layout="wide", initial_sidebar_state="expanded")
inject_global_css()
render_sidebar_header()

st.markdown("<div class='hero-banner'><div class='hero-eyebrow'>Healthcare Operations Intelligence Engine</div><div class='hero-name'>Kori <span>Pickle</span></div><div class='hero-subtitle'>Revenue Cycle Management · Prior Authorization · Denial Prevention · Patient Access · Workflow Integrity · Responsible AI in Healthcare</div><div class='hero-tags'><span class='hero-tag'>RCM</span><span class='hero-tag'>Prior Auth</span><span class='hero-tag'>Denial Prevention</span><span class='hero-tag'>Patient Access</span><span class='hero-tag'>Workflow Analysis</span><span class='hero-tag'>Remote Ready</span><span class='hero-tag'>Tennessee</span></div></div>", unsafe_allow_html=True)

st.markdown("<div class='signature-question'><span class='sq-label'>Portfolio Signature Question</span><div class='sq-text'>Where does the workflow break — and how do we stop it before it becomes a denial?</div></div>", unsafe_allow_html=True)

st.markdown("## About This Portfolio")
st.markdown("<div class='body-text'>This portfolio demonstrates applied healthcare operations knowledge through student-developed analysis of revenue cycle management, prior authorization, patient access, denial prevention, workflow integrity, and responsible AI.<br/><br/>All projects use synthetic or fictional no-PHI data and do not represent professional healthcare employment experience.<br/><br/><b>The core argument:</b> Most revenue cycle failures do not start in billing. They start upstream — in intake, eligibility, authorization, and documentation. This portfolio is built around finding those upstream breaks before they cost the organization money.</div>", unsafe_allow_html=True)

st.markdown("<br/>", unsafe_allow_html=True)
k1, k2, k3, k4 = st.columns(4)
k1.markdown("<div class='kpi-box'><div class='kpi-value'>7</div><div class='kpi-label'>Portfolio Sections</div></div>", unsafe_allow_html=True)
k2.markdown("<div class='kpi-box'><div class='kpi-value'>6</div><div class='kpi-label'>Workflow Analysis Tools</div></div>", unsafe_allow_html=True)
k3.markdown("<div class='kpi-box'><div class='kpi-value'>100%</div><div class='kpi-label'>No-PHI Synthetic Data</div></div>", unsafe_allow_html=True)
k4.markdown("<div class='kpi-box'><div class='kpi-value'>Remote</div><div class='kpi-label'>Work Ready</div></div>", unsafe_allow_html=True)

st.markdown("<br/><br/>", unsafe_allow_html=True)
st.markdown("## Portfolio Sections")

sections = [
    ("💰","Revenue Cycle Management","RCM ANALYSIS","Upstream failure mapping, clean claim rate improvement, and front-end validation strategy."),
    ("🏥","Patient Access and Eligibility","ACCESS OPERATIONS","Insurance verification accuracy, eligibility workflow gaps, and intake quality controls."),
    ("📋","Prior Authorization","AUTH OPERATIONS","Authorization aging, payer friction patterns, and PA workflow risk scoring."),
    ("🚫","Denials Management","DENIAL PREVENTION","Root cause pattern analysis, repeat denial identification, and prevention checkpoints."),
    ("🗺️","Workflow Mapping","PROCESS INTEGRITY","End-to-end revenue cycle workflow visualization and failure point identification."),
    ("🤖","AI-Assisted Operations","RESPONSIBLE AI","AI workflow visibility tools with clear human oversight boundaries and governance."),
]

col_a, col_b = st.columns(2)
for i, (icon, title, tag, desc) in enumerate(sections):
    col = col_a if i % 2 == 0 else col_b
    with col:
        st.markdown(f"<div class='section-card'><div class='sc-icon'>{icon}</div><div class='sc-title'>{title}</div><div class='sc-tag'>{tag}</div><div class='sc-desc'>{desc}</div></div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div class='footer'><div class='footer-created'>Created by</div><div class='footer-signature'>Kori Pickle</div><div class='footer-icons'><a class='footer-icon-link' href='https://github.com/koripickle1101-TN/healthcare-workflow-portfolio' target='_blank'>GH</a><a class='footer-icon-link' href='https://linkedin.com' target='_blank'>in</a></div></div>", unsafe_allow_html=True)
