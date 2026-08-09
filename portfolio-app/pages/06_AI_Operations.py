"""AI-Assisted Healthcare Operations — responsible AI with human oversight."""

import streamlit as st
from components.styles import inject_global_css
from components.header import render_sidebar_header

st.set_page_config(page_title="AI Operations | Kori Pickle", page_icon="🤖", layout="wide")
inject_global_css()
render_sidebar_header()

st.markdown("""
<div class='page-header'>
    <div class='page-header-eyebrow'>Section 06 · Responsible AI</div>
    <div class='page-header-title'>AI-Assisted Operations</div>
    <div class='page-header-sub'>
        Workflow visibility tools · Human oversight boundaries · Responsible AI governance
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='orange-callout'>
    <strong>Core Position:</strong> AI does not replace healthcare operations judgment.
    It surfaces patterns, flags risk, and generates summaries — so that
    humans can review, validate, and decide faster and with better information.
    The human stays responsible. The AI stays in its lane.
</div>
""", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["🤖 What AI Can Do", "🚫 What AI Cannot Do", "📋 Governance Checklist"])

with tab1:
    st.markdown("### Where AI Adds Value in Healthcare Operations")
    uses = [
        ("Pattern Recognition",
         "AI can identify repeat denial patterns across payers, providers, and service types faster than manual review — surfacing trends that inform workflow correction."),
        ("Workflow Risk Scoring",
         "AI can score open authorizations, eligibility gaps, and documentation completeness to prioritize which cases need human attention first."),
        ("Summary Generation",
         "AI can generate daily huddle scripts, leadership briefs, and operational summaries from structured data — reducing administrative time."),
        ("Queue Aging Alerts",
         "AI can flag cases approaching SLA deadlines, authorization expiration dates, and denial appeal windows before they are missed."),
        ("Denial Categorization",
         "AI can sort and categorize incoming denials by type, payer, and root cause — feeding the root cause analysis process."),
        ("Documentation Gap Detection",
         "AI can compare clinical documentation against payer-specific medical necessity criteria and flag likely gaps before submission."),
    ]
    for title, desc in uses:
        st.markdown(f"""
        <div class='info-card' style='border-left:4px solid #FF8200;'>
            <div class='info-card-title'>✅ {title}</div>
            <div class='info-card-body'>{desc}</div>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("### What AI Cannot and Should Not Do")
    limits = [
        ("Make Clinical Decisions",
         "AI cannot determine medical necessity, clinical appropriateness, or treatment decisions. Those require licensed clinical judgment."),
        ("Override Payer Rules",
         "AI cannot interpret or override payer contracts, coverage determinations, or denial outcomes. Compliance requires human review."),
        ("Submit Claims or Authorizations",
         "Automated submission without human review creates compliance and accuracy risk. AI supports the process — humans authorize the action."),
        ("Replace Coding Expertise",
         "AI-assisted coding tools must be reviewed by a certified coder. Incorrect codes submitted without review create audit exposure."),
        ("Access or Process Real PHI Without Governance",
         "Any AI tool working with real patient data requires HIPAA compliance review, BAA agreements, and formal governance documentation."),
        ("Be Trusted Without Validation",
         "AI outputs are workflow signals — not verified facts. Every AI-generated flag, summary, or score requires human validation before action."),
    ]
    for title, desc in limits:
        st.markdown(f"""
        <div class='info-card' style='border-left:4px solid #CC0000;'>
            <div class='info-card-title'>🚫 {title}</div>
            <div class='info-card-body'>{desc}</div>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown("### Responsible AI Governance Checklist")
    checks = [
        ("Synthetic or de-identified data only during development and testing",
         "No real patient data should be used to build, test, or demonstrate AI tools outside of a formally governed environment."),
        ("Clear human-in-the-loop documentation",
         "Every AI tool must document which decisions require human review and which outputs are informational only."),
        ("Bias and fairness monitoring",
         "AI tools used in healthcare operations must be monitored for disparate impact across payer types, demographics, and service lines."),
        ("Explainability built into outputs",
         "AI-generated flags, scores, and summaries must include the reasoning behind the output — not just the result."),
        ("Audit trail for all AI-assisted actions",
         "When AI supports a workflow decision, the action taken and the human who took it must be documented."),
        ("Regular model and rule validation",
         "AI tools must be reviewed against current payer rules, coding guidelines, and operational realities on a defined schedule."),
    ]
    for title, desc in checks:
        st.markdown(f"""
        <div class='info-card'>
            <div class='info-card-title'>📋 {title}</div>
            <div class='info-card-body'>{desc}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class='orange-callout' style='margin-top:1.5rem;'>
        <strong>Portfolio Note:</strong> All tools in this portfolio use synthetic no-PHI data only.
        No clinical decisions are made. No payer decisions are made. No patient-specific recommendations
        are generated. All flagged records are workflow signals that require human validation.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div class='footer'>Kori Pickle · Healthcare Operations Portfolio · All data synthetic · No PHI</div>
""", unsafe_allow_html=True)
