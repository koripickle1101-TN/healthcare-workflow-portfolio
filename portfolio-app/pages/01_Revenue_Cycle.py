import streamlit as st
import pandas as pd
import plotly.express as px
from components.styles import inject_global_css
from components.header import render_sidebar_header

st.set_page_config(page_title="Revenue Cycle | Kori Pickle", page_icon="💰", layout="wide")
inject_global_css()
render_sidebar_header()

st.markdown("<div class='page-header'><div class='page-header-eyebrow'>Section 01 · Revenue Cycle</div><div class='page-header-title'>Revenue Cycle Management</div><div class='page-header-sub'>Upstream failure mapping · Clean claim rate improvement · Front-end validation strategy</div></div>", unsafe_allow_html=True)
st.markdown("<div class='orange-callout'><strong>Core Argument:</strong> Most revenue cycle failures do not start in billing. They start upstream — in intake, eligibility, authorization, and documentation. Fixing the front end is the highest-leverage move in the revenue cycle.</div>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Clean Claim Rate", "Denial Root Causes", "Front-End Checklist"])

with tab1:
    st.markdown("### Clean Claim Rate by Department (Synthetic Data)")
    df = pd.DataFrame({
        "Department": ["Emergency","Radiology","Surgery","Primary Care","Behavioral Health","Orthopedics"],
        "Clean Claim Rate": [72, 81, 88, 91, 65, 85],
        "Avg Days to Pay": [38, 29, 24, 21, 45, 27]
    })
    fig = px.bar(df, x="Department", y="Clean Claim Rate", text="Clean Claim Rate", color="Clean Claim Rate", color_continuous_scale=["#CC0000","#FF8200","#228B22"], title="Clean Claim Rate by Department")
    fig.update_traces(texttemplate="%{text}%", textposition="outside")
    fig.update_layout(plot_bgcolor="white", paper_bgcolor="white", yaxis_range=[0,110], coloraxis_showscale=False, font_family="Inter")
    st.plotly_chart(fig, use_container_width=True)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Highest Clean Claim Rate", "91% — Primary Care")
    c2.metric("Lowest Clean Claim Rate", "65% — Behavioral Health")
    c3.metric("Avg Days to Pay (Best)", "21 days")
    c4.metric("Avg Days to Pay (Worst)", "45 days")

with tab2:
    st.markdown("### Denial Root Cause Distribution (Synthetic Data)")
    causes = ["Missing Authorization","Eligibility Error","Duplicate Claim","Coding Error","Missing Documentation","Timely Filing","Other"]
    volumes = [28, 22, 8, 19, 14, 6, 3]
    df2 = pd.DataFrame({"Root Cause": causes, "Denial Volume": volumes})
    fig2 = px.bar(df2, x="Root Cause", y="Denial Volume", text="Denial Volume", title="Denial Volume by Root Cause", color_discrete_sequence=["#FF8200"])
    fig2.update_traces(textposition="outside")
    fig2.update_layout(plot_bgcolor="white", paper_bgcolor="white", yaxis_range=[0,35], font_family="Inter")
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown("<div class='orange-callout'><strong>Key Finding:</strong> Missing authorization (28%) and eligibility errors (22%) account for 50% of all denials — both are preventable at the front end before the claim is ever submitted.</div>", unsafe_allow_html=True)

with tab3:
    st.markdown("### Front-End Revenue Cycle Checklist")
    for i, (title, desc) in enumerate([
        ("Real-time eligibility verified at scheduling AND check-in", "Two-touch verification prevents coverage change denials."),
        ("Authorization obtained before service is rendered", "PA confirmed and documented in the chart before appointment."),
        ("Referral collected for HMO and EPO plan types", "Missing referrals are a top denial cause for managed care plans."),
        ("Patient demographics verified against insurance card", "Name, DOB, and member ID mismatches cause rejections."),
        ("COB order confirmed for patients with multiple insurances", "Primary and secondary payer sequence documented at registration."),
        ("Estimated patient responsibility calculated and communicated", "Upfront financial counseling reduces bad debt and surprises."),
        ("Copay and deductible collected at point of service", "POS collection is the single best bad debt prevention strategy."),
        ("Clinical documentation supports medical necessity", "Diagnosis codes must support the ordered service before submission."),
    ], 1):
        st.markdown(f"<div class='process-step'><div class='step-num'>{i}</div><div><div class='step-title'>{title}</div><div class='step-desc'>{desc}</div></div></div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div class='footer'><div class='footer-created'>Created by</div><div class='footer-signature'>Kori Pickle</div><div class='footer-icons'><a class='footer-icon-link' href='https://github.com/koripickle1101-TN' target='_blank'>GH</a><a class='footer-icon-link' href='https://linkedin.com' target='_blank'>in</a></div></div>", unsafe_allow_html=True)
