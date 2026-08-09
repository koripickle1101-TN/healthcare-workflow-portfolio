"""Prior Authorization — aging, payer friction, and workflow risk."""

import streamlit as st
import pandas as pd
import plotly.express as px
from components.styles import inject_global_css
from components.header import render_sidebar_header

st.set_page_config(page_title="Prior Authorization | Kori Pickle", page_icon="📋", layout="wide")
inject_global_css()
render_sidebar_header()

st.markdown("""
<div class='page-header'>
    <div class='page-header-eyebrow'>Section 03 · Auth Operations</div>
    <div class='page-header-title'>Prior Authorization</div>
    <div class='page-header-sub'>
        Authorization aging · Payer friction patterns · PA workflow risk scoring
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='orange-callout'>
    <strong>Core Problem:</strong> Prior authorization denials are almost always preventable.
    They happen when tracking is reactive, timelines are missed, and payer rules
    are not embedded into the scheduling workflow from day one.
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📊 PA Risk Tracker", "🔥 Payer Friction", "📋 PA Workflow"])

with tab1:
    st.markdown("### Authorization Aging Queue (Synthetic Data)")
    pa_data = {
        "Patient ID": ["PT-001","PT-002","PT-003","PT-004","PT-005",
                        "PT-006","PT-007","PT-008","PT-009","PT-010"],
        "Service": ["MRI Brain","Knee Surgery","Infusion Therapy","Sleep Study",
                    "Cardiac Cath","Physical Therapy","Colonoscopy","CT Chest",
                    "Hip Replacement","Rheumatology"],
        "Payer": ["Aetna","BCBS","Humana","UHC","Aetna","Medicaid",
                  "BCBS","Cigna","Humana","UHC"],
        "Days Pending": [3, 12, 8, 21, 5, 30, 6, 15, 18, 9],
        "Status": ["Active","At Risk","Active","Critical","Active",
                   "Critical","Active","At Risk","At Risk","Active"],
        "SLA Breach Risk": ["Low","High","Medium","Critical","Low",
                            "Critical","Low","High","High","Medium"]
    }
    df = pd.DataFrame(pa_data)
    color_map = {"Active":"#4CAF50","At Risk":"#FF8200","Critical":"#CC0000"}
    fig = px.bar(
        df, x="Patient ID", y="Days Pending", color="Status",
        color_discrete_map=color_map,
        title="PA Aging Queue — Days Pending by Patient",
        hover_data=["Service","Payer","SLA Breach Risk"]
    )
    fig.update_layout(
        plot_bgcolor="white", paper_bgcolor="white",
        font_family="Inter", xaxis_title="", yaxis_title="Days Pending"
    )
    st.plotly_chart(fig, use_container_width=True)

    c1, c2, c3 = st.columns(3)
    c1.metric("Critical (30+ Days)", "2 cases")
    c2.metric("At Risk (11–29 Days)", "3 cases")
    c3.metric("Avg Days Pending", "12.7 days")

with tab2:
    st.markdown("### Payer Friction Heatmap")
    payers = ["Aetna","BCBS","Cigna","Humana","Medicaid","UHC"]
    services = ["Surgery","Infusion","Imaging","PT/OT","Sleep Study","Cardiology"]
    friction_data = [
        [2, 4, 3, 1, 3, 5],
        [3, 2, 4, 2, 4, 3],
        [4, 3, 2, 3, 3, 4],
        [5, 5, 3, 2, 5, 4],
        [5, 4, 4, 3, 5, 5],
        [3, 4, 3, 2, 4, 3],
    ]
    heat_df = pd.DataFrame(friction_data, index=payers, columns=services)
    fig2 = px.imshow(
        heat_df,
        color_continuous_scale=["#FFFFFF","#FFD9A8","#FF8200","#CC3300"],
        title="Payer Friction Score by Service Type (1=Low, 5=High)",
        text_auto=True,
        aspect="auto"
    )
    fig2.update_layout(font_family="Inter", title_font_size=14)
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown("""
    <div class='orange-callout'>
        <strong>Reading this chart:</strong> Darker orange = higher payer friction = more PA effort required.
        Medicaid and Humana show the highest friction across most service types.
        Use this to prioritize staffing and proactive outreach.
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("### Prior Authorization Workflow Steps")
    steps = [
        ("Identify PA Requirement at Scheduling",
         "Embed payer-specific PA rules in scheduling system. Flag required services before the appointment is confirmed."),
        ("Initiate PA Request Within 24 Hours",
         "Submit to payer the same day scheduling is confirmed. Delays compound quickly with longer payer timelines."),
        ("Document Submission Confirmation",
         "Record submission date, payer reference number, and expected turnaround in the patient account."),
        ("Track Daily in Aging Queue",
         "No PA should go more than 3 business days without a status update. Assign ownership to each open request."),
        ("Escalate At-Risk Cases",
         "Cases approaching service date without approval need supervisor escalation and peer-to-peer review readiness."),
        ("Document Auth Number Before Service",
         "Auth number must be recorded in the account before the patient arrives. No auth = no service."),
        ("Monitor for Expiration Post-Auth",
         "Auth approvals expire. Track expiration dates for ongoing or recurring services and renew proactively."),
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

st.markdown("---")
st.markdown("""
<div class='footer'>Kori Pickle · Healthcare Operations Portfolio · All data synthetic · No PHI</div>
""", unsafe_allow_html=True)
