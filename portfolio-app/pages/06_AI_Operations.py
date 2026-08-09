import streamlit as st
from components.styles import inject_global_css
from components.header import render_sidebar_header

st.set_page_config(page_title="AI Operations | Kori Pickle", page_icon="🤖", layout="wide")
inject_global_css()
render_sidebar_header()

st.markdown("<div class='page-header'><div class='page-header-eyebrow'>Section 06 · Responsible AI</div><div class='page-header-title'>AI-Assisted Operations</div><div class='page-header-sub'>Practical AI use cases · Human oversight boundaries · Governance in healthcare operations</div></div>", unsafe_allow_html=True)
st.markdown("<div class='orange-callout'><strong>Core Position:</strong> AI in healthcare operations is a workflow visibility tool — not a decision-maker. Every AI output requires a trained human to review, validate, and act. This section documents where AI adds value and where the line must be drawn.</div>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["AI Use Cases", "Governance Boundaries", "Human Oversight"])

with tab1:
    st.markdown("### Where AI Adds Value in Healthcare Operations")
    for title, desc in [
        ("Eligibility Verification Automation","AI-assisted real-time eligibility checks reduce manual phone calls and catch coverage gaps before service."),
        ("Prior Authorization Status Tracking","Automated PA aging queues surface at-risk authorizations before they expire or time out."),
        ("Denial Pattern Recognition","ML pattern analysis identifies repeat denial root causes faster than manual audit."),
        ("Claim Scrubbing and Error Detection","AI claim scrubbers catch coding mismatches and missing documentation before submission."),
        ("Patient Financial Counseling Estimates","AI tools calculate estimated patient responsibility at scheduling to support upfront collection."),
        ("Workflow Bottleneck Identification","Process analytics identify handoff delays and redundant steps in the revenue cycle."),
    ]:
        st.markdown(f"<div class='info-card'><div class='info-card-title'>{title}</div><div class='info-card-body'>{desc}</div></div>", unsafe_allow_html=True)

with tab2:
    st.markdown("### Governance Boundaries — Where AI Must Not Decide Alone")
    for title, desc, risk in [
        ("Clinical necessity determination","AI cannot determine whether a service is medically necessary. A licensed provider must make that call.","Critical Boundary"),
        ("Appeal decision authority","AI can draft appeal language but a human must review, approve, and submit every appeal.","Critical Boundary"),
        ("Patient financial hardship decisions","Charity care, write-offs, and payment plan exceptions require human judgment and policy authority.","High Boundary"),
        ("Denial write-off approval","AI can flag candidates for write-off but financial authority to approve must remain with a human.","High Boundary"),
        ("Payer contract interpretation","AI can surface contract terms but a revenue cycle professional must interpret and apply them.","Medium Boundary"),
    ]:
        color = "#CC0000" if risk == "Critical Boundary" else "#FF8200" if risk == "High Boundary" else "#888888"
        st.markdown(f"<div class='info-card' style='border-left:3px solid {color};'><div class='info-card-title' style='color:{color};'>{title} — {risk}</div><div class='info-card-body'>{desc}</div></div>", unsafe_allow_html=True)

with tab3:
    st.markdown("### Human Oversight Checklist for AI-Assisted Workflows")
    for i, (title, desc) in enumerate([
        ("All AI outputs are reviewed before action is taken","No AI recommendation is acted on without a trained staff member reviewing it first."),
        ("AI tools are validated against payer-specific rules","Generic AI tools must be configured and tested against each payer contract."),
        ("Staff are trained to identify AI errors","Teams must know what AI errors look like and how to escalate when something is wrong."),
        ("AI audit logs are maintained and reviewed monthly","Every AI action is logged. Logs are reviewed for accuracy and anomalies."),
        ("Patients are informed when AI tools are used in their care pathway","Transparency with patients about AI use is an ethical and emerging regulatory requirement."),
        ("AI tools are evaluated for bias in denial and payment patterns","Pattern analysis must include equity checks to ensure AI is not amplifying existing disparities."),
    ], 1):
        st.markdown(f"<div class='process-step'><div class='step-num'>{i}</div><div><div class='step-title'>{title}</div><div class='step-desc'>{desc}</div></div></div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div class='footer'><div class='footer-created'>Created by</div><div class='footer-signature'>Kori Pickle</div><div class='footer-icons'><a class='footer-icon-link' href='https://github.com/koripickle1101-TN' target='_blank'>GH</a><a class='footer-icon-link' href='https://linkedin.com' target='_blank'>in</a></div></div>", unsafe_allow_html=True)
