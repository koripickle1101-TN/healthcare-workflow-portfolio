import streamlit as st
import pandas as pd
import plotly.express as px
from components.styles import inject_global_css
from components.header import render_sidebar_header

st.set_page_config(page_title="Workflow Mapping | Kori Pickle", page_icon="🗺️", layout="wide")
inject_global_css()
render_sidebar_header()

st.markdown("<div class='page-header'><div class='page-header-eyebrow'>Section 05 · Process Integrity</div><div class='page-header-title'>Workflow Mapping</div><div class='page-header-sub'>End-to-end revenue cycle visualization · Failure point identification · Process integrity</div></div>", unsafe_allow_html=True)
st.markdown("<div class='orange-callout'><strong>Core Argument:</strong> You cannot fix a workflow you cannot see. Mapping the revenue cycle end-to-end reveals the handoff gaps, redundant steps, and silent failure points that cost organizations money every single day.</div>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Workflow Map", "Failure Point Analysis"])

with tab1:
    st.markdown("### Revenue Cycle — End-to-End Workflow Steps")
    steps = [
        ("1","Scheduling and Pre-Registration","Patient demographics, insurance, and appointment type collected. PA requirement checked.","Front End","5/5"),
        ("2","Eligibility Verification","Real-time eligibility run. Coverage confirmed. COB sequenced. Patient responsibility estimated.","Front End","4/5"),
        ("3","Prior Authorization","PA submitted if required. Tracking initiated. Status confirmed before service date.","Front End","5/5"),
        ("4","Check-In and Registration","Demographics verified. Eligibility re-confirmed. Copay collected. Referral confirmed.","Front End","4/5"),
        ("5","Clinical Documentation","Provider documents diagnosis, procedure, and medical necessity in the chart.","Clinical","3/5"),
        ("6","Charge Capture","Services coded. CPT and ICD-10 codes assigned. Charges entered within 24 hours.","Mid Cycle","3/5"),
        ("7","Claim Scrubbing","Claim reviewed against payer rules. Errors corrected before submission.","Mid Cycle","4/5"),
        ("8","Claim Submission","Clean claim submitted to payer within 5 business days of service.","Mid Cycle","5/5"),
        ("9","Payment Posting","EOB received. Payment posted. Adjustments applied. Patient balance identified.","Back End","4/5"),
        ("10","Denial Management","Denied claims triaged. Root cause identified. Appeals filed within payer deadline.","Back End","5/5"),
        ("11","Patient Billing","Patient statement issued. Payment plan offered if needed. Collections as last resort.","Back End","3/5"),
    ]
    for num, title, desc, phase, risk in steps:
        color = "#CC0000" if risk in ["5/5"] and phase in ["Front End","Back End"] else "#FF8200" if risk == "4/5" else "#228B22"
        st.markdown(f"<div class='process-step'><div class='step-num'>{num}</div><div><div class='step-title'> in a centralized aging queue", "Untracked PAs expire or time out without staff awareness."),
        ("Escalate to peer-to-peer within 48 hours of denial", "Peer-to-peer reversal rates are significantly higher than written appeals."),
        ("Communicate PA status to patient before service date", "Patients should never arrive for services with unresolved PA issues."),
    ], 1):
        st.markdown(f"<div class='process-step'><div class='step-num'>{i}</div><div><div class='step-title'>{title}</div><div class='step-desc'>{desc}</div></div></div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div class='footer'><div class='footer-created'>Created by</div><div class='footer-signature'>Kori Pickle</div><div class='footer-icons'><a class='footer-icon-link' href='https://github.com/koripickle1101-TN' target='_blank'>GH</a><a class='footer-icon-link' href='https://linkedin.com' target='_blank'>in</a></div></div>", unsafe_allow_html=True)
