const brand={orange:'#FF8200',black:'#000000',white:'#FFFFFF'};

const stages=[
['Patient registration','Capture demographic and insurance details','Is the information complete and internally consistent?'],
['Insurance identification','Confirm the payer and member information to be checked','Are we verifying the correct plan and member?'],
['Eligibility verification','Confirm active coverage status for the relevant date','Is coverage active for the date in question?'],
['Benefit review','Identify relevant benefit information for the planned service','What coverage details affect the next workflow step?'],
['Authorization screening','Determine whether prior authorization may be required','Does the service require another payer control before moving forward?'],
['Exception review','Classify unresolved, conflicting, or missing information','What uncertainty remains and who owns it?'],
['Documentation / handoff','Record the verification result and next action','Can the next person see what was verified, what is unresolved, and what happens next?'],
['Readiness decision','Advance, hold, or escalate the workflow','Is there enough verified information to move forward safely?']
];

const scenarios=[
['Coverage appears inactive','Eligibility verification','Coverage may be inactive, member information may not match, or the wrong payer/plan may have been checked.','Recheck identifying information and classify the unresolved coverage status before advancing.'],
['Member ID does not match','Insurance identification','A mismatch can prevent a reliable eligibility response and create downstream claim or patient-balance confusion.','Validate the member, payer, and plan information before relying on the result.'],
['Eligibility response is incomplete','Eligibility verification / benefit review','An incomplete response may leave unresolved questions about coverage or benefit information.','Document what was confirmed, what remains unclear, and the next verification step.'],
['Authorization requirement is uncertain','Authorization screening','A missed requirement can become a downstream denial or delay.','Identify whether another payer control applies and assign follow-up before claim readiness.'],
['Coverage changed','Patient registration / eligibility verification','Updated coverage may not match information already in the workflow.','Reconcile current payer information before the case proceeds.'],
['Multiple plans are present','Insurance identification / coordination review','The workflow can lose control if payer order or plan selection is unclear.','Flag the ambiguity and route it for appropriate verification rather than guessing.'],
['Benefit information conflicts','Benefit review','Conflicting information can create false confidence about patient responsibility or claim readiness.','Record the conflict and escalate or reverify before downstream use.'],
['Verification is unresolved','Exception review / handoff','Unresolved uncertainty can move downstream when ownership and next action are not explicit.','Assign an owner, next action, and status before the case advances.']
];

const measures=[
['Verification completion rate','Share of simulated cases with all required verification steps completed'],
['Unresolved eligibility count','Number of simulated cases with unresolved coverage questions'],
['Member-information mismatch count','Number of simulated cases with payer/member data inconsistencies'],
['Authorization-screening exception count','Number of simulated cases needing additional authorization review'],
['Reverification count','Number of simulated cases requiring another verification attempt'],
['First-pass classification rate','Whether simulated eligibility exceptions are categorized correctly initially'],
['Exception aging','How long simulated unresolved verification issues remain open'],
['Handoff completeness rate','Whether simulated handoffs include status, owner, next action, and unresolved questions']
];

const kicker={color:brand.orange,fontWeight:900,letterSpacing:'0.2em',textTransform:'uppercase',fontSize:12};
const sectionTitle={fontFamily:'Georgia, Times New Roman, serif',fontSize:'clamp(34px,5vw,58px)',lineHeight:1.02,margin:'8px 0 20px'};
const body={fontSize:17,lineHeight:1.7,maxWidth:850};

export default function EligibilityInsuranceVerificationAnalysis(){
return <main style={{fontFamily:'Arial, Helvetica, sans-serif',background:brand.white,color:brand.black}}>
  <header style={{borderTop:`10px solid ${brand.orange}`,padding:'28px 22px 64px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <a href="/" style={{color:brand.black,textDecoration:'none',fontWeight:900,fontSize:13}}>← Portfolio Home</a>
      <p style={{...kicker,marginTop:42}}>Case Study 02 · Patient Access / Eligibility / Insurance Verification</p>
      <h1 style={{fontFamily:'Georgia, Times New Roman, serif',fontSize:'clamp(46px,8vw,86px)',lineHeight:.96,margin:'14px 0 22px',maxWidth:1000}}>Eligibility & Insurance Verification Analysis</h1>
      <p style={{fontSize:'clamp(20px,3vw,28px)',fontWeight:800,lineHeight:1.35,maxWidth:850}}>A student-developed patient-access workflow case study built around one question: what has to be verified, documented, and resolved before coverage uncertainty becomes a downstream claim or patient-balance problem?</p>
      <div style={{display:'flex',flexWrap:'wrap',gap:10,marginTop:26}}>
        {['Student-developed','Simulated','No PHI','Healthcare Administration Candidate'].map(x=><span key={x} style={{border:`1px solid ${brand.black}`,padding:'9px 12px',fontSize:12,fontWeight:900,textTransform:'uppercase',letterSpacing:'.06em'}}>{x}</span>)}
      </div>
    </div>
  </header>

  <section style={{background:brand.black,color:brand.white,padding:'48px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Core Operations Insight</p>
      <h2 style={{...sectionTitle,color:brand.white}}>Verification Is a Control Point, Not Just a Check</h2>
      <p style={{...body,color:brand.white}}>Eligibility verification does more than confirm whether coverage appears active. It creates a control point for payer identification, member matching, coverage status, benefit information, authorization screening, unresolved exceptions, ownership, and handoff documentation. If uncertainty is allowed to move forward without being classified and owned, the problem may become visible later as rework, delay, denial, or patient-balance confusion.</p>
    </div>
  </section>

  <section style={{padding:'66px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Problem → Workflow</p>
      <h2 style={sectionTitle}>What Must Be Controlled Before Coverage Uncertainty Moves Downstream</h2>
      <p style={body}>This simulated model treats eligibility and insurance verification as a connected patient-access workflow. Each step asks whether the information is complete enough, clear enough, and documented enough for the next action. The goal is not to assume that a coverage response is the end of the process, but to make unresolved uncertainty visible before it becomes a downstream operational problem.</p>
      <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(210px,1fr))',gap:14,marginTop:32}}>
        {stages.map((s,i)=><article key={s[0]} style={{border:`1px solid ${brand.black}`,padding:18}}>
          <p style={{...kicker,margin:0}}>Step {String(i+1).padStart(2,'0')}</p>
          <h3 style={{fontSize:20,margin:'9px 0'}}>{s[0]}</h3>
          <p style={{lineHeight:1.5}}>{s[1]}</p>
          <p style={{fontWeight:900,borderTop:`2px solid ${brand.orange}`,paddingTop:12}}>{s[2]}</p>
        </article>)}
      </div>
    </div>
  </section>

  <section style={{padding:'58px 22px',borderTop:`1px solid ${brand.black}`}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Control Design</p>
      <h2 style={sectionTitle}>Eight Verification Control Gates</h2>
      <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(260px,1fr))',gap:14}}>
        {[
          ['Gate 01 · Registration completeness','Required demographic and insurance information is present before verification begins.'],
          ['Gate 02 · Payer/member match','The payer, plan, member, and identifying information are internally consistent enough to verify.'],
          ['Gate 03 · Coverage status','The simulated eligibility result is classified as active, inactive, uncertain, or unresolved.'],
          ['Gate 04 · Benefit visibility','Relevant benefit information is documented without treating incomplete information as confirmed.'],
          ['Gate 05 · Authorization screening','Possible authorization requirements are identified for follow-up before downstream readiness.'],
          ['Gate 06 · Exception ownership','Conflicts, missing information, and unresolved questions have an owner and next action.'],
          ['Gate 07 · Handoff documentation','The next person can see what was verified, what remains unresolved, and what action is pending.'],
          ['Gate 08 · Readiness decision','The workflow advances only when the verification state is sufficiently clear or appropriately escalated.']
        ].map(x=><article key={x[0]} style={{border:`1px solid ${brand.black}`,padding:20}}>
          <p style={kicker}>{x[0]}</p><p style={{lineHeight:1.6,fontWeight:800}}>{x[1]}</p>
        </article>)}
      </div>
    </div>
  </section>

  <section style={{background:brand.black,color:brand.white,padding:'64px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Simulated Analysis</p>
      <h2 style={{...sectionTitle,color:brand.white}}>Eligibility Exception Decision Path</h2>
      <p style={{...body,color:brand.white}}><strong>Scenario:</strong> A simulated eligibility check returns incomplete, conflicting, inactive, or uncertain information. The verification response is treated as a workflow signal that must be classified before the case advances.</p>
      <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(260px,1fr))',gap:16,marginTop:28}}>
        <div style={{border:`1px solid ${brand.orange}`,padding:22}}><p style={kicker}>If verification is clear</p><h3>Document → Confirm → Advance</h3><p style={{lineHeight:1.6}}>The verified status and relevant findings are documented before the next workflow step.</p></div>
        <div style={{border:`1px solid ${brand.orange}`,padding:22}}><p style={kicker}>If verification is uncertain</p><h3>Classify → Reverify → Assign → Escalate / Resolve → Document</h3><p style={{lineHeight:1.6}}>The uncertainty remains visible until an owner, next action, and status are documented.</p></div>
      </div>
    </div>
  </section>

  <section style={{padding:'64px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Failure-Point Reasoning</p>
      <h2 style={sectionTitle}>Eligibility Risk-to-Control Matrix</h2>
      <style>{`
        .risk-mobile{display:none}
        @media(max-width:700px){.risk-desktop{display:none}.risk-mobile{display:grid;gap:14px}}
      `}</style>
      <div className="risk-desktop"><table style={{width:'100%',borderCollapse:'collapse'}}>
        <thead><tr>{['Verification signal / risk','Likely workflow stage','Why it matters','Control response'].map(h=><th key={h} style={{background:brand.black,color:brand.white,padding:13,textAlign:'left',border:`1px solid ${brand.black}`}}>{h}</th>)}</tr></thead>
        <tbody>{scenarios.map(r=><tr key={r[0]}>{r.map(x=><td key={x} style={{padding:13,border:`1px solid ${brand.black}`,verticalAlign:'top',lineHeight:1.45}}>{x}</td>)}</tr>)}</tbody>
      </table></div>
      <div className="risk-mobile">{scenarios.map(r=><article key={r[0]} style={{border:`1px solid ${brand.black}`,padding:18}}>
        <p style={{...kicker,margin:'0 0 5px'}}>Verification Signal / Risk</p><p style={{fontWeight:900,lineHeight:1.45,margin:'0 0 15px'}}>{r[0]}</p>
        <p style={{...kicker,margin:'0 0 5px'}}>Likely Workflow Stage</p><p style={{lineHeight:1.45,margin:'0 0 15px'}}>{r[1]}</p>
        <p style={{...kicker,margin:'0 0 5px'}}>Why It Matters</p><p style={{lineHeight:1.55,margin:'0 0 15px'}}>{r[2]}</p>
        <p style={{...kicker,margin:'0 0 5px'}}>Control Response</p><p style={{lineHeight:1.55,margin:0}}>{r[3]}</p>
      </article>)}</div>
    </div>
  </section>

  <section style={{padding:'58px 22px',borderTop:`1px solid ${brand.black}`}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Measurement Layer</p>
      <h2 style={sectionTitle}>Simulated Educational Measures</h2>
      <p style={body}>These measures show how this student-developed verification model could make completion, unresolved eligibility questions, exception classification, aging, and handoff quality more visible. They are educational measures only and do not represent employer performance results.</p>
      <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(240px,1fr))',gap:12,marginTop:24}}>{measures.map(k=><div key={k[0]} style={{border:`1px solid ${brand.black}`,padding:18}}><strong>{k[0]}</strong><p style={{lineHeight:1.5}}>{k[1]}</p></div>)}</div>
    </div>
  </section>

  <section style={{background:brand.black,color:brand.white,padding:'62px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Skills Demonstrated</p>
      <h2 style={{...sectionTitle,color:brand.white}}>What This Project Demonstrates</h2>
      <div style={{display:'flex',flexWrap:'wrap',gap:10}}>{['Patient-Access Workflow Literacy','Eligibility Reasoning','Insurance Verification Awareness','Exception Classification','Authorization-Screening Awareness','Workflow Mapping','Control-Point Design','Handoff Documentation','Root-Cause Reasoning','Patient-Impact Awareness'].map(x=><span key={x} style={{border:`1px solid ${brand.orange}`,color:brand.orange,padding:'11px 14px',fontWeight:900}}>{x}</span>)}</div>
    </div>
  </section>

  <section style={{padding:'64px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Key Takeaway</p>
      <h2 style={sectionTitle}>Unresolved Coverage Questions Should Not Disappear Into the Next Workflow Step.</h2>
      <p style={body}>This case study demonstrates how a student can practice eligibility and insurance-verification thinking: confirm the information being checked, classify the verification result, identify unresolved uncertainty, assign ownership, document the next action, and decide whether the workflow should advance, hold, or escalate.</p>
      <div style={{borderLeft:`5px solid ${brand.orange}`,padding:'6px 0 6px 20px',marginTop:30,maxWidth:850}}>
        <strong>Integrity boundary</strong>
        <p style={{lineHeight:1.65}}>Created by Kori Pickle, Bachelor's Degree in Healthcare Administration Candidate, University of Phoenix. This student-developed project is educational, simulated, and uses no PHI, employer data, payer data, real claims data, or real patient information. It demonstrates applied healthcare operations learning and does not represent professional eligibility-verification experience, payer authority, benefit interpretation authority, authorization authority, live EHR access, or work with real patient accounts.</p>
      </div>
      <a href="/" style={{display:'inline-block',marginTop:28,background:brand.orange,color:brand.white,textDecoration:'none',padding:'14px 20px',fontWeight:900}}>← Return to Portfolio</a>
    </div>
  </section>
</main>
}

export const metadata={title:'Eligibility & Insurance Verification Analysis | Kori Pickle',description:'Student-developed, simulated, no-PHI healthcare operations case study on patient access, eligibility verification, coverage uncertainty, authorization screening, exception control, and workflow handoffs.'};
