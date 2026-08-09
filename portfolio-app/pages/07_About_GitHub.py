"""About & GitHub — portfolio context, tools, and links."""

import streamlit as st
from components.styles import inject_global_css
from components.header import render_sidebar_header

st.set_page_config(page_title="About | Kori Pickle", page_icon="👤", layout="wide")
inject_global_css()
render_sidebar_header()

st.markdown("""
<div class='page-header'>
    <div class='page-header-eyebrow'>Section 07 · About This Portfolio</div>
    <div class='page-header-title'>About & GitHub</div>
    <div class='page-header-sub'>
        Portfolio context · Tools used · What this demonstrates
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("## About Kori Pickle")
    st.markdown("""
    <div class='body-text'>
    Healthcare operations professional with a focus on revenue cycle management,
    prior authorization, patient access, and denial prevention. Based in Tennessee.
    Remote-ready.<br/><br/>
    This portfolio was built to demonstrate practical understanding of how administrative
    workflows impact operational performance and patient access outcomes — not just theoretical
    knowledge, but applied thinking documented in real tools and analysis.<br/><br/>
    <b>The core question driving all of this work:</b><br/>
    <i>"Where does the workflow break — and how do we stop it before it becomes a denial?"</i>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("## What This Portfolio Demonstrates")
    items = [
        ("Revenue Cycle Thinking", "Understanding of end-to-end RCM — from scheduling to payment — and where upstream failures create downstream costs."),
        ("Prior Authorization Operations", "Tracking, aging, payer friction analysis, and workflow design for PA management."),
        ("Patient Access & Eligibility", "Real-time verification requirements, intake quality controls, and COB handling."),
        ("Denial Prevention Strategy", "Root cause analysis, repeat denial pattern identification, and feedback loop design."),
        ("Workflow Mapping", "Process visualization, failure point identification, and risk scoring across the revenue cycle."),
        ("Responsible AI Application", "Practical AI use cases in healthcare ops with clear human oversight boundaries and governance documentation."),
        ("Data Tools Without PHI", "All analysis uses synthetic data. No real patient information. Full HIPAA compliance awareness."),
    ]
    for title, desc in items:
        st.markdown(f"""
        <div class='info-card'>
            <div class='info-card-title'>🟠 {title}</div>
            <div class='info-card-body'>{desc}</div>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("## Tools Used")
    tools = [
        ("Python", "Core language for all data and workflow tools"),
        ("Streamlit", "Portfolio web app framework"),
        ("Pandas", "Data manipulation and analysis"),
        ("Plotly", "Interactive charts and visualizations"),
        ("GitHub", "Version control and portfolio hosting"),
        ("Streamlit Cloud", "Live deployment"),
    ]
    for tool, desc in tools:
        st.markdown(f"""
        <div class='metric-card' style='margin-bottom:0.6rem;'>
            <div class='metric-title'>{tool}</div>
            <div class='metric-desc'>{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("## Portfolio Links")
    st.markdown("""
    <div class='info-card'>
        <div class='info-card-title'>🔗 GitHub Repository</div>
        <div class='info-card-body'>
            <a href='https://github.com/koripickle1101-TN/healthcare-workflow-portfolio'
               target='_blank' style='color:#FF8200;font-weight:600;'>
               github.com/koripickle1101-TN
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='orange-callout' style='margin-top:1rem;'>
        <strong>Data Notice:</strong> All data in this portfolio is synthetic and generated
        for demonstration purposes only. No PHI. No real patient records.
        No clinical decisions. No payer decisions.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div class='footer'>
    Kori Pickle · Healthcare Operations Portfolio · Tennessee · Remote Ready<br/>
    All data synthetic · No PHI · No clinical decisions
</div>
""", unsafe_allow_html=True)
