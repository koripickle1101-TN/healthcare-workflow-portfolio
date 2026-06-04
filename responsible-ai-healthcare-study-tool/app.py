import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="Responsible AI Healthcare Operations Intelligence",
    page_icon="🟧",
    layout="wide",
    initial_sidebar_state="expanded",
)

TENNESSEE_ORANGE = "#FF8200"
BLACK = "#000000"
WHITE = "#FFFFFF"
WARM_GRAY = "#E8E3DC"
SOFT_GRAY = "#F7F4EF"
INK = "#151515"

st.markdown(
    f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:wght@700;800;900&family=Homemade+Apple&display=swap');

:root {{
  --orange:{TENNESSEE_ORANGE};
  --black:{BLACK};
  --white:{WHITE};
  --warm:{WARM_GRAY};
  --soft:{SOFT_GRAY};
}}

html, body, [class*="css"] {{
  font-family:'Inter', sans-serif;
  color:var(--black);
}}

.stApp {{
  background:
    radial-gradient(circle at 92% 4%, rgba(255,130,0,.12), transparent 26%),
    radial-gradient(circle at 4% 20%, rgba(255,130,0,.045), transparent 20%),
    linear-gradient(180deg,#FFFFFF 0%,#FFFFFF 72%,#FBF8F3 100%);
}}

section[data-testid="stSidebar"] {{
  background:#FFFFFF;
  border-right:1px solid var(--warm);
}}

section[data-testid="stSidebar"] * {{
  font-family:'Inter', sans-serif;
}}

h1,h2,h3,.serif {{
  font-family:'Playfair Display', serif !important;
}}

.block-container {{
  padding-top: 2.2rem;
  padding-bottom: 2.5rem;
  max-width: 1240px;
}}

.hero {{
  min-height:500px;
  padding:64px 58px 52px 58px;
  border:1px solid var(--warm);
  border-radius:36px;
  background:
    linear-gradient(135deg,#FFFFFF 0%,#FFFFFF 68%,rgba(255,130,0,.08) 100%);
  box-shadow:0 28px 78px rgba(0,0,0,.07);
  position:relative;
  overflow:hidden;
  margin-bottom:34px;
}}
.hero:before {{
  content:"";
  position:absolute;
  top:40px;
  right:46px;
  width:190px;
  height:190px;
  border:1px dashed rgba(255,130,0,.42);
  border-radius:999px;
}}
.hero:after {{
  content:"";
  position:absolute;
  right:-135px;
  bottom:-165px;
  width:430px;
  height:430px;
  border:1px solid rgba(255,130,0,.16);
  border-radius:999px;
  box-shadow:0 0 80px rgba(255,130,0,.08);
}}
.eyebrow {{
  font-size:12px;
  letter-spacing:3.1px;
  text-transform:uppercase;
  font-weight:900;
  color:#333;
  display:inline-block;
  padding-bottom:8px;
  border-bottom:2px solid var(--orange);
  margin-bottom:24px;
}}
.hero h1 {{
  font-family:'Playfair Display', serif;
  font-size:clamp(48px,6.8vw,96px);
  line-height:.88;
  letter-spacing:-2.7px;
  margin:0 0 28px 0;
  max-width:990px;
}}
.hero p {{
  max-width:900px;
  font-size:18px;
  line-height:1.72;
  color:#242424;
}}
.orange {{color:var(--orange)}}

.node-row {{display:flex; align-items:center; gap:14px; flex-wrap:wrap; margin-top:34px;}}
.node {{
  width:64px; height:64px; border-radius:999px;
  border:2px solid var(--orange);
  display:flex; align-items:center; justify-content:center;
  background:#fff; color:var(--orange); font-weight:900;
  box-shadow:0 0 0 10px rgba(255,130,0,.07), 0 0 34px rgba(255,130,0,.23);
}}
.connector {{
  width:78px; height:2px;
  background-image:linear-gradient(to right, rgba(255,130,0,.85) 45%, rgba(255,130,0,0) 0%);
  background-size:13px 2px; background-repeat:repeat-x;
}}

.card {{
  border:1px solid var(--warm);
  border-radius:26px;
  padding:26px;
  background:#FFFFFF;
  box-shadow:0 18px 48px rgba(0,0,0,.05);
  height:100%;
}}
.card h3 {{
  font-family:'Playfair Display', serif;
  font-size:30px;
  line-height:1.05;
  margin:0 0 12px 0;
}}
.card p, .subtle {{color:#464646; line-height:1.68; font-size:16px;}}

.grid-card {{
  border:1px solid var(--warm);
  background:#fff;
  border-radius:24px;
  padding:22px;
  min-height:160px;
  box-shadow:0 14px 34px rgba(0,0,0,.04);
}}
.metric {{
  border:1px solid var(--warm);
  border-left:5px solid var(--orange);
  border-radius:22px;
  background:var(--soft);
  padding:24px;
  min-height:138px;
}}
.metric .big {{font-family:'Playfair Display',serif; font-size:48px; font-weight:900; line-height:.9;}}
.metric .label {{font-size:12px; font-weight:900; letter-spacing:1.4px; text-transform:uppercase; margin-top:12px; color:#555;}}

.section-title {{
  font-family:'Playfair Display', serif;
  font-size:44px;
  line-height:.98;
  letter-spacing:-1px;
  margin:38px 0 14px 0;
}}

.pill {{
  display:inline-block;
  border:1px solid var(--orange);
  background:rgba(255,130,0,.08);
  color:#111;
  border-radius:999px;
  padding:8px 13px;
  margin:4px 5px 4px 0;
  font-size:12px;
  font-weight:900;
  letter-spacing:.55px;
  text-transform:uppercase;
}}
.callout {{
  border:1px solid var(--warm);
  border-left:6px solid var(--orange);
  border-radius:24px;
  padding:24px 28px;
  background:#fff;
  box-shadow:0 18px 44px rgba(0,0,0,.045);
  margin:18px 0;
}}
.warning-panel {{
  border:1px solid rgba(255,130,0,.35);
  border-radius:24px;
  background:linear-gradient(135deg, rgba(255,130,0,.09), #FFFFFF 70%);
  padding:24px;
}}
.table-wrap {{
  border:1px solid var(--warm);
  border-radius:24px;
  background:#fff;
  padding:16px;
}}
.signature {{
  font-family:'Homemade Apple', cursive;
  font-size:30px;
  color:#222;
  display:inline-block;
  transform:rotate(-1deg);
  margin-top:6px;
}}
.footer {{
  text-align:center;
  border-top:1px solid var(--warm);
  margin-top:56px;
  padding:34px 0 18px 0;
}}
.icons {{display:flex; gap:12px; justify-content:center; margin-top:12px;}}
.icon-circle {{
  width:31px; height:31px; border-radius:999px; border:1px solid var(--warm);
  display:inline-flex; align-items:center; justify-content:center;
  background:#fff; color:#111; font-size:12px; font-weight:900;
}}

div.stButton > button, div.stDownloadButton > button {{
  border-radius:999px;
  border:1px solid var(--orange);
  background:var(--orange);
  color:white;
  font-weight:900;
  padding:.72rem 1.15rem;
}}
div.stButton > button:hover, div.stDownloadButton > button:hover {{
  background:#111; border:1px solid #111; color:white;
}}

textarea, input {{border-radius:16px !important;}}
.small {{font-size:13px; color:#666; line-height:1.55;}}
</style>
""",
    unsafe_allow_html=True,
)

MODULES = [
    {
        "name":"Responsible AI Foundations",
        "node":"AI",
        "tag":"Useful · Safe · Human-Guided",
        "definition":"Responsible AI means artificial intelligence is designed, used, monitored, and governed in a way that supports people instead of harming them.",
        "healthcare":"In healthcare operations, responsible AI should improve workflow clarity, reduce avoidable burden, protect privacy, support human judgment, and create better long-term outcomes.",
        "example":"An AI tool that flags prior authorization cases at risk of delay is responsible only if humans can review the recommendation, understand the reason, verify payer policy, and protect patient information.",
        "risks":["Over-automation", "Privacy exposure", "Unclear accountability", "Unsupported recommendations"],
        "portfolio":"Add a Responsible AI Use Statement to every AI-supported portfolio tool.",
        "prompt":"Where could AI support healthcare operations without replacing human judgment?",
    },
    {
        "name":"AI + Operational Sustainability",
        "node":"OS",
        "tag":"Stability · Capacity · Trust",
        "definition":"Operational sustainability means workflows can keep functioning safely, reliably, and fairly over time.",
        "healthcare":"In healthcare, sustainability includes staff capacity, workflow reliability, patient trust, reduced rework, documentation quality, and responsible data use.",
        "example":"If AI speeds up claims review but creates confusing exception queues for staff, the workflow may look faster on paper while becoming less sustainable in practice.",
        "risks":["Hidden staff burden", "More exception queues", "Workflow drift", "Trust erosion"],
        "portfolio":"Add an Operational Sustainability section with staff burden, patient access, documentation quality, and long-term reliability considerations.",
        "prompt":"How would you know whether an AI workflow is making the system more sustainable or just faster?",
    },
    {
        "name":"Strategic Foresight",
        "node":"SF",
        "tag":"Early Signals · Future Risk · Prevention",
        "definition":"Strategic foresight means looking ahead before problems become expensive, harmful, or operationally unstable.",
        "healthcare":"Teams should monitor leading indicators that show where the workflow is starting to lose control before denials, delays, complaints, or burnout appear.",
        "example":"Repeated missing documentation, authorization aging, payer-specific requests, and queue backlog may signal future denials before the denial appears.",
        "risks":["Late detection", "Reactive management", "Escalation delay", "Missed leading indicators"],
        "portfolio":"Add Early Warning Signals to PriorAuthIQ, Silent Breakpoint Intelligence, or the Denial KPI Dashboard.",
        "prompt":"What early signal would you track first in patient access, prior authorization, or denial prevention?",
    },
    {
        "name":"Systemic Risk Assessment",
        "node":"SR",
        "tag":"Cause Chain · Downstream Damage",
        "definition":"Systemic risk means one workflow issue can spread across multiple departments instead of staying isolated.",
        "healthcare":"A patient access error may move into prior authorization, documentation, billing, denials, A/R, staff workload, and patient trust.",
        "example":"Wrong insurance information can trigger eligibility failure, authorization delay, claim denial, patient confusion, staff rework, and revenue cycle instability.",
        "risks":["Department silos", "Handoff failure", "Downstream rework", "Patient confusion"],
        "portfolio":"Create a workflow failure chain map showing how one upstream defect creates downstream operational damage.",
        "prompt":"Which upstream workflow failure creates the most downstream pressure in your portfolio tools?",
    },
    {
        "name":"Ethical Governance",
        "node":"EG",
        "tag":"Oversight · Accountability · Privacy",
        "definition":"Ethical governance means clear rules for how AI is used, reviewed, audited, corrected, and owned.",
        "healthcare":"Healthcare AI requires accountability because AI-supported decisions can affect patients, staff, documentation, access, compliance, and trust.",
        "example":"A denial-risk scoring tool needs human review, no-PHI safeguards, audit logs, bias monitoring, policy validation, and clear escalation ownership.",
        "risks":["Bias", "PHI exposure", "No audit trail", "No owner"],
        "portfolio":"Add a Governance Checklist that includes human oversight, privacy, bias risk, auditability, validation, and accountability.",
        "prompt":"Who should be accountable when an AI-supported healthcare workflow recommendation is wrong?",
    },
    {
        "name":"Responsible Innovation",
        "node":"RI",
        "tag":"Problem First · AI Second",
        "definition":"Responsible innovation means not using AI just because it is popular. The workflow problem must come first.",
        "healthcare":"Good innovation starts with real workflow evidence: missing data, authorization delays, handoff failure, unclear ownership, or visibility gaps.",
        "example":"Before adding AI to patient access, leaders should define whether the problem is eligibility accuracy, missing intake data, prior auth aging, or unclear escalation ownership.",
        "risks":["AI hype", "Wrong problem", "No measurement", "Poor adoption"],
        "portfolio":"Build a 'Should This Workflow Use AI?' decision checklist.",
        "prompt":"What healthcare operations problem should not be automated until the workflow is better understood?",
    },
    {
        "name":"Long-Term Value Creation",
        "node":"LV",
        "tag":"Beyond Speed · Beyond Cost",
        "definition":"Long-term value means AI should improve more than short-term productivity or cost reduction.",
        "healthcare":"Value should include patient access, staff capacity, documentation quality, compliance, trust, quality improvement, operational resilience, and financial stability.",
        "example":"A faster workflow is not valuable if it creates more appeals, staff confusion, patient complaints, or compliance risk later.",
        "risks":["Short-term thinking", "Cost-only measurement", "Quality blind spots", "Staff burnout"],
        "portfolio":"Create a value scorecard that tracks patient, staff, workflow, compliance, and financial outcomes.",
        "prompt":"Which metric proves an AI-supported healthcare workflow is creating real value, not just moving faster?",
    },
    {
        "name":"Capstone Framework",
        "node":"CF",
        "tag":"Responsible AI Healthcare Operations",
        "definition":"The capstone combines responsible AI, sustainability, foresight, systemic risk, governance, innovation, and long-term value into one framework.",
        "healthcare":"A responsible AI framework for prior authorization would include no-PHI data, early warning signals, payer policy validation, staff capacity monitoring, human review, patient access impact, and measurable workflow improvement.",
        "example":"A no-PHI AI-assisted RCM dashboard should explain its purpose, limits, risk signals, required human oversight, and governance boundaries.",
        "risks":["No implementation boundary", "No measurement plan", "No governance language", "No patient impact review"],
        "portfolio":"Publish a Responsible AI Healthcare Operations Framework as a portfolio artifact and LinkedIn post.",
        "prompt":"How would you explain responsible AI healthcare operations in one professional sentence?",
    },
]

FLASHCARDS = [
    ("Responsible AI", "AI that is useful, safe, monitored, privacy-conscious, fair, and designed to support human decision-making."),
    ("Operational Sustainability", "The ability of a workflow to remain reliable, safe, manageable, and effective over time."),
    ("Strategic Foresight", "Identifying early signals and future risks before they become costly or harmful."),
    ("Systemic Risk", "A risk that spreads through connected workflows instead of staying isolated in one department."),
    ("Ethical Governance", "Rules, oversight, accountability, auditability, and correction processes for responsible AI use."),
    ("Responsible Innovation", "Using technology only when it solves a real problem safely, ethically, and measurably."),
    ("Long-Term Value", "Value measured by patient trust, staff capacity, compliance, quality, workflow stability, and financial performance."),
    ("Human Oversight", "The requirement that people review, validate, and remain accountable for AI-supported recommendations."),
    ("Leading Indicator", "A signal that appears before a downstream failure, such as authorization aging before denial."),
    ("No-PHI Prototype", "A portfolio tool that uses simulated data only and avoids patient-identifiable information."),
]

QUIZ = [
    {"q":"In healthcare operations, responsible AI should primarily do what?","options":["Replace staff judgment","Make every workflow faster no matter what","Support safer, clearer, more accountable workflows","Remove compliance review"],"answer":"Support safer, clearer, more accountable workflows","why":"Responsible AI supports human judgment, visibility, privacy, safety, and accountability."},
    {"q":"Which is the best example of a leading indicator?","options":["A final denial after claim submission","An authorization case aging past threshold","A monthly revenue report after close","A patient complaint after billing confusion"],"answer":"An authorization case aging past threshold","why":"Authorization aging can warn teams before the downstream denial, delay, or rework happens."},
    {"q":"What does systemic risk mean?","options":["A small issue that stays in one department","A workflow issue that can spread across connected processes","A risk that only affects finance","A technical problem with no operational impact"],"answer":"A workflow issue that can spread across connected processes","why":"One upstream defect can spread across access, authorization, documentation, billing, denials, and patient experience."},
    {"q":"What is the strongest governance question for AI-supported healthcare workflows?","options":["Can the AI sound confident?","Can AI replace managers?","Who reviews, validates, audits, and remains accountable?","Can AI decide without documentation?"],"answer":"Who reviews, validates, audits, and remains accountable?","why":"Governance is about oversight, accountability, privacy, auditability, and human responsibility."},
    {"q":"What is the best definition of long-term value in healthcare AI?","options":["Short-term speed only","Cost reduction only","Better visibility, patient trust, staff capacity, compliance, quality, and financial stability","More automation regardless of impact"],"answer":"Better visibility, patient trust, staff capacity, compliance, quality, and financial stability","why":"Long-term value balances operational, financial, patient, staff, quality, and compliance outcomes."},
    {"q":"Which statement is most mature professionally?","options":["AI fixes healthcare by itself","AI should support workflow visibility and human oversight","Healthcare should automate everything possible","AI removes the need for process improvement"],"answer":"AI should support workflow visibility and human oversight","why":"Mature AI positioning avoids hype and emphasizes safe, governed operational support."},
    {"q":"What should happen before applying AI to a workflow?","options":["Buy a tool immediately","Define the real workflow problem","Remove humans from the process","Ignore current policies"],"answer":"Define the real workflow problem","why":"Responsible innovation starts with the problem, workflow evidence, and operational context."},
    {"q":"What does no-PHI mean in a portfolio tool?","options":["No financial data","No patient-identifiable health information","No process data","No healthcare examples"],"answer":"No patient-identifiable health information","why":"No-PHI data protects privacy and makes portfolio simulations safer and more professional."},
]

SCENARIOS = {
    "Prior Authorization Delay": {
        "summary":"Orthopedic authorization turnaround time is increasing, payer requests are repeating, and staff are manually tracking cases across spreadsheets.",
        "signals":["Authorization aging > 5 days", "Missing documentation", "Repeated payer clarification", "No clear escalation owner"],
        "risk":"Delayed care, denial risk, patient frustration, staff rework, and revenue cycle instability.",
        "governance":"Use AI only to flag risk; require human review for payer policy, documentation readiness, and escalation decisions.",
    },
    "Eligibility Verification Breakdown": {
        "summary":"Insurance mismatches are discovered after service instead of before the visit. Claims are being corrected downstream.",
        "signals":["Eligibility mismatch", "COB uncertainty", "Registration data gaps", "Repeated front-end corrections"],
        "risk":"Claim denials, patient billing confusion, delayed reimbursement, and rework burden.",
        "governance":"AI can identify mismatch patterns but staff must verify payer response, patient information, and coverage rules.",
    },
    "Denial Spike": {
        "summary":"Medical necessity and authorization denials increased across two service lines after a payer policy change.",
        "signals":["Denial rate increase", "Policy-related appeal notes", "Documentation gap trend", "A/R aging increase"],
        "risk":"Revenue leakage, appeal backlog, delayed correction, staff fatigue, and reporting instability.",
        "governance":"AI can surface patterns, but payer policy interpretation, coding validation, and compliance review must remain human-owned.",
    },
    "Healthcare Staffing Friction": {
        "summary":"Recruiters are spending more time on follow-ups, compliance checks, scheduling friction, and fragmented systems than candidate engagement.",
        "signals":["Slow placement cycle", "Compliance bottleneck", "Scheduling delay", "Recruiter workload imbalance"],
        "risk":"Recruiter burnout, staffing shortages, slower placements, and operational instability.",
        "governance":"AI can monitor workflow health and surface leading indicators, but candidate communication, compliance validation, and hiring judgment need human oversight.",
    },
}

GOVERNANCE_ITEMS = [
    "Uses simulated no-PHI data or clearly defines PHI protections",
    "Requires human review before operational action",
    "Explains the workflow risk being monitored",
    "Identifies the human workflow owner",
    "Includes bias and fairness review",
    "Includes auditability and documentation trail",
    "Validates recommendations against payer policy or operational rules",
    "Measures staff burden and patient access impact",
    "Defines escalation thresholds",
    "Measures whether the tool improves long-term workflow reliability",
    "Documents what AI should not decide",
    "Includes a communication plan for staff trust and adoption",
]

if "completed_modules" not in st.session_state:
    st.session_state.completed_modules = set()
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = None
if "saved_reflections" not in st.session_state:
    st.session_state.saved_reflections = []


def footer():
    st.markdown("""
    <div class="footer">
      <div style="font-weight:900; letter-spacing:.45px;">Created by Kori Pickle</div>
      <div class="signature">Kori Pickle</div>
      <div class="icons"><span class="icon-circle">in</span><span class="icon-circle">GH</span></div>
    </div>
    """, unsafe_allow_html=True)


def progress_metrics():
    completed = len(st.session_state.completed_modules)
    quiz = st.session_state.quiz_score if st.session_state.quiz_score is not None else 0
    c1,c2,c3,c4 = st.columns(4)
    c1.markdown(f"<div class='metric'><div class='big'>{completed}/8</div><div class='label'>Modules Completed</div></div>", unsafe_allow_html=True)
    c2.markdown(f"<div class='metric'><div class='big'>{quiz}</div><div class='label'>Latest Quiz Score</div></div>", unsafe_allow_html=True)
    c3.markdown(f"<div class='metric'><div class='big'>{len(st.session_state.saved_reflections)}</div><div class='label'>Saved Reflections</div></div>", unsafe_allow_html=True)
    c4.markdown("<div class='metric'><div class='big'>No</div><div class='label'>PHI Used</div></div>", unsafe_allow_html=True)


def module_card(module, idx):
    st.markdown(f"""
    <div class='card'>
      <div class='node' style='margin-bottom:18px;'>{module['node']}</div>
      <h3>{idx}. {module['name']}</h3>
      <span class='pill'>{module['tag']}</span>
      <p class='subtle' style='margin-top:16px;'><strong>Definition:</strong> {module['definition']}</p>
      <p class='subtle'><strong>Healthcare translation:</strong> {module['healthcare']}</p>
    </div>
    """, unsafe_allow_html=True)


def branded_download(label, text, filename):
    st.download_button(label, text, file_name=filename, mime="text/plain")

with st.sidebar:
    st.markdown("### Healthcare Operations Intelligence")
    st.caption("Responsible AI · Workflow Intelligence · Governance")
    page = st.radio("Choose a study mode", [
        "Executive Home",
        "8-Module Study Path",
        "Flashcards",
        "Scenario Lab",
        "Quiz Bank",
        "Governance Checklist",
        "Risk Scorecard",
        "Portfolio Builder",
        "LinkedIn Post Generator",
        "Capstone Export",
        "Progress Dashboard",
    ])
    st.divider()
    st.markdown("**Brand System**")
    st.markdown("<span class='pill'>White #FFFFFF</span><span class='pill'>Vols Orange #FF8200</span><span class='pill'>Black Typography</span>", unsafe_allow_html=True)
    st.caption("Built for Kori Pickle's healthcare operations portfolio. Simulated learning content only. No PHI.")

if page == "Executive Home":
    st.markdown("""
    <div class='hero'>
      <div class='eyebrow'>Responsible AI for Healthcare Operations</div>
      <h1>Build AI governance judgment through a <span class='orange'>workflow intelligence</span> lens.</h1>
      <p>This premium interactive study tool teaches responsible AI, operational sustainability, strategic foresight, systemic risk, ethical governance, responsible innovation, and long-term value creation using healthcare operations examples.</p>
      <div class='node-row'>
        <div class='node'>AI</div><div class='connector'></div>
        <div class='node'>RCM</div><div class='connector'></div>
        <div class='node'>PA</div><div class='connector'></div>
        <div class='node'>HIM</div><div class='connector'></div>
        <div class='node'>QI</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    progress_metrics()
    st.markdown("<div class='section-title'>What this tool helps you practice</div>", unsafe_allow_html=True)
    a,b = st.columns([1.18,.82])
    with a:
        st.markdown("""
        <div class='card'>
          <h3>From AI hype to healthcare operations judgment</h3>
          <p class='subtle'>This tool is designed to help you explain AI responsibly in healthcare operations. The focus is not coding. The focus is governance, workflow risk, patient impact, staff capacity, compliance, and long-term operational value.</p>
          <span class='pill'>Revenue Cycle</span><span class='pill'>Patient Access</span><span class='pill'>Prior Authorization</span><span class='pill'>Denial Prevention</span><span class='pill'>Health Informatics</span><span class='pill'>Healthcare Staffing</span>
        </div>
        """, unsafe_allow_html=True)
    with b:
        st.markdown("""
        <div class='callout'>
          <strong>Core professional sentence:</strong><br><br>
          Responsible AI in healthcare operations should not only make workflows faster. It should make them safer, more visible, more accountable, and more sustainable for patients, staff, and the organization.
        </div>
        """, unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Learning architecture</div>", unsafe_allow_html=True)
    cols = st.columns(4)
    for i,m in enumerate(MODULES[:4]):
        with cols[i]: module_card(m, i+1)
    cols2 = st.columns(4)
    for i,m in enumerate(MODULES[4:]):
        with cols2[i]: module_card(m, i+5)
    footer()

elif page == "8-Module Study Path":
    st.markdown("<div class='section-title'>8-Module Study Path</div>", unsafe_allow_html=True)
    selected_name = st.selectbox("Select a module", [m["name"] for m in MODULES])
    module = next(m for m in MODULES if m["name"] == selected_name)
    idx = [m["name"] for m in MODULES].index(selected_name)+1
    left,right = st.columns([1.18,.82])
    with left:
        module_card(module, idx)
        st.markdown("### Healthcare example")
        st.info(module["example"])
        st.markdown("### Key risks to watch")
        st.write(pd.DataFrame({"Risk Point": module["risks"], "Why it matters": ["Can weaken trust, reliability, compliance, or workflow stability." for _ in module["risks"]]}))
        st.markdown("### Portfolio move")
        st.success(module["portfolio"])
    with right:
        st.markdown("<div class='card'><h3>Reflection Workspace</h3><p class='subtle'>Write a practical answer you could turn into a portfolio note, LinkedIn post, or interview talking point.</p></div>", unsafe_allow_html=True)
        response = st.text_area(module["prompt"], height=230)
        if st.button("Save reflection") and response:
            st.session_state.saved_reflections.append({"module": module["name"], "reflection": response})
            st.success("Reflection saved in this session.")
        if st.button("Mark module complete"):
            st.session_state.completed_modules.add(module["name"])
            st.success("Module marked complete.")
        if response:
            branded_download("Download this reflection", response, f"{module['name'].lower().replace(' ','_')}_reflection.txt")
    footer()

elif page == "Flashcards":
    st.markdown("<div class='section-title'>Interactive Flashcards</div>", unsafe_allow_html=True)
    idx = st.slider("Choose a flashcard", 1, len(FLASHCARDS), 1)-1
    term, definition = FLASHCARDS[idx]
    st.markdown(f"<div class='card'><h3>{term}</h3><p class='subtle'>{definition}</p></div>", unsafe_allow_html=True)
    st.markdown("### Translate it into healthcare operations")
    example = st.text_area("Write your own example using revenue cycle, patient access, prior authorization, HIM, staffing, or denial prevention.", height=170)
    if example:
        st.success("Good. Now check whether your example includes workflow impact, human oversight, privacy/compliance, and patient or staff implications.")
    footer()

elif page == "Scenario Lab":
    st.markdown("<div class='section-title'>Scenario Lab</div>", unsafe_allow_html=True)
    scenario_name = st.selectbox("Choose a healthcare operations scenario", list(SCENARIOS.keys()))
    s = SCENARIOS[scenario_name]
    left,right = st.columns([1,.95])
    with left:
        st.markdown(f"<div class='card'><h3>{scenario_name}</h3><p class='subtle'>{s['summary']}</p></div>", unsafe_allow_html=True)
        st.markdown("### Leading indicators")
        st.write(pd.DataFrame({"Early Signal": s["signals"]}))
        st.markdown("### Downstream risk")
        st.warning(s["risk"])
        st.markdown("### Governance boundary")
        st.info(s["governance"])
    with right:
        st.markdown("### Your analysis")
        root = st.text_input("Likely root workflow issue")
        owner = st.text_input("Human owner / accountable role")
        intervention = st.text_area("Immediate containment action", height=120)
        kpi = st.text_input("KPI to monitor")
        output = f"""Scenario Analysis: {scenario_name}\n\nSummary: {s['summary']}\n\nLikely root workflow issue: {root}\nHuman owner/accountable role: {owner}\nImmediate containment action: {intervention}\nKPI to monitor: {kpi}\n\nGovernance boundary: {s['governance']}\n"""
        if root or owner or intervention or kpi:
            st.text_area("Generated scenario note", output, height=260)
            branded_download("Download scenario note", output, f"{scenario_name.lower().replace(' ','_')}_scenario_note.txt")
    footer()

elif page == "Quiz Bank":
    st.markdown("<div class='section-title'>Quiz Bank</div>", unsafe_allow_html=True)
    st.caption("Answer all questions, then grade your knowledge check.")
    score = 0
    details = []
    for i,item in enumerate(QUIZ, start=1):
        st.markdown(f"<div class='grid-card'><strong>Question {i}</strong><br>{item['q']}</div>", unsafe_allow_html=True)
        choice = st.radio("Select one", item["options"], key=f"quiz_{i}")
        correct = choice == item["answer"]
        if correct: score += 1
        details.append((i, correct, item["answer"], item["why"]))
    if st.button("Grade quiz"):
        st.session_state.quiz_score = score
        st.progress(score/len(QUIZ))
        st.subheader(f"Score: {score}/{len(QUIZ)}")
        for i,correct,answer,why in details:
            if correct: st.success(f"Question {i}: Correct. {why}")
            else: st.error(f"Question {i}: Review needed. Correct answer: {answer}. {why}")
    footer()

elif page == "Governance Checklist":
    st.markdown("<div class='section-title'>Responsible AI Governance Checklist</div>", unsafe_allow_html=True)
    st.caption("Use this to evaluate any AI-supported healthcare workflow or portfolio prototype.")
    completed=[]
    for item in GOVERNANCE_ITEMS:
        if st.checkbox(item): completed.append(item)
    pct = len(completed)/len(GOVERNANCE_ITEMS)
    st.progress(pct)
    st.subheader(f"Governance readiness: {len(completed)}/{len(GOVERNANCE_ITEMS)}")
    if pct >= .85: st.success("Strong governance foundation. This prototype is ready for professional presentation.")
    elif pct >= .55: st.warning("Partial governance foundation. Strengthen the unchecked items before presenting as mature.")
    else: st.error("Governance risk is high. Add oversight, accountability, privacy, and measurement details.")
    text = "Responsible AI Governance Checklist\n\n" + "\n".join([f"[{'x' if i in completed else ' '}] {i}" for i in GOVERNANCE_ITEMS])
    branded_download("Download checklist", text, "responsible_ai_governance_checklist.txt")
    footer()

elif page == "Risk Scorecard":
    st.markdown("<div class='section-title'>AI Workflow Risk Scorecard</div>", unsafe_allow_html=True)
    st.caption("Score a proposed AI-supported healthcare workflow before presenting it as responsible or implementation-ready.")
    cols = st.columns(2)
    with cols[0]:
        privacy = st.slider("Privacy / PHI protection", 0, 5, 3)
        oversight = st.slider("Human oversight clarity", 0, 5, 3)
        explainability = st.slider("Explainability / reason visibility", 0, 5, 3)
    with cols[1]:
        bias = st.slider("Bias and fairness review", 0, 5, 3)
        workflow = st.slider("Workflow fit", 0, 5, 3)
        measurement = st.slider("Success measurement plan", 0, 5, 3)
    total = privacy+oversight+explainability+bias+workflow+measurement
    st.markdown(f"<div class='metric'><div class='big'>{total}/30</div><div class='label'>Responsible AI Readiness Score</div></div>", unsafe_allow_html=True)
    if total >= 25: st.success("Strong readiness. The workflow has solid responsible AI structure.")
    elif total >= 17: st.warning("Moderate readiness. Good start, but governance needs tightening.")
    else: st.error("High risk. Do not present this as responsible AI without stronger safeguards.")
    footer()

elif page == "Portfolio Builder":
    st.markdown("<div class='section-title'>Portfolio Builder</div>", unsafe_allow_html=True)
    project_name = st.text_input("Project name", "AI-Assisted Revenue Cycle Workflow System")
    workflow_area = st.selectbox("Workflow area", ["Revenue Cycle", "Prior Authorization", "Patient Access", "Eligibility Verification", "Denial Prevention", "Health Informatics", "Healthcare Staffing", "Documentation Quality"])
    risk_signal = st.text_input("Primary workflow risk signal", "Authorization aging and documentation gaps")
    owner = st.text_input("Human review owner", "Revenue cycle lead, patient access supervisor, or operations analyst")
    patient_impact = st.text_area("Patient-centered impact", "Earlier workflow visibility may reduce avoidable delays, confusion, rework, and access friction.", height=110)
    generated = f"""Responsible AI Use Statement for {project_name}\n\nThis portfolio project uses simulated no-PHI data to explore how AI-assisted workflow visibility could support {workflow_area.lower()} operations. It is not intended to replace human review, payer policy interpretation, clinical judgment, coding validation, compliance oversight, or patient communication.\n\nPrimary workflow risk signal monitored:\n{risk_signal}\n\nHuman oversight owner:\n{owner}\n\nPatient-centered impact:\n{patient_impact}\n\nGovernance considerations:\n- Human review is required before operational action.\n- No PHI is used in this prototype.\n- Recommendations must be validated against current policy and workflow rules.\n- Bias, fairness, and access implications should be reviewed.\n- Staff burden and downstream workflow effects should be measured.\n- The purpose is early risk detection, not autonomous decision-making.\n"""
    st.text_area("Generated portfolio section", generated, height=350)
    branded_download("Download portfolio section", generated, "responsible_ai_portfolio_section.txt")
    footer()

elif page == "LinkedIn Post Generator":
    st.markdown("<div class='section-title'>LinkedIn Post Generator</div>", unsafe_allow_html=True)
    angle = st.selectbox("Post angle", ["Responsible AI", "Strategic Foresight", "AI Governance", "Operational Sustainability", "Systemic Risk", "Long-Term Value"])
    focus = st.text_input("Healthcare focus area", "revenue cycle, prior authorization, patient access, and denial prevention")
    post = f"""One thing I am learning about {angle.lower()} in healthcare operations is that AI should not be measured by speed alone.\n\nIn {focus}, the real question is not only whether a tool can automate a task.\n\nThe better question is whether it helps teams see workflow risk earlier, protect human judgment, reduce avoidable administrative burden, support patient access, and create more accountable operations.\n\nA faster workflow is not always a better workflow.\n\nA responsible workflow is one that is visible, governed, measurable, and sustainable over time.\n\nFrom a patient-to-professional perspective, I believe healthcare AI should support trust, safety, communication, documentation quality, and workflow reliability — not just efficiency.\n\n#HealthcareOperations #ResponsibleAI #RevenueCycleManagement #PatientAccess #PriorAuthorization #DenialPrevention #HealthInformatics #WorkflowIntelligence #HealthcareAdministration #OperationalExcellence"""
    st.text_area("Generated LinkedIn post", post, height=360)
    branded_download("Download LinkedIn post", post, "responsible_ai_linkedin_post.txt")
    footer()

elif page == "Capstone Export":
    st.markdown("<div class='section-title'>Capstone Export</div>", unsafe_allow_html=True)
    title = st.text_input("Framework title", "Responsible AI Healthcare Operations Framework")
    focus = st.text_area("Framework focus", "Workflow intelligence, patient access, revenue cycle visibility, denial prevention, health informatics, human oversight, and long-term operational sustainability.")
    capstone = f"""{title}\nCreated by Kori Pickle\nDate: {date.today().isoformat()}\n\nPurpose\nThis framework explains how responsible AI can support healthcare operations without replacing human judgment or ignoring patient impact.\n\nFocus\n{focus}\n\nCore Principle\nResponsible AI in healthcare operations should not only make workflows faster. It should make them safer, more visible, more accountable, and more sustainable for patients, staff, and the organization.\n\nFramework Pillars\n1. Responsible AI Foundations: AI must be useful, safe, privacy-conscious, monitored, fair, and human-guided.\n2. Operational Sustainability: AI should support workflow reliability, staff capacity, patient trust, and long-term process stability.\n3. Strategic Foresight: Teams should monitor early workflow signals before problems become denials, delays, harm, or burnout.\n4. Systemic Risk Assessment: One upstream defect can spread across patient access, prior authorization, documentation, billing, denials, A/R, and patient experience.\n5. Ethical Governance: AI-supported workflows require human oversight, accountability, PHI protection, auditability, bias review, and policy validation.\n6. Responsible Innovation: Healthcare teams should define the real workflow problem before applying AI.\n7. Long-Term Value Creation: Success should be measured through patient, staff, compliance, quality, operational, and financial outcomes.\n\nProfessional Positioning Statement\nFrom a patient-to-professional perspective, responsible AI cannot only be measured by automation speed or cost reduction. It must also be measured by trust, safety, access, communication, documentation quality, workflow reliability, and human accountability.\n"""
    st.text_area("Capstone framework", capstone, height=520)
    branded_download("Download capstone", capstone, "responsible_ai_healthcare_operations_framework.txt")
    footer()

elif page == "Progress Dashboard":
    st.markdown("<div class='section-title'>Progress Dashboard</div>", unsafe_allow_html=True)
    progress_metrics()
    st.markdown("### Completed modules")
    if st.session_state.completed_modules:
        st.write(pd.DataFrame({"Completed Module": sorted(list(st.session_state.completed_modules))}))
    else:
        st.info("No modules marked complete yet.")
    st.markdown("### Saved reflections")
    if st.session_state.saved_reflections:
        st.write(pd.DataFrame(st.session_state.saved_reflections))
        combined = "\n\n".join([f"{r['module']}\n{r['reflection']}" for r in st.session_state.saved_reflections])
        branded_download("Download all reflections", combined, "kori_responsible_ai_reflections.txt")
    else:
        st.info("No saved reflections yet.")
    footer()
