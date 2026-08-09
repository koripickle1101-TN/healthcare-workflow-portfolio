import streamlit as st
import pandas as pd
import plotly.express as px
from components.styles import inject_global_css
from components.header import render_sidebar_header

st.set_page_config(page_title="Patient Access | Kori Pickle", page_icon="🏥", layout="wide")
inject_global_css()
render_sidebar_header()

st.markdown("<div class='page-header'><div class='page-header-eyebrow'>Section 02 · Patient Access</div><div class='page-header-title'>Patient Access and Eligibility</div><div class='page-header-sub'>Insurance verification accuracy · Eligibility workflow gaps · Intake quality controls</div></div>", unsafe_allow_html=True)

st.markdown("<div class='orange-callout'><strong>Core Argument:</strong> Patient access is the front door of the revenue cycle. When eligibility is wrong at intake, every step downstream pays for it. Real-time verification and registration accuracy are denial prevention.</div>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Eligibility Accuracy", "COB and Secondary", "Intake Checklist"])

with tab1:
    st.markdown("### Eligibility Accuracy by Verification Method")
    methods = ["Real-Time Electronic", "Manual Phone Call", "Prior Visit Assumed", "Portal Self-Report", "No Verification"]
    accuracy = [97, 78, 52, 61, 18]
    denial = [3, 14, 38, 29, 71]
    df = pd.DataFrame({"Method": methods, "Accuracy": accuracy, "Denial Rate": denial})
    fig = px.bar(df, x="Method", y="Accuracy", text="Accuracy", title="Eligibility Accuracy Rate by Verification Method", color="Accuracy", color_continuous_scale=["#CC0000", "#FF8200", "#228B22"])
    fig.update_traces(texttemplate="%{text}%", textposition="outside")
    fig.update_layout(plot_bgcolor="white", paper_bgcolor="white", yaxis_range=[0, 110], coloraxis_showscale=False, font_family="Inter")
    st.plotly_chart(fig, use_container_width=True)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Real-Time Accuracy", "97%")
    c2.metric("Prior Visit Accuracy", "52%")
    c3.metric("No Verification Denial Rate", "71%")
    c4.metric("Real-Time Denial Rate", "3%")

with tab2:
    st.markdown("### Coordination of Benefits Failure Points")
    for title, desc in [
        ("Primary Payer Sequencing Error", "Claims submitted to secondary payer first. Results in full denial or incorrect payment."),
        ("Spouse Coverage Not Identified", "Spouse employer coverage not collected at registration. COB not applied."),
        ("Medicare Secondary Payer Rules Not Applied", "Employer coverage is primary over Medicare but Medicare billed first."),
        ("COB Not Updated After Life Event", "Marriage or new employment changes coverage order. Registration not updated."),
        ("Secondary Claim Not Filed", "Primary pays but secondary claim never submitted. Revenue left on the table."),
    ]:
        st.markdown(f"<div class='info-card'><div class='info-card-title'>{title}</div><div class='info-card-body'>{desc}</div></div>", unsafe_allow_html=True)

with tab3:
    st.markdown("### Patient Access Intake Checklist")
    steps = [
        ("Insurance card collected and scanned", "Physical or digital copy required at every visit."),
        ("Real-time eligibility run at scheduling AND check-in", "Two-touch verification catches coverage changes."),
        ("Primary vs secondary payer confirmed", "COB order documented before service is rendered."),
        ("Authorization requirement checked", "PA requirements verified at scheduling, not after."),
        ("Referral collected if required", "HMO plans require referral documentation."),
        ("Patient demographics verified", "Demographic mismatches cause claim rejections."),
        ("Copay collected at point of service", "Point-of-service collection reduces bad debt."),
        ("MSP questionnaire completed if applicable", "Required for Medicare patients."),
    ]
    for i, (title, desc) in enumerate(steps, 1):
        st.markdown(f"<div class='process-step'><div class='step-num'>{i}</div><div><div class='step-title'>{title}</div><div class='step-desc'>{desc}</div></div></div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div class='footer'><div class='footer-created'>Created by</div><div class='footer-signature'>Kori Pickle</div><div class='footer-icons'><a class='footer-icon-link' href='https://github.com/koripickle1101-TN' target='_blank'>GH</a><a class='footer-icon-link' href='https://linkedin.com' target='_blank'>in</a></div></div>", unsafe_allow_html=True)
