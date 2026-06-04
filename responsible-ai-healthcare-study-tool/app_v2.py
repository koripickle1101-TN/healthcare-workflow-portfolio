import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(
    page_title="Responsible AI Healthcare Operations Intelligence",
    page_icon="🟧",
    layout="wide",
    initial_sidebar_state="expanded",
)

ORANGE = "#FF8200"
BLACK = "#000000"
WHITE = "#FFFFFF"
WARM = "#E8E3DC"
SOFT = "#F7F4EF"
CHARCOAL = "#151515"

HASHTAGS = "#HealthcareOperations #ResponsibleAI #RevenueCycleManagement #PatientAccess #PriorAuthorization #DenialPrevention #HealthInformatics #WorkflowIntelligence #HealthcareAdministration #OperationalExcellence"

BRAND_IDENTITY = """HEALTHCARE OPERATIONS INTELLIGENCE
Created by Kori Pickle

Brand Identity:
White background: #FFFFFF
Tennessee Orange accent: #FF8200
Black typography: #000000
Editorial serif headlines
Clean sans-serif supporting text
Double-ring workflow nodes
Dotted or fading connector lines
40–50% whitespace for premium readability
Minimal LinkedIn and GitHub footer icons

Use Case:
No-PHI healthcare operations portfolio artifact focused on workflow intelligence, responsible AI, governance, and patient-centered operational sustainability.
"""

VISUAL_DIRECTIONS = """Visual Layout Direction:
Top-left label: HEALTHCARE OPERATIONS INTELLIGENCE
Thin Tennessee Orange #FF8200 divider line beneath header
High-contrast editorial serif headline
Clean sans-serif body copy
White background with warm gray structure lines
Tennessee Orange accent line on key callout boxes
Double-ring circular workflow nodes
Dotted or fading connector lines between stages
Large whitespace for executive readability
Footer: Created by Kori Pickle
Signature: Kori Pickle in elegant feminine cursive, black/dark gray ink
Minimal LinkedIn and GitHub icons below signature
"""

NO_PHI = """No-PHI Disclaimer:
This artifact uses simulated, educational, no-PHI content only. It does not include patient-identifiable information, confidential payer data, proprietary organizational data, or clinical decision-making instructions.
"""

FOOTER_TEXT = """Created by Kori Pickle
Kori Pickle
LinkedIn | GitHub
"""

st.markdown(
    f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Playfair+Display:wght@700;800;900&family=Allura&family=Great+Vibes&display=swap');

html, body, [class*='css'] {{
    font-family:'Inter', sans-serif;
    color:{BLACK};
}}

.stApp {{
    background:
        radial-gradient(circle at 92% 4%, rgba(255,130,0,.12), transparent 26%),
        radial-gradient(circle at 8% 18%, rgba(255,130,0,.055), transparent 22%),
        linear-gradient(180deg,#FFFFFF 0%,#FFFFFF 68%,#FBF8F3 100%);
}}

section[data-testid='stSidebar'] {{
    background:#FFFFFF;
    border-right:1px solid {WARM};
}}

.block-container {{
    max-width:1240px;
    padding-top:1.35rem;
    padding-bottom:2.4rem;
}}

h1,h2,h3,.serif {{
    font-family:'Playfair Display',serif!important;
}}

.brand-lockup {{
    border:1px solid {WARM};
    border-radius:34px;
    background:#fff;
    padding:34px 38px 30px;
    margin-bottom:28px;
    box-shadow:0 24px 64px rgba(0,0,0,.055);
    position:relative;
    overflow:hidden;
}}
.brand-lockup:before {{
    content:'';
    position:absolute;
    left:48px;
    right:48px;
    top:112px;
    height:2px;
    background:linear-gradient(90deg, rgba(255,130,0,.05), {ORANGE}, rgba(255,130,0,.05));
}}
.brand-signature {{
    font-family:'Allura','Great Vibes',cursive;
    font-size:86px;
    line-height:.86;
    color:#111;
    letter-spacing:.5px;
    text-align:center;
    margin:0 auto 26px;
    transform:rotate(-1.2deg);
    text-shadow:.35px .35px 0 rgba(0,0,0,.22);
}}
.brand-node-row {{
    display:flex;
    align-items:center;
    justify-content:center;
    gap:18px;
    margin:6px 0 18px;
}}
.brand-line {{
    height:2px;
    flex:1;
    max-width:360px;
    background:linear-gradient(90deg, rgba(255,130,0,.12), {ORANGE});
}}
.brand-line.right {{
    background:linear-gradient(90deg, {ORANGE}, rgba(255,130,0,.12));
}}
.brand-mark {{
    width:102px;
    height:102px;
    border:7px solid {ORANGE};
    border-radius:999px;
    box-shadow:0 0 0 12px rgba(255,130,0,.07), 0 0 42px rgba(255,130,0,.22);
    position:relative;
    background:#fff;
}}
.brand-mark:before {{
    content:'';
    position:absolute;
    inset:16px;
    border:7px solid {ORANGE};
    border-radius:999px;
}}
.brand-mark:after {{
    content:'';
    position:absolute;
    right:-70px;
    top:39px;
    width:61px;
    height:7px;
    background:{ORANGE};
    box-shadow:52px 0 0 -19px #fff, 52px 0 0 -12px {ORANGE};
}}
.brand-kicker {{
    text-align:center;
    font-size:28px;
    letter-spacing:13px;
    text-transform:uppercase;
    font-weight:600;
    margin-top:18px;
}}
.brand-intel {{
    text-align:center;
    font-size:42px;
    letter-spacing:18px;
    text-transform:uppercase;
    color:{ORANGE};
    font-weight:800;
    line-height:1.1;
}}
.brand-bottom-line {{
    height:2px;
    width:78%;
    margin:18px auto 0;
    background:linear-gradient(90deg, transparent, {ORANGE}, transparent);
}}

.hero {{
    min-height:475px;
    padding:58px 58px 48px;
    border:1px solid {WARM};
    border-radius:36px;
    background:linear-gradient(135deg,#fff 0%,#fff 64%,rgba(255,130,0,.095) 100%);
    box-shadow:0 28px 78px rgba(0,0,0,.07);
    position:relative;
    overflow:hidden;
    margin-bottom:30px;
}}
.hero:before {{
    content:'';
    position:absolute;
    top:40px;
    right:46px;
    width:190px;
    height:190px;
    border:1px dashed rgba(255,130,0,.42);
    border-radius:999px;
}}
.hero:after {{
    content:'';
    position:absolute;
    right:-90px;
    bottom:-120px;
    width:320px;
    height:320px;
    border-radius:999px;
    border:1px solid rgba(255,130,0,.18);
}}
.eyebrow {{
    font-size:12px;
    letter-spacing:3.1px;
    text-transform:uppercase;
    font-weight:900;
    display:inline-block;
    padding-bottom:8px;
    border-bottom:2px solid {ORANGE};
    margin-bottom:24px;
}}
.hero h1 {{
    font-size:clamp(48px,6.8vw,96px);
    line-height:.88;
    letter-spacing:-2.7px;
    margin:0 0 28px;
    max-width:1000px;
}}
.hero p {{
    max-width:900px;
    font-size:18px;
    line-height:1.72;
    color:#242424;
}}
.orange {{ color:{ORANGE}; }}
.node-row {{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin-top:34px;}}
.node {{
    width:64px;height:64px;border-radius:999px;border:2px solid {ORANGE};
    display:flex;align-items:center;justify-content:center;background:#fff;color:{ORANGE};font-weight:900;
    box-shadow:0 0 0 10px rgba(255,130,0,.07),0 0 34px rgba(255,130,0,.23);
}}
.connector {{width:78px;height:2px;background-image:linear-gradient(to right,rgba(255,130,0,.85) 45%,rgba(255,130,0,0) 0%);background-size:13px 2px;background-repeat:repeat-x;}}
.card {{
    border:1px solid {WARM};
    border-radius:26px;
    padding:26px;
    background:#fff;
    box-shadow:0 18px 48px rgba(0,0,0,.05);
    height:100%;
}}
.card.accent {{ border-top:5px solid {ORANGE}; }}
.card h3 {{font-size:30px;line-height:1.05;margin:0 0 12px;}}
.subtle,.card p {{color:#464646;line-height:1.68;font-size:16px;}}
.metric {{border:1px solid {WARM};border-left:5px solid {ORANGE};border-radius:22px;background:{SOFT};padding:24px;min-height:138px;}}
.big {{font-family:'Playfair Display',serif;font-size:48px;font-weight:900;line-height:.9;}}
.label {{font-size:12px;font-weight:900;letter-spacing:1.4px;text-transform:uppercase;margin-top:12px;color:#555;}}
.section-title {{font-family:'Playfair Display',serif;font-size:46px;line-height:.98;letter-spacing:-1px;margin:42px 0 16px;}}
.pill {{display:inline-block;border:1px solid {ORANGE};background:rgba(255,130,0,.08);border-radius:999px;padding:8px 13px;margin:4px 5px 4px 0;font-size:12px;font-weight:900;letter-spacing:.55px;text-transform:uppercase;}}
.callout {{border:1px solid {WARM};border-left:6px solid {ORANGE};border-radius:24px;padding:24px 28px;background:#fff;box-shadow:0 18px 44px rgba(0,0,0,.045);margin:18px 0;}}
.signature {{
    font-family:'Allura','Great Vibes',cursive;
    font-size:48px;
    color:#151515;
    display:inline-block;
    transform:rotate(-1.1deg);
    margin-top:6px;
    text-shadow:.3px .3px 0 rgba(0,0,0,.20);
}}
.footer {{text-align:center;border-top:1px solid {WARM};margin-top:56px;padding:34px 0 18px;}}
.icons {{display:flex;gap:12px;justify-content:center;margin-top:12px;}}
.icon-circle {{width:31px;height:31px;border-radius:999px;border:1px solid {WARM};display:inline-flex;align-items:center;justify-content:center;background:#fff;font-size:12px;font-weight:900;}}
.sidebar-logo {{
    text-align:center;
    border:1px solid {WARM};
    border-radius:24px;
    padding:18px 12px;
    background:linear-gradient(180deg,#fff,rgba(255,130,0,.045));
    margin-bottom:18px;
}}
.sidebar-signature {{
    font-family:'Allura',cursive;
    font-size:44px;
    line-height:.85;
    color:#111;
}}
.sidebar-title {{font-size:11px;letter-spacing:2.2px;text-transform:uppercase;font-weight:900;margin-top:10px;}}
div.stButton>button,div.stDownloadButton>button{{border-radius:999px;border:1px solid {ORANGE};background:{ORANGE};color:white;font-weight:900;padding:.72rem 1.15rem;}}
div.stButton>button:hover,div.stDownloadButton>button:hover{{background:#111;border:1px solid #111;color:white;}}
textarea,input{{border-radius:16px!important;}}
@media(max-width:760px){{
  .brand-signature{{font-size:62px;}}
  .brand-kicker{{font-size:17px;letter-spacing:7px;}}
  .brand-intel{{font-size:26px;letter-spacing:10px;}}
  .brand-mark{{width:76px;height:76px;border-width:6px;}}
  .brand-mark:before{{inset:12px;border-width:6px;}}
  .brand-mark:after{{display:none;}}
  .hero{{padding:38px 28px;}}
}}
</style>
""",
    unsafe_allow_html=True,
)

MODULES = {
    "Responsible AI Foundations": ["AI", "Useful · Safe · Human-Guided", "AI should support people, not replace judgment or hide accountability.", "A prior authorization risk flag is useful only when staff can review the reason, confirm payer policy, and act safely."],
    "Operational Sustainability": ["OS", "Stability · Capacity · Trust", "A workflow is sustainable when it can function reliably over time without creating hidden burden.", "A faster claims process is not sustainable if it creates confusing exception queues and staff rework."],
    "Strategic Foresight": ["SF", "Early Signals · Prevention", "Foresight means detecting weak signals before denials, delays, complaints, or burnout appear.", "Authorization aging, repeated payer requests, and documentation gaps can warn teams before a denial occurs."],
    "Systemic Risk": ["SR", "Cause Chain · Downstream Damage", "Systemic risk spreads across connected workflows instead of staying in one department.", "Wrong insurance information can trigger eligibility failure, authorization delay, denial, A/R rework, and patient confusion."],
    "Ethical Governance": ["EG", "Oversight · Accountability · Privacy", "Governance defines who reviews, validates, audits, and owns AI-supported workflow decisions.", "A denial-risk score needs no-PHI safeguards, human review, audit trail, bias review, and clear escalation ownership."],
    "Responsible Innovation": ["RI", "Problem First · AI Second", "Responsible innovation starts with the workflow problem, not the tool trend.", "Before adding AI to patient access, define whether the real issue is intake data, eligibility accuracy, authorization aging, or handoff clarity."],
    "Long-Term Value": ["LV", "Beyond Speed · Beyond Cost", "Value must include trust, safety, staff capacity, quality, access, compliance, and financial stability.", "A faster workflow is not valuable if it creates appeals, confusion, complaints, or compliance risk later."],
    "Capstone Framework": ["CF", "Responsible AI Healthcare Operations", "The capstone connects responsible AI, sustainability, foresight, systemic risk, governance, innovation, and long-term value.", "A no-PHI RCM dashboard should explain purpose, limits, risk signals, oversight, and governance boundaries."],
}

FLASHCARDS = [
    ("Responsible AI", "AI that is useful, safe, monitored, privacy-conscious, fair, and designed to support human decision-making."),
    ("Operational Sustainability", "The ability of a healthcare workflow to remain reliable, manageable, and effective over time."),
    ("Strategic Foresight", "Identifying early signals and future risks before they become costly or harmful."),
    ("Systemic Risk", "A risk that spreads through connected workflows instead of staying isolated."),
    ("Ethical Governance", "Rules, oversight, accountability, auditability, and correction processes for responsible AI use."),
    ("No-PHI Prototype", "A portfolio tool that uses simulated data only and avoids patient-identifiable information."),
]

QUIZ = [
    ("Responsible AI in healthcare operations should primarily:", ["Replace staff judgment", "Support safer, clearer, more accountable workflows", "Remove compliance review"], "Support safer, clearer, more accountable workflows"),
    ("Best example of a leading indicator:", ["Final denial", "Authorization aging past threshold", "Monthly report after close"], "Authorization aging past threshold"),
    ("Systemic risk means:", ["A workflow issue can spread across connected processes", "Only finance is affected", "No operational impact"], "A workflow issue can spread across connected processes"),
    ("Strongest governance question:", ["Can AI sound confident?", "Who reviews, validates, audits, and remains accountable?", "Can AI replace managers?"], "Who reviews, validates, audits, and remains accountable?"),
    ("No-PHI means:", ["No financial data", "No patient-identifiable health information", "No healthcare examples"], "No patient-identifiable health information"),
]

SCENARIOS = {
    "Prior Authorization Delay": "Orthopedic authorization turnaround time is increasing. Risk signals include authorization aging, repeated payer requests, missing documentation, and unclear escalation ownership.",
    "Eligibility Verification Breakdown": "Insurance mismatches are discovered after service. Risk signals include registration gaps, COB uncertainty, and downstream claim correction.",
    "Denial Spike": "Medical necessity and authorization denials increased after a payer policy shift. Risk signals include denial trend spikes, appeal backlog, and A/R aging.",
    "Healthcare Staffing Friction": "Recruiters spend more time on compliance checks, follow-ups, and scheduling friction than candidate engagement. Risk signals include slow placement and workload imbalance.",
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
    "Documents what AI should not decide",
]

if "completed" not in st.session_state:
    st.session_state.completed = set()
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "reflections" not in st.session_state:
    st.session_state.reflections = []

def footer():
    st.markdown("""
    <div class='footer'>
      <div style='font-weight:900; letter-spacing:.5px;'>Created by Kori Pickle</div>
      <div class='signature'>Kori Pickle</div>
      <div class='icons'><span class='icon-circle'>in</span><span class='icon-circle'>GH</span></div>
    </div>
    """, unsafe_allow_html=True)

def brand_lockup():
    st.markdown("""
    <div class='brand-lockup'>
      <div class='brand-signature'>Kori Pickle</div>
      <div class='brand-node-row'>
        <div class='brand-line'></div>
        <div class='brand-mark'></div>
        <div class='brand-line right'></div>
      </div>
      <div class='brand-kicker'>Healthcare Operations</div>
      <div class='brand-intel'>Intelligence</div>
      <div class='brand-bottom-line'></div>
    </div>
    """, unsafe_allow_html=True)

def branded_export(title, artifact_type, body, caption=""):
    text = f"""{BRAND_IDENTITY}

{title}
Portfolio Artifact Type:
{artifact_type}

{NO_PHI}

{body.strip()}

{VISUAL_DIRECTIONS}
"""
    if caption:
        text += f"\nLinkedIn-Ready Caption:\n{caption}\n\n{HASHTAGS}\n"
    text += f"\n{FOOTER_TEXT}"
    return text

def download(label, text, filename):
    st.download_button(label, text, file_name=filename, mime="text/plain")

def metrics():
    a, b, c, d = st.columns(4)
    a.markdown(f"<div class='metric'><div class='big'>{len(st.session_state.completed)}/8</div><div class='label'>Modules Complete</div></div>", unsafe_allow_html=True)
    b.markdown(f"<div class='metric'><div class='big'>{st.session_state.quiz_score}</div><div class='label'>Latest Quiz Score</div></div>", unsafe_allow_html=True)
    c.markdown(f"<div class='metric'><div class='big'>{len(st.session_state.reflections)}</div><div class='label'>Saved Reflections</div></div>", unsafe_allow_html=True)
    d.markdown("<div class='metric'><div class='big'>No</div><div class='label'>PHI Used</div></div>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div class='sidebar-logo'>
      <div class='sidebar-signature'>Kori Pickle</div>
      <div class='sidebar-title'>Healthcare Operations Intelligence</div>
    </div>
    """, unsafe_allow_html=True)
    st.caption("Responsible AI · Workflow Intelligence · Governance")
    page = st.radio(
        "Choose a study mode",
        ["Executive Home", "8-Module Study Path", "Flashcards", "Scenario Lab", "Quiz Bank", "Governance Checklist", "Risk Scorecard", "Portfolio Builder", "LinkedIn Post Generator", "Capstone Export", "Progress Dashboard"],
    )
    st.divider()
    st.markdown("**Brand System**")
    st.markdown("<span class='pill'>White #FFFFFF</span><span class='pill'>Vols Orange #FF8200</span><span class='pill'>Black Typography</span>", unsafe_allow_html=True)
    st.caption("Every generator exports brand-locked Kori Pickle | Healthcare Operations Intelligence content.")

if page == "Executive Home":
    brand_lockup()
    st.markdown("""
    <div class='hero'>
      <div class='eyebrow'>Responsible AI for Healthcare Operations</div>
      <h1>Build AI governance judgment through a <span class='orange'>workflow intelligence</span> lens.</h1>
      <p>This premium interactive study tool teaches responsible AI, operational sustainability, strategic foresight, systemic risk, ethical governance, responsible innovation, and long-term value creation using healthcare operations examples.</p>
      <div class='node-row'><div class='node'>AI</div><div class='connector'></div><div class='node'>RCM</div><div class='connector'></div><div class='node'>PA</div><div class='connector'></div><div class='node'>HIM</div><div class='connector'></div><div class='node'>QI</div></div>
    </div>
    """, unsafe_allow_html=True)
    metrics()
    st.markdown("<div class='section-title'>What this tool helps you practice</div>", unsafe_allow_html=True)
    c1, c2 = st.columns([1.2, .8])
    with c1:
        st.markdown("""
        <div class='card accent'>
          <h3>From AI hype to healthcare operations judgment</h3>
          <p class='subtle'>This tool helps you explain AI responsibly in healthcare operations. The focus is governance, workflow risk, patient impact, staff capacity, compliance, and long-term operational value.</p>
          <span class='pill'>Revenue Cycle</span><span class='pill'>Patient Access</span><span class='pill'>Prior Authorization</span><span class='pill'>Denial Prevention</span><span class='pill'>Health Informatics</span>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class='callout'>
          <strong>Core professional sentence:</strong><br><br>
          Responsible AI in healthcare operations should not only make workflows faster. It should make them safer, more visible, more accountable, and more sustainable for patients, staff, and the organization.
        </div>
        """, unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Learning architecture</div>", unsafe_allow_html=True)
    cols = st.columns(4)
    for i, (name, data) in enumerate(list(MODULES.items())[:4], start=1):
        with cols[i - 1]:
            st.markdown(f"<div class='card'><div class='node'>{data[0]}</div><h3>{i}. {name}</h3><span class='pill'>{data[1]}</span><p class='subtle'>{data[2]}</p></div>", unsafe_allow_html=True)
    cols = st.columns(4)
    for j, (name, data) in enumerate(list(MODULES.items())[4:], start=5):
        with cols[j - 5]:
            st.markdown(f"<div class='card'><div class='node'>{data[0]}</div><h3>{j}. {name}</h3><span class='pill'>{data[1]}</span><p class='subtle'>{data[2]}</p></div>", unsafe_allow_html=True)
    footer()

elif page == "8-Module Study Path":
    brand_lockup()
    st.markdown("<div class='section-title'>8-Module Study Path</div>", unsafe_allow_html=True)
    name = st.selectbox("Select a module", list(MODULES.keys()))
    data = MODULES[name]
    st.markdown(f"<div class='card accent'><div class='node'>{data[0]}</div><h3>{name}</h3><span class='pill'>{data[1]}</span><p class='subtle'>{data[2]}</p><p class='subtle'><strong>Healthcare example:</strong> {data[3]}</p></div>", unsafe_allow_html=True)
    reflection = st.text_area("Reflection prompt: How does this concept apply to revenue cycle, patient access, prior authorization, HIM, denial prevention, or staffing operations?", height=180)
    if st.button("Mark module complete"):
        st.session_state.completed.add(name)
        st.success("Module marked complete.")
    if reflection:
        if st.button("Save reflection"):
            st.session_state.reflections.append({"module": name, "reflection": reflection})
            st.success("Reflection saved.")
        output = branded_export(f"{name} Reflection", "Responsible AI Learning Reflection", f"Module: {name}\n\nReflection:\n{reflection}", f"I am studying {name.lower()} through a healthcare operations and responsible AI lens. The goal is to connect AI governance with workflow visibility, patient trust, and operational sustainability.")
        st.text_area("Brand-locked export", output, height=360)
        download("Download branded reflection", output, f"{name.lower().replace(' ','_')}_brand_locked_reflection.txt")
    footer()

elif page == "Flashcards":
    brand_lockup()
    st.markdown("<div class='section-title'>Interactive Flashcards</div>", unsafe_allow_html=True)
    term, definition = FLASHCARDS[st.slider("Choose a flashcard", 1, len(FLASHCARDS), 1) - 1]
    st.markdown(f"<div class='card accent'><h3>{term}</h3><p class='subtle'>{definition}</p></div>", unsafe_allow_html=True)
    example = st.text_area("Translate this term into a healthcare operations example.", height=150)
    if example:
        output = branded_export(f"{term} Study Note", "Healthcare Operations Flashcard Translation", f"Term: {term}\nDefinition: {definition}\nHealthcare Operations Example:\n{example}", f"A concept I am studying in responsible AI for healthcare operations is {term}. I am connecting it to workflow visibility, governance, and patient-centered operational sustainability.")
        download("Download branded flashcard note", output, f"{term.lower().replace(' ','_')}_brand_locked_note.txt")
    footer()

elif page == "Scenario Lab":
    brand_lockup()
    st.markdown("<div class='section-title'>Scenario Lab</div>", unsafe_allow_html=True)
    scenario = st.selectbox("Choose a scenario", list(SCENARIOS.keys()))
    st.info(SCENARIOS[scenario])
    root = st.text_input("Likely root workflow issue")
    owner = st.text_input("Human owner / accountable role")
    action = st.text_area("Immediate containment action", height=100)
    kpi = st.text_input("KPI to monitor")
    if root or owner or action or kpi:
        body = f"Scenario: {scenario}\nSummary: {SCENARIOS[scenario]}\n\nLikely Root Workflow Issue:\n{root}\n\nHuman Owner / Accountable Role:\n{owner}\n\nImmediate Containment Action:\n{action}\n\nKPI to Monitor:\n{kpi}\n\nResponsible AI Boundary:\nAI may support early risk visibility, but human review must own validation, escalation, communication, compliance, and operational action."
        output = branded_export(f"{scenario} Scenario Analysis", "No-PHI Healthcare Operations Scenario Note", body, f"I analyzed a simulated {scenario.lower()} scenario through a responsible AI and healthcare workflow intelligence lens. The goal is earlier visibility, clearer ownership, and safer operational response.")
        st.text_area("Generated brand-locked scenario note", output, height=420)
        download("Download branded scenario note", output, f"{scenario.lower().replace(' ','_')}_brand_locked_scenario.txt")
    footer()

elif page == "Quiz Bank":
    brand_lockup()
    st.markdown("<div class='section-title'>Quiz Bank</div>", unsafe_allow_html=True)
    score = 0
    answers = []
    for i, (q, opts, ans) in enumerate(QUIZ, start=1):
        choice = st.radio(q, opts, key=f"q{i}")
        correct = choice == ans
        score += int(correct)
        answers.append((q, choice, ans, correct))
    if st.button("Grade quiz"):
        st.session_state.quiz_score = score
        st.progress(score / len(QUIZ))
        st.subheader(f"Score: {score}/{len(QUIZ)}")
        report = "\n".join([f"Question: {q}\nYour answer: {c}\nCorrect answer: {a}\nResult: {'Correct' if ok else 'Review needed'}\n" for q, c, a, ok in answers])
        output = branded_export("Responsible AI Healthcare Operations Quiz Report", "Study Progress Artifact", f"Quiz Score: {score}/{len(QUIZ)}\n\n{report}", "I completed a responsible AI healthcare operations knowledge check focused on governance, workflow intelligence, systemic risk, and no-PHI portfolio thinking.")
        download("Download branded quiz report", output, "brand_locked_quiz_report.txt")
    footer()

elif page == "Governance Checklist":
    brand_lockup()
    st.markdown("<div class='section-title'>Responsible AI Governance Checklist</div>", unsafe_allow_html=True)
    completed = [item for item in GOVERNANCE_ITEMS if st.checkbox(item)]
    pct = len(completed) / len(GOVERNANCE_ITEMS)
    st.progress(pct)
    st.subheader(f"Governance readiness: {len(completed)}/{len(GOVERNANCE_ITEMS)}")
    verdict = "Strong governance foundation." if pct >= .85 else "Partial governance foundation. Strengthen the unchecked items." if pct >= .55 else "High governance risk. Add oversight, accountability, privacy, and measurement."
    st.info(verdict)
    body = "Governance Checklist Results:\n\n" + "\n".join([f"[{'x' if i in completed else ' '}] {i}" for i in GOVERNANCE_ITEMS]) + f"\n\nReadiness Verdict:\n{verdict}"
    output = branded_export("Responsible AI Governance Checklist", "Brand-Locked Governance Evaluation", body, "A responsible AI healthcare workflow needs human oversight, no-PHI safeguards, auditability, fairness review, escalation logic, and long-term value measurement.")
    st.text_area("Brand-locked checklist export", output, height=320)
    download("Download branded checklist", output, "brand_locked_governance_checklist.txt")
    footer()

elif page == "Risk Scorecard":
    brand_lockup()
    st.markdown("<div class='section-title'>AI Workflow Risk Scorecard</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        privacy = st.slider("Privacy / PHI protection", 0, 5, 3)
        oversight = st.slider("Human oversight clarity", 0, 5, 3)
        explain = st.slider("Explainability / reason visibility", 0, 5, 3)
    with c2:
        fairness = st.slider("Bias and fairness review", 0, 5, 3)
        fit = st.slider("Workflow fit", 0, 5, 3)
        measure = st.slider("Success measurement plan", 0, 5, 3)
    total = privacy + oversight + explain + fairness + fit + measure
    verdict = "Strong readiness" if total >= 25 else "Moderate readiness" if total >= 17 else "High risk"
    st.markdown(f"<div class='metric'><div class='big'>{total}/30</div><div class='label'>Responsible AI Readiness Score</div></div>", unsafe_allow_html=True)
    st.info(verdict)
    body = f"Score: {total}/30\nPrivacy / PHI protection: {privacy}/5\nHuman oversight clarity: {oversight}/5\nExplainability: {explain}/5\nBias and fairness review: {fairness}/5\nWorkflow fit: {fit}/5\nMeasurement plan: {measure}/5\nVerdict: {verdict}"
    output = branded_export("AI Workflow Risk Scorecard", "Brand-Locked Responsible AI Readiness Report", body, "A healthcare AI workflow should be scored before it is trusted. Privacy, oversight, explainability, fairness, workflow fit, and measurement all matter.")
    download("Download branded risk scorecard", output, "brand_locked_risk_scorecard.txt")
    footer()

elif page == "Portfolio Builder":
    brand_lockup()
    st.markdown("<div class='section-title'>Portfolio Builder</div>", unsafe_allow_html=True)
    project = st.text_input("Project name", "AI-Assisted Revenue Cycle Workflow System")
    area = st.selectbox("Workflow area", ["Revenue Cycle", "Prior Authorization", "Patient Access", "Eligibility Verification", "Denial Prevention", "Health Informatics", "Healthcare Staffing", "Documentation Quality"])
    signal = st.text_input("Primary workflow risk signal", "Authorization aging and documentation gaps")
    owner = st.text_input("Human review owner", "Revenue cycle lead, patient access supervisor, or operations analyst")
    impact = st.text_area("Patient-centered impact", "Earlier workflow visibility may reduce avoidable delays, confusion, rework, and access friction.")
    body = f"""Responsible AI Use Statement:
This no-PHI healthcare operations portfolio artifact uses simulated data to explore how AI-assisted workflow visibility can support {area.lower()} operations.

Responsible AI Boundary:
This tool does not replace human review, payer policy interpretation, clinical judgment, coding validation, compliance oversight, or patient communication.

Purpose:
To demonstrate how early workflow risk signals can support better operational awareness, stronger governance, and earlier intervention before downstream disruption occurs.

Primary Workflow Risk Signal:
{signal}

Human Oversight Owner:
{owner}

Patient-Centered Impact:
{impact}

Governance Considerations:
- Human review is required before operational action.
- No PHI is used in this prototype.
- Recommendations must be validated against current policy and workflow rules.
- Bias, fairness, and access implications should be reviewed.
- Staff burden and downstream workflow effects should be measured.
- The purpose is early risk detection, not autonomous decision-making.
"""
    caption = f"I created a no-PHI healthcare operations portfolio artifact focused on {area.lower()}, responsible AI, workflow visibility, and patient-centered operational sustainability."
    output = branded_export(project, "Brand-Locked Healthcare Operations Portfolio Artifact", body, caption)
    st.text_area("Generated brand-locked portfolio artifact", output, height=520)
    download("Download brand-locked portfolio artifact", output, "brand_locked_portfolio_artifact.txt")
    footer()

elif page == "LinkedIn Post Generator":
    brand_lockup()
    st.markdown("<div class='section-title'>LinkedIn Post Generator</div>", unsafe_allow_html=True)
    angle = st.selectbox("Post angle", ["Responsible AI", "Strategic Foresight", "AI Governance", "Operational Sustainability", "Systemic Risk", "Long-Term Value"])
    focus = st.text_input("Healthcare focus area", "revenue cycle, prior authorization, patient access, and denial prevention")
    post = f"""HEALTHCARE OPERATIONS INTELLIGENCE

One thing I am learning about {angle.lower()} in healthcare operations is that AI should not be measured by speed alone.

In {focus}, the real question is not only whether a tool can automate a task.

The better question is whether it helps teams see workflow risk earlier, protect human judgment, reduce avoidable administrative burden, support patient access, and create more accountable operations.

A faster workflow is not always a better workflow.

A responsible workflow is one that is visible, governed, measurable, and sustainable over time.

From a patient-to-professional perspective, I believe healthcare AI should support trust, safety, communication, documentation quality, and workflow reliability — not just efficiency.

Portfolio positioning:
This connects to my no-PHI Healthcare Operations Intelligence portfolio, where I am building simulated workflow tools around revenue cycle visibility, patient access, prior authorization, denial prevention, health informatics, and responsible AI governance.

Created by Kori Pickle

{HASHTAGS}
"""
    visual = f"Carousel / Visual Direction:\n{VISUAL_DIRECTIONS}\nSuggested Slide Headline:\nAI should not only make healthcare workflows faster. It should make them safer, more visible, and more accountable.\n\nFooter:\n{FOOTER_TEXT}"
    st.text_area("Generated brand-locked LinkedIn post", post, height=430)
    st.text_area("Generated visual directions", visual, height=260)
    download("Download LinkedIn post", post, "brand_locked_linkedin_post.txt")
    download("Download visual directions", visual, "brand_locked_visual_directions.txt")
    footer()

elif page == "Capstone Export":
    brand_lockup()
    st.markdown("<div class='section-title'>Capstone Export</div>", unsafe_allow_html=True)
    title = st.text_input("Framework title", "Responsible AI Healthcare Operations Framework")
    focus = st.text_area("Framework focus", "Workflow intelligence, patient access, revenue cycle visibility, denial prevention, health informatics, human oversight, and long-term operational sustainability.")
    body = f"""Executive Summary:
This framework explains how responsible AI can support healthcare operations without replacing human judgment or ignoring patient impact.

Framework Focus:
{focus}

Core Principle:
Responsible AI in healthcare operations should not only make workflows faster. It should make them safer, more visible, more accountable, and more sustainable for patients, staff, and the organization.

Framework Pillars:
1. Responsible AI Foundations
2. Operational Sustainability
3. Strategic Foresight
4. Systemic Risk Assessment
5. Ethical Governance
6. Responsible Innovation
7. Long-Term Value Creation

Professional Positioning Statement:
From a patient-to-professional perspective, responsible AI cannot only be measured by automation speed or cost reduction. It must also be measured by trust, safety, access, communication, documentation quality, workflow reliability, and human accountability.
"""
    output = branded_export(title, "Complete Brand-Locked Capstone Framework", body, "I built a Responsible AI Healthcare Operations Framework to connect workflow intelligence, governance, systemic risk, and patient-centered operational sustainability.")
    st.text_area("Brand-locked capstone framework", output, height=620)
    download("Download brand-locked capstone", output, "brand_locked_capstone_framework.txt")
    footer()

elif page == "Progress Dashboard":
    brand_lockup()
    st.markdown("<div class='section-title'>Progress Dashboard</div>", unsafe_allow_html=True)
    metrics()
    st.markdown("### Completed modules")
    st.write(pd.DataFrame({"Completed Module": sorted(st.session_state.completed)})) if st.session_state.completed else st.info("No modules marked complete yet.")
    st.markdown("### Saved reflections")
    if st.session_state.reflections:
        st.write(pd.DataFrame(st.session_state.reflections))
        combined = "\n\n".join([f"{r['module']}\n{r['reflection']}" for r in st.session_state.reflections])
        output = branded_export("Responsible AI Study Reflection Bundle", "Brand-Locked Progress Export", combined, "I am building responsible AI healthcare operations knowledge through a workflow intelligence, governance, and no-PHI portfolio lens.")
        download("Download all branded reflections", output, "brand_locked_reflections.txt")
    else:
        st.info("No saved reflections yet.")
    footer()
