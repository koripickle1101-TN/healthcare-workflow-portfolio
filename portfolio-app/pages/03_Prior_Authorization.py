import streamlit as st
import pandas as pd
import plotly.express as px
from components.styles import inject_global_css
from components.header import render_sidebar_header

st.set_page_config(page_title="Prior Authorization | Kori Pickle", page_icon="📋", layout="wide")
inject_global_css()
render_sidebar_header()

st.markdown("<div class='page-header'><div class='page-header-eyebrow'>Section 03 · Auth Operations</div><div class='page-header-title'>Prior Authorization</div><div class='page-header-sub'>Authorization aging · Payer friction patterns · PA workflow risk scoring</div></div>", unsafe_allow_html=True)
st.markdown("<div class='orange-callout'><strong>Core Problem:</strong> Prior authorization denials are almost always preventable. They happen when tracking is reactive, timelines are missed, and payer rules are not embedded into the scheduling workflow from day one.</div>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["PA Aging Queue", "Payer Friction", "PA Workflow"])

with tab1:
    st.markdown("### Authorization Aging Queue (Synthetic Data)")
    df = pd.DataFrame({
        "Patient": ["PT-001","PT-002","PT-003","PT-004","PT-005","PT-006"],
        "Days Pending": [4, 8, 12, 18, 25, 29],
        "Status": ["Active","Active","At Risk","At Risk","Critical","Critical"]
    })
    color_map = {"Active":"#228B22","At Risk":"#FF8200","Critical":"#CC0000"}
    fig = px.bar(df, x="Patient", y="Days Pending", color="Status", color_discrete_map=color_map, text="Days Pending", title="PA Aging Queue — Days Pending by Patient")
    fig.update_traces(textposition="outside")
    fig.update_layout(plot_bgcolor="white", paper_bgcolor="white", yaxis_range=[0,35], font_family="Inter")
    st.plotly_chart(fig, use_container_width=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("Critical (30+ days)", "2 cases")
    c2.metric("At Risk (11-29 days)", "3 cases")
    c3.metric("Avg Days Pending", "16.0")

with tab2:
    st.markdown("### Payer Friction Patterns")
    for payer, score, note in [
        ("United Healthcare","High Friction","Requires portal submission. Peer-to-peer available but delayed."),
        ("Cigna","High Friction","Frequent requests for additional clinical documentation."),
        ("Aetna","Medium Friction","Generally responsive. PA turnaround 5-7 business days."),
        ("BCBS","Medium Friction","Inconsistent requirements by plan type. Verify each time."),
        ("Medicare Advantage","Low Friction","Most services covered without PA. Check plan-specific rules."),
        ("Medicaid","Variable","Requirements vary significantly by state and managed care plan."),
    ]:
        color = "#CC0000" if score == "High Friction" else "#FF8200" if score == "Medium Friction" else "#228B22"
        st.markdown(f"<div class='info-card' style='border-left:3px solid {color};'><div class='info-card-title' style='color:{color};'>{payer} — {score}</div><div class='info-card-body'>{note}</div></div>", unsafe_allow_html=True)

with tab3:
    st.markdown("### PA Workflow — Best Practice Steps")
    for i, (title, desc) in enumerate([
        ("Verify PA requirement at scheduling", "Check payer and plan-specific rules before the appointment is booked."),
        ("Submit PA request minimum 5 business days before service", "Last-minute submissions are the leading cause of PA denials."),
        ("Document clinical necessity in the chart before submission", "Payer reviewers need diagnosis codes and clinical rationale upfront."),
        ("Track PA status daily in a centralized aging queue", "Untracked PAs expire or time out without staff awareness."),
        ("Escalate to peer-to-peer within 48 hours of denial", "Peer-to-peer reversal rates are significantly higher than written appeals."),
        ("Communicate PA status to patient before service date", "Patients should never arrive for services with unresolved PA issues."),
    ], 1):
        st.markdown(f"<div class='process-step'><div class='step-num'>{i}</div><div><div class='step-title'>{title}</div><div class='step-desc'>{desc}</div></div></div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div class='footer'><div class='footer-created'>Created by</div><div class='footer-signature'>Kori Pickle</div><div class='footer-icons'><a class='footer-icon-link' href='https://github.com/koripickle1101-TN' target='_blank'>GH</a><a class='footer-icon-link' href='https://linkedin.com' target='_blank'>in</a></div></div>", unsafe_allow_html=True)
