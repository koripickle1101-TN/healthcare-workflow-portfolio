import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="Responsible AI Healthcare Operations Study Tool",
    page_icon="🟧",
    layout="wide",
    initial_sidebar_state="expanded",
)

TENNESSEE_ORANGE = "#FF8200"
BLACK = "#000000"
WHITE = "#FFFFFF"
WARM_GRAY = "#E8E3DC"
SOFT_GRAY = "#F7F4EF"
DARK_GRAY = "#2A2A2A"

st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800;900&family=Homemade+Apple&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
        color: {BLACK};
        background: {WHITE};
    }}

    .stApp {{
        background:
            radial-gradient(circle at top right, rgba(255,130,0,.08), transparent 24%),
            linear-gradient(180deg, #FFFFFF 0%, #FFFFFF 65%, #FBF8F3 100%);
    }}

    section[data-testid="stSidebar"] {{
        background: #FFFFFF;
        border-right: 1px solid {WARM_GRAY};
    }}

    .hero {{
        min-height: 430px;
        padding: 58px 56px 42px 56px;
        border: 1px solid {WARM_GRAY};
        border-radius: 32px;
        background: linear-gradient(135deg, #FFFFFF 0%, #FFFFFF 74%, rgba(255,130,0,.08) 100%);
        box-shadow: 0 24px 70px rgba(0,0,0,.06);
        position: relative;
        overflow: hidden;
        margin-bottom: 34px;
    }}

    .hero::after {{
        content: "";
        position: absolute;
        right: -70px;
        top: -80px;
        width: 300px;
        height: 300px;
        border: 1px dashed rgba(255,130,0,.40);
        border-radius: 999px;
    }}

    .eyebrow {{
        font-size: 12px;
        letter-spacing: 2.8px;
        text-transform: uppercase;
        font-weight: 800;
        color: {DARK_GRAY};
        border-bottom: 2px solid {TENNESSEE_ORANGE};
        display: inline-block;
        padding-bottom: 8px;
        margin-bottom: 24px;
    }}

    .hero h1 {{
        font-family: 'Playfair Display', serif;
        font-size: clamp(46px, 6vw, 92px);
        line-height: .90;
        color: {BLACK};
        letter-spacing: -2.4px;
        max-width: 980px;
        margin: 0 0 26px 0;
    }}

    .hero p {{
        font-size: 18px;
        line-height: 1.7;
        max-width: 860px;
        color: #222222;
    }}

    .orange {{ color: {TENNESSEE_ORANGE}; }}

    .node-row {{
        display: flex;
        align-items: center;
        gap: 16px;
        margin-top: 34px;
        flex-wrap: wrap;
    }}

    .node {{
        width: 60px;
        height: 60px;
        border: 2px solid {TENNESSEE_ORANGE};
        border-radius: 999px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 900;
        color: {TENNESSEE_ORANGE};
        background: #FFFFFF;
        box-shadow: 0 0 0 10px rgba(255,130,0,.06), 0 0 28px rgba(255,130,0,.22);
    }}

    .connector {{
        width: 82px;
        height: 2px;
        background-image: linear-gradient(to right, rgba(255,130,0,.80) 45%, rgba(255,130,0,0) 0%);
        background-position: bottom;
        background-size: 14px 2px;
        background-repeat: repeat-x;
    }}

    .section-title {{
        font-family: 'Playfair Display', serif;
        font-size: 42px;
        line-height: 1.0;
        margin: 32px 0 14px 0;
        letter-spacing: -1px;
    }}

    .subtle {{
        color: #4A4A4A;
        line-height: 1.65;
        font-size: 16px;
    }}

    .card {{
        border: 1px solid {WARM_GRAY};
        border-radius: 24px;
        padding: 26px;
        background: #FFFFFF;
        box-shadow: 0 16px 44px rgba(0,0,0,.045);
        height: 100%;
    }}

    .card h3 {{
        font-family: 'Playfair Display', serif;
        font-size: 28px;
        line-height: 1.05;
        margin: 0 0 12px 0;
    }}

    .metric {{
        border-left: 4px solid {TENNESSEE_ORANGE};
        background: {SOFT_GRAY};
        padding: 22px;
        border-radius: 18px;
        min-height: 128px;
    }}

    .metric .big {{
        font-family: 'Playfair Display', serif;
        font-size: 44px;
        line-height: .9;
        font-weight: 900;
        color: {BLACK};
    }}

    .metric .label {{
        margin-top: 10px;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 1.3px;
        font-weight: 800;
        color: #555;
    }}

    .callout {{
        border: 1px solid {WARM_GRAY};
        border-left: 6px solid {TENNESSEE_ORANGE};
        border-radius: 22px;
        padding: 24px 28px;
        background: #FFFFFF;
        box-shadow: 0 16px 40px rgba(0,0,0,.04);
        margin: 20px 0;
    }}

    .signature {{
        font-family: 'Homemade Apple', cursive;
        font-size: 29px;
        color: #222;
        transform: rotate(-1deg);
        display: inline-block;
        margin-top: 6px;
    }}

    .footer {{
        text-align: center;
        border-top: 1px solid {WARM_GRAY};
        padding: 34px 0 20px 0;
        margin-top: 50px;
        color: #111;
    }}

    .icons {{
        display: flex;
        justify-content: center;
        gap: 12px;
        margin-top: 12px;
    }}

    .icon-circle {{
        width: 30px;
        height: 30px;
        border: 1px solid {WARM_GRAY};
        border-radius: 999px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 12px;
        font-weight: 800;
        color: {BLACK};
        background: #FFFFFF;
    }}

    .quiz-box {{
        padding: 22px;
        border-radius: 22px;
        border: 1px solid {WARM_GRAY};
        background: #FFFFFF;
        margin-bottom: 18px;
    }}

    .pill {{
        display: inline-block;
        border: 1px solid {TENNESSEE_ORANGE};
        color: {BLACK};
        background: rgba(255,130,0,.08);
        border-radius: 999px;
        padding: 8px 13px;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: .5px;
        text-transform: uppercase;
        margin: 4px 4px 4px 0;
    }}

    div.stButton > button, div.stDownloadButton > button {{
        border-radius: 999px;
        border: 1px solid {TENNESSEE_ORANGE};
        background: {TENNESSEE_ORANGE};
        color: white;
        font-weight: 800;
        padding: .7rem 1.1rem;
    }}

    div.stButton > button:hover, div.stDownloadButton > button:hover {{
        border: 1px solid {BLACK};
        color: white;
        background: {BLACK};
    }}

    .small-note {{
        font-size: 13px;
        color: #666;
        line-height: 1.55;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

MODULES = {
    "1. Responsible AI Foundations": {
        "tag": "Useful · Safe · Human-Guided",
        "lesson": "Responsible AI means artificial intelligence is designed, used, monitored, and governed in a way that supports people instead of harming them. In healthcare operations, responsible AI should improve workflow clarity, reduce avoidable burden, protect privacy, support human judgment, and create better long-term outcomes.",
        "healthcare_example": "An AI tool that flags prior authorization cases at risk of delay is responsible only if humans can review the recommendation, understand the reason, verify payer policy, and protect patient information.",
        "portfolio_move": "Add a Responsible AI Use Statement to every AI-supported portfolio tool.",
        "reflection": "Where could AI support healthcare operations without replacing human judgment?",
    },
    "2. AI + Operational Sustainability": {
        "tag": "Stability · Capacity · Trust",
        "lesson": "Sustainability in healthcare operations is not only environmental. It also means workflows can keep functioning safely, reliably, and fairly over time. A sustainable AI workflow should reduce rework, protect staff capacity, improve visibility, and avoid creating new hidden burdens.",
        "healthcare_example": "If AI speeds up claims review but creates confusing exception queues for staff, the workflow may look faster on paper while becoming less sustainable in practice.",
        "portfolio_move": "Add an Operational Sustainability section with staff burden, patient access, documentation quality, and long-term workflow reliability considerations.",
        "reflection": "How would you know whether an AI workflow is making the system more sustainable or just faster?",
    },
    "3. Strategic Foresight": {
        "tag": "Early Signals · Future Risk · Prevention",
        "lesson": "Strategic foresight means looking ahead before problems become expensive or harmful. Instead of waiting for denials, delays, complaints, or burnout, healthcare operations teams should monitor leading indicators that reveal where the workflow is starting to lose control.",
        "healthcare_example": "Repeated missing documentation, authorization aging, payer-specific requests, and queue backlog may signal future denials before the denial actually appears.",
        "portfolio_move": "Add Early Warning Signals to PriorAuthIQ, Silent Breakpoint Intelligence, or the Denial KPI Dashboard.",
        "reflection": "What early signal would you track first in patient access, prior authorization, or denial prevention?",
    },
    "4. Systemic Risk Assessment": {
        "tag": "Cause Chain · Downstream Damage",
        "lesson": "Systemic risk means one workflow issue can spread across multiple departments. In healthcare operations, an error rarely stays isolated. It may move from patient access to prior authorization, documentation, billing, denials, A/R, staff workload, and patient trust.",
        "healthcare_example": "Wrong insurance information can trigger eligibility failure, authorization delay, claim denial, patient confusion, staff rework, and revenue cycle instability.",
        "portfolio_move": "Create a workflow failure chain map showing how one upstream defect creates downstream operational damage.",
        "reflection": "Which upstream workflow failure creates the most downstream pressure in your portfolio tools?",
    },
    "5. Ethical Governance": {
        "tag": "Oversight · Accountability · Privacy",
        "lesson": "Ethical governance means clear rules for how AI is used, reviewed, audited, and corrected. Healthcare AI requires accountability because AI-supported decisions can affect patients, staff, documentation, access, compliance, and trust.",
        "healthcare_example": "A denial-risk scoring tool needs human review, no-PHI safeguards, audit logs, bias monitoring, policy validation, and clear escalation ownership.",
        "portfolio_move": "Add a Governance Checklist that includes human oversight, privacy, bias risk, auditability, validation, and accountability.",
        "reflection": "Who should be accountable when an AI-supported healthcare workflow recommendation is wrong?",
    },
    "6. Responsible Innovation": {
        "tag": "Problem First · AI Second",
        "lesson": "Responsible innovation means not using AI just because it is popular. The right question is whether AI solves the right problem safely, fairly, and measurably. Good innovation starts with workflow reality, not technology hype.",
        "healthcare_example": "Before adding AI to patient access, leaders should define the problem: missing data, eligibility errors, authorization delays, handoff failure, unclear ownership, or lack of visibility.",
        "portfolio_move": "Build a 'Should This Workflow Use AI?' decision checklist.",
        "reflection": "What healthcare operations problem should not be automated until the workflow is better understood?",
    },
    "7. Long-Term Value Creation": {
        "tag": "Beyond Speed · Beyond Cost",
        "lesson": "Long-term value means AI should improve more than short-term productivity. It should support patient access, staff capacity, documentation quality, compliance, trust, quality improvement, operational resilience, and financial stability.",
        "healthcare_example": "A faster workflow is not valuable if it creates more appeals, staff confusion, patient complaints, or compliance risk later.",
        "portfolio_move": "Create a value scorecard that tracks patient, staff, workflow, compliance, and financial outcomes.",
        "reflection": "Which metric proves an AI-supported healthcare workflow is creating real value, not just moving faster?",
    },
    "8. Capstone Framework": {
        "tag": "Responsible AI Healthcare Operations",
        "lesson": "The capstone connects responsible AI, operational sustainability, strategic foresight, systemic risk, governance, responsible innovation, and long-term value into one healthcare operations framework.",
        "healthcare_example": "A responsible AI framework for prior authorization would include no-PHI data, early warning signals, payer policy validation, staff capacity monitoring, human review, patient access impact, and measurable workflow improvement.",
        "portfolio_move": "Publish a Responsible AI Healthcare Operations Framework as a portfolio artifact and LinkedIn post.",
        "reflection": "How would you explain responsible AI healthcare operations in one professional sentence?",
    },
}

FLASHCARDS = [
    ("Responsible AI", "AI that is useful, safe, privacy-conscious, monitored, fair, and designed to support human decision-making."),
    ("Operational Sustainability", "The ability of a healthcare workflow to remain reliable, safe, manageable, and effective over time."),
    ("Strategic Foresight", "The practice of identifying early signals and future risks before problems become costly or harmful."),
    ("Systemic Risk", "A risk that spreads through connected workflows instead of staying isolated in one department."),
    ("Ethical Governance", "Rules, oversight, accountability, and audit processes that guide responsible AI use."),
    ("Responsible Innovation", "Using technology only when it solves a real problem safely, ethically, and measurably."),
    ("Long-Term Value", "Value measured beyond speed and cost, including patient trust, staff capacity, compliance, quality, and workflow stability."),
    ("Human Oversight", "The requirement that people review, validate, and remain accountable for AI-supported recommendations."),
]

QUIZ = [
    {
        "q": "In healthcare operations, responsible AI should primarily do what?",
        "options": ["Replace staff judgment", "Make every workflow faster no matter what", "Support safer, clearer, more accountable workflows", "Remove the need for compliance review"],
        "answer": "Support safer, clearer, more accountable workflows",
        "why": "Responsible AI supports human judgment, visibility, privacy, safety, and accountability. It should not replace human review in high-impact healthcare workflows.",
    },
    {
        "q": "Which is the best example of a leading indicator?",
        "options": ["A final denial after claim submission", "An authorization case aging past threshold", "A monthly revenue report after close", "A patient complaint after billing confusion"],
        "answer": "An authorization case aging past threshold",
        "why": "Authorization aging can warn teams before the downstream denial, delay, or rework happens.",
    },
    {
        "q": "What does systemic risk mean?",
        "options": ["A small issue that stays in one department", "A workflow issue that can spread across connected processes", "A risk that only affects finance", "A technical problem with no operational impact"],
        "answer": "A workflow issue that can spread across connected processes",
        "why": "In healthcare, a patient access error can move into prior authorization, documentation, billing, denials, A/R, and patient trust.",
    },
    {
        "q": "What is the strongest governance question for AI-supported healthcare workflows?",
        "options": ["Can the AI sound confident?", "Can the AI replace managers?", "Who reviews, validates, audits, and remains accountable?", "Can the AI make decisions without documentation?"],
        "answer": "Who reviews, validates, audits, and remains accountable?",
        "why": "Governance is about oversight, accountability, privacy, auditability, and human responsibility.",
    },
    {
        "q": "What is the best definition of long-term value in healthcare AI?",
        "options": ["Short-term speed only", "Cost reduction only", "Better visibility, patient trust, staff capacity, compliance, quality, and financial stability", "More automation regardless of impact"],
        "answer": "Better visibility, patient trust, staff capacity, compliance, quality, and financial stability",
        "why": "Long-term value has to balance operational, financial, patient, staff, quality, and compliance outcomes.",
    },
]

GOVERNANCE_CHECKLIST = [
    "Uses simulated no-PHI data or clearly defines PHI protections",
    "Requires human review before action",
    "Explains the workflow risk being monitored",
    "Identifies who owns the workflow decision",
    "Includes bias and fairness review",
    "Includes auditability and documentation trail",
    "Validates recommendations against payer policy or operational rules",
    "Measures staff burden and patient access impact",
    "Defines escalation thresholds",
    "Measures whether the tool improves long-term workflow reliability",
]


def footer():
    st.markdown(
        """
        <div class="footer">
            <div style="font-weight:800; letter-spacing:.4px;">Created by Kori Pickle</div>
            <div class="signature">Kori Pickle</div>
            <div class="icons">
                <span class="icon-circle">in</span>
                <span class="icon-circle">GH</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def progress_bar(score, total):
    pct = int((score / total) * 100) if total else 0
    st.progress(pct / 100)
    st.caption(f"Score: {score}/{total} · {pct}%")


with st.sidebar:
    st.markdown("### Healthcare Operations Intelligence")
    st.caption("Responsible AI · Workflow Intelligence · Governance")
    page = st.radio(
        "Choose a study mode",
        [
            "Home",
            "8-Module Study Path",
            "Flashcards",
            "Quiz",
            "Governance Checklist",
            "Portfolio Builder",
            "LinkedIn Post Generator",
            "Capstone Export",
        ],
    )
    st.divider()
    st.markdown("**Brand System**")
    st.markdown(f"<span class='pill'>White #FFFFFF</span><span class='pill'>Vols Orange #FF8200</span><span class='pill'>Black Typography</span>", unsafe_allow_html=True)
    st.caption("Built for Kori Pickle's healthcare operations portfolio.")

if page == "Home":
    st.markdown(
        """
        <div class="hero">
            <div class="eyebrow">Responsible AI for Healthcare Operations</div>
            <h1>Learn AI governance through a <span class="orange">workflow intelligence</span> lens.</h1>
            <p>This interactive study tool teaches responsible AI, sustainability, strategic foresight, systemic risk, governance, responsible innovation, and long-term value creation using healthcare operations examples.</p>
            <div class="node-row">
                <div class="node">AI</div><div class="connector"></div>
                <div class="node">RCM</div><div class="connector"></div>
                <div class="node">PA</div><div class="connector"></div>
                <div class="node">HIM</div><div class="connector"></div>
                <div class="node">QI</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns([1.1, 1, 1])
    with c1:
        st.markdown("<div class='metric'><div class='big'>8</div><div class='label'>Study Modules</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='metric'><div class='big'>5</div><div class='label'>Quiz Questions</div></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='metric'><div class='big'>1</div><div class='label'>Capstone Framework</div></div>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>What this tool helps you practice</div>", unsafe_allow_html=True)
    a, b = st.columns([1.15, .85])
    with a:
        st.markdown(
            """
            <div class="card">
                <h3>From AI hype to healthcare operations judgment</h3>
                <p class="subtle">This tool is designed to help you explain AI responsibly in healthcare operations. The focus is not coding. The focus is governance, workflow risk, patient impact, staff capacity, compliance, and long-term operational value.</p>
                <span class="pill">Revenue Cycle</span><span class="pill">Patient Access</span><span class="pill">Prior Authorization</span><span class="pill">Denial Prevention</span><span class="pill">Health Informatics</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with b:
        st.markdown(
            """
            <div class="callout">
                <strong>Core professional sentence:</strong><br><br>
                Responsible AI in healthcare operations should not only make workflows faster. It should make them safer, more visible, more accountable, and more sustainable for patients, staff, and the organization.
            </div>
            """,
            unsafe_allow_html=True,
        )
    footer()

elif page == "8-Module Study Path":
    st.markdown("<div class='section-title'>8-Module Study Path</div>", unsafe_allow_html=True)
    selected = st.selectbox("Select a module", list(MODULES.keys()))
    module = MODULES[selected]

    left, right = st.columns([1.2, .8])
    with left:
        st.markdown(f"<div class='card'><h3>{selected}</h3><span class='pill'>{module['tag']}</span><p class='subtle' style='margin-top:18px;'>{module['lesson']}</p></div>", unsafe_allow_html=True)
        st.markdown("### Healthcare example")
        st.info(module["healthcare_example"])
        st.markdown("### Portfolio move")
        st.success(module["portfolio_move"])
    with right:
        st.markdown("<div class='card'><h3>Reflection Prompt</h3><p class='subtle'>Use this to build LinkedIn posts, portfolio notes, or networking language.</p></div>", unsafe_allow_html=True)
        response = st.text_area(module["reflection"], height=180)
        if response:
            st.download_button("Download reflection", response, file_name=f"{selected.replace(' ', '_').replace('.', '')}_reflection.txt")

    footer()

elif page == "Flashcards":
    st.markdown("<div class='section-title'>Flashcards</div>", unsafe_allow_html=True)
    idx = st.slider("Choose a flashcard", 1, len(FLASHCARDS), 1) - 1
    term, definition = FLASHCARDS[idx]
    st.markdown(f"<div class='card'><h3>{term}</h3><p class='subtle'>{definition}</p></div>", unsafe_allow_html=True)
    st.caption("Study move: say the definition out loud, then translate it into a healthcare operations example.")
    user_example = st.text_area("Write your healthcare operations example", height=140)
    if user_example:
        st.success("Good. Now ask: does your example include workflow impact, human oversight, and patient or staff implications?")
    footer()

elif page == "Quiz":
    st.markdown("<div class='section-title'>Knowledge Check Quiz</div>", unsafe_allow_html=True)
    st.caption("Answer each question, then review the explanation.")
    score = 0
    answers = []
    for i, item in enumerate(QUIZ, start=1):
        st.markdown(f"<div class='quiz-box'><strong>Question {i}</strong><br>{item['q']}</div>", unsafe_allow_html=True)
        choice = st.radio("Select one", item["options"], key=f"q_{i}")
        correct = choice == item["answer"]
        if correct:
            score += 1
        answers.append((i, correct, item["answer"], item["why"]))

    if st.button("Grade quiz"):
        progress_bar(score, len(QUIZ))
        for i, correct, answer, why in answers:
            if correct:
                st.success(f"Question {i}: Correct. {why}")
            else:
                st.error(f"Question {i}: Review needed. Correct answer: {answer}. {why}")
    footer()

elif page == "Governance Checklist":
    st.markdown("<div class='section-title'>Responsible AI Governance Checklist</div>", unsafe_allow_html=True)
    st.write("Use this checklist to evaluate any AI-supported healthcare operations workflow.")
    completed = []
    for item in GOVERNANCE_CHECKLIST:
        checked = st.checkbox(item)
        if checked:
            completed.append(item)
    st.divider()
    progress_bar(len(completed), len(GOVERNANCE_CHECKLIST))
    if len(completed) == len(GOVERNANCE_CHECKLIST):
        st.success("This workflow has a strong responsible AI governance foundation.")
    elif len(completed) >= 6:
        st.warning("This workflow has a partial governance foundation. Review the unchecked items before implementation.")
    else:
        st.error("This workflow needs stronger governance before it should be trusted.")

    checklist_text = "Responsible AI Governance Checklist\n\n" + "\n".join([f"[{'x' if item in completed else ' '}] {item}" for item in GOVERNANCE_CHECKLIST])
    st.download_button("Download checklist", checklist_text, file_name="responsible_ai_governance_checklist.txt")
    footer()

elif page == "Portfolio Builder":
    st.markdown("<div class='section-title'>Portfolio Builder</div>", unsafe_allow_html=True)
    st.caption("Generate a professional Responsible AI section for one of your healthcare operations portfolio projects.")

    project_name = st.text_input("Project name", "AI-Assisted Revenue Cycle Workflow System")
    workflow_area = st.selectbox("Workflow area", ["Revenue Cycle", "Prior Authorization", "Patient Access", "Eligibility Verification", "Denial Prevention", "Health Informatics", "Healthcare Staffing", "Documentation Quality"])
    risk_signal = st.text_input("Primary workflow risk signal", "Authorization aging and documentation gaps")
    human_owner = st.text_input("Human review owner", "Revenue cycle lead, patient access supervisor, or operations analyst")
    patient_impact = st.text_area("Patient-centered impact", "Earlier workflow visibility may reduce avoidable delays, confusion, rework, and access friction.")

    generated = f"""Responsible AI Use Statement for {project_name}

This portfolio project uses simulated no-PHI data to explore how AI-assisted workflow visibility could support {workflow_area.lower()} operations. It is not intended to replace human review, payer policy interpretation, clinical judgment, coding validation, compliance oversight, or patient communication.

Primary workflow risk signal monitored:
{risk_signal}

Human oversight owner:
{human_owner}

Patient-centered impact:
{patient_impact}

Governance considerations:
- Human review is required before any operational action.
- No PHI is used in this prototype.
- Recommendations must be validated against current policy and workflow rules.
- Bias, fairness, and access implications should be reviewed.
- Staff burden and downstream workflow effects should be measured.
- The purpose is early risk detection, not autonomous decision-making.
"""
    st.text_area("Generated portfolio section", generated, height=340)
    st.download_button("Download portfolio section", generated, file_name="responsible_ai_portfolio_section.txt")
    footer()

elif page == "LinkedIn Post Generator":
    st.markdown("<div class='section-title'>LinkedIn Post Generator</div>", unsafe_allow_html=True)
    topic = st.selectbox("Choose a post angle", ["Responsible AI", "Strategic Foresight", "AI Governance", "Operational Sustainability", "Long-Term Value", "Systemic Risk"])
    custom_focus = st.text_input("Healthcare focus area", "revenue cycle, prior authorization, patient access, and denial prevention")

    post = f"""One thing I am learning about {topic.lower()} in healthcare operations is that AI should not be measured by speed alone.

In {custom_focus}, the real question is not only whether a tool can automate a task.

The better question is whether it helps teams see workflow risk earlier, protect human judgment, reduce avoidable administrative burden, support patient access, and create more accountable operations.

A faster workflow is not always a better workflow.

A responsible workflow is one that is visible, governed, measurable, and sustainable over time.

From a patient-to-professional perspective, I believe healthcare AI should support trust, safety, communication, documentation quality, and workflow reliability—not just efficiency.

#HealthcareOperations #ResponsibleAI #RevenueCycleManagement #PatientAccess #PriorAuthorization #DenialPrevention #HealthInformatics #WorkflowIntelligence #HealthcareAdministration #OperationalExcellence"""

    st.text_area("Generated LinkedIn post", post, height=330)
    st.download_button("Download post", post, file_name="responsible_ai_linkedin_post.txt")
    footer()

elif page == "Capstone Export":
    st.markdown("<div class='section-title'>Capstone Export</div>", unsafe_allow_html=True)
    st.write("Create a concise framework summary you can use in your portfolio or LinkedIn content.")
    capstone_title = st.text_input("Framework title", "Responsible AI Healthcare Operations Framework")
    capstone_focus = st.text_area("Framework focus", "Workflow intelligence, patient access, revenue cycle visibility, denial prevention, health informatics, human oversight, and long-term operational sustainability.")

    capstone = f"""{capstone_title}
Created by Kori Pickle
Date: {date.today().isoformat()}

Purpose
This framework explains how responsible AI can support healthcare operations without replacing human judgment or ignoring patient impact.

Focus
{capstone_focus}

Core Principle
Responsible AI in healthcare operations should not only make workflows faster. It should make them safer, more visible, more accountable, and more sustainable for patients, staff, and the organization.

Framework Pillars
1. Responsible AI Foundations: AI must be useful, safe, privacy-conscious, monitored, fair, and human-guided.
2. Operational Sustainability: AI should support workflow reliability, staff capacity, patient trust, and long-term process stability.
3. Strategic Foresight: Teams should monitor early workflow signals before problems become denials, delays, harm, or burnout.
4. Systemic Risk Assessment: One upstream defect can spread across patient access, prior authorization, documentation, billing, denials, A/R, and patient experience.
5. Ethical Governance: AI-supported workflows require human oversight, accountability, PHI protection, auditability, bias review, and policy validation.
6. Responsible Innovation: Healthcare teams should define the real workflow problem before applying AI.
7. Long-Term Value Creation: Success should be measured through patient, staff, compliance, quality, operational, and financial outcomes.

Professional Positioning Statement
From a patient-to-professional perspective, responsible AI cannot only be measured by automation speed or cost reduction. It must also be measured by trust, safety, access, communication, documentation quality, workflow reliability, and human accountability.
"""
    st.text_area("Capstone framework", capstone, height=500)
    st.download_button("Download capstone", capstone, file_name="responsible_ai_healthcare_operations_framework.txt")
    footer()
