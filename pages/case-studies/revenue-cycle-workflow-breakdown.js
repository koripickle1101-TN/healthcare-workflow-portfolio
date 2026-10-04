const brand={orange:'#FF8200',black:'#000000',white:'#FFFFFF'};

const stages=[
['Patient intake','Capture demographic, contact, and insurance information','Is the information complete enough for downstream work?'],
['Eligibility verification','Confirm coverage status and benefit information','Was coverage checked and documented before the next step?'],
['Prior authorization','Identify whether authorization is required','Was the requirement identified, assigned, and resolved?'],
['Documentation readiness','Confirm required information is available','Is anything missing that could block claim readiness?'],
['Claim preparation','Validate claim-ready information before submission','Did upstream data pass final review?'],
['Claim submission','Transmit the claim and monitor acceptance','Was the claim accepted into payer processing?'],
['Payer processing','Payer validates and adjudicates the claim','Did the claim move through adjudication as expected?'],
['Denial / exception feedback','Classify the downstream signal and trace possible origins','Where did the workflow first lose control?']
];

const risks=[
['Incomplete registration data','Patient intake','Missing or inaccurate demographics or payer information can move downstream into eligibility, claim preparation, or billing confusion.','Validate required fields before the workflow advances.'],
['Coverage not verified','Eligibility verification','An eligibility-related issue may not become visible until claim rejection, denial, or patient balance activity.','Document coverage status and unresolved questions before service or submission.'],
['Authorization requirement missed','Prior authorization','A missing or unresolved authorization can create downstream denial or rework.','Confirm requirement, ownership, status, and next action before claim readiness.'],
['Required information missing','Documentation readiness','Incomplete documentation or work-queue items can prevent clean claim preparation.','Use a readiness check before the claim moves forward.'],
['Claim-ready data mismatch','Claim preparation','A claim can carry forward upstream errors even when submission itself works correctly.','Validate key data elements before transmission.'],
['Submission rejection','Claim submission','A claim may fail before adjudication because of formatting, missing data, or payer routing issues.','Classify the rejection and route it back to the correct origin point.'],
['Denial appears downstream','Payer processing / feedback','The denial is the detection point, but the failure may have begun earlier.','Trace the denial category back through intake, eligibility, authorization, documentation, and submission.'],
['Patient balance looks wrong','Post-adjudication feedback','An unexpected balance can reflect earlier adjudication, posting, eligibility, or documentation problems.','Verify the source before treating the patient balance as the root cause.']
];

const measures=[
['Upstream completeness rate','Share of simulated cases that pass intake requirements before advancing'],
['Eligibility verification status','Whether simulated coverage checks are complete, pending, or unresolved'],
['Authorization exception count','Number of simulated cases with unresolved authorization requirements'],
['Claim-readiness exception count','Number of simulated cases blocked by missing or inconsistent information'],
['Submission rejection count','Number of simulated claims that fail before adjudication'],
['Denial-origin classification rate','Whether downstream denials are linked to a plausible workflow origin'],
['Exception aging','How long simulated unresolved items remain open'],
['Closure validation rate','Whether resolved exceptions include evidence of review and closure']
];

const kicker={color:brand.orange,fontWeight:900,letterSpacing:'0.2em',textTransform:'uppercase',fontSize:12};
const sectionTitle={fontFamily:'Georgia, Times New Roman, serif',fontSize:'clamp(34px,5vw,58px)',lineHeight:1.02,margin:'8px 0 20px'};
const body={fontSize:17,lineHeight:1.7,maxWidth:850};

export default function RevenueCycleWorkflowBreakdown(){
return <main style={{fontFamily:'Arial, Helvetica, sans-serif',background:brand.white,color:brand.black}}>
  <header style={{borderTop:`10px solid ${brand.orange}`,padding:'28px 22px 64px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <a href="/" style={{color:brand.black,textDecoration:'none',fontWeight:900,fontSize:13}}>← Portfolio Home</a>
      <p style={{...kicker,marginTop:42}}>Case Study 01 · Revenue Cycle / Patient Access / Claim Readiness</p>
      <h1 style={{fontFamily:'Georgia, Times New Roman, serif',fontSize:'clamp(46px,8vw,86px)',lineHeight:.96,margin:'14px 0 22px',maxWidth:1000}}>Revenue Cycle Workflow Breakdown</h1>
      <p style={{fontSize:'clamp(20px,3vw,28px)',fontWeight:800,lineHeight:1.35,maxWidth:850}}>A student-developed workflow case study built around one question: where did the workflow first lose control before the denial, rework, delay, or patient balance appeared?</p>
      <div style={{display:'flex',flexWrap:'wrap',gap:10,marginTop:26}}>
        {['Student-developed','Simulated','No PHI','Healthcare Administration Candidate'].map(x=><span key={x} style={{border:`1px solid ${brand.black}`,padding:'9px 12px',fontSize:12,fontWeight:900,textTransform:'uppercase',letterSpacing:'.06em'}}>{x}</span>)}
      </div>
    </div>
  </header>

  <section style={{background:brand.black,color:brand.white,padding:'48px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Core Operations Insight</p>
      <h2 style={{...sectionTitle,color:brand.white}}>Downstream Symptoms Can Begin Upstream</h2>
      <p style={{...body,color:brand.white}}>A denial, rejection, delayed claim, or confusing patient balance may be where a revenue-cycle problem becomes visible, but that does not automatically identify the original failure point. This simulated project maps the workflow from patient intake through payer feedback so each downstream signal can be traced back to the control point where information, ownership, or validation may have first broken down.</p>
    </div>
  </section>

  <section style={{padding:'66px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Problem → Workflow</p>
      <h2 style={sectionTitle}>Why Revenue Cycle Needs Connected-Process Thinking</h2>
      <p style={body}>Revenue-cycle work is connected. Patient intake, eligibility verification, prior authorization, documentation readiness, claim preparation, submission, payer processing, and downstream follow-up affect one another. This case study treats each stage as a control point and asks what must be complete, documented, owned, or validated before work moves forward.</p>
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
      <h2 style={sectionTitle}>Validation Gates Before the Claim Moves Forward</h2>
      <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(260px,1fr))',gap:14}}>
        {[
          ['Gate 01 · Intake completeness','Required demographic and payer information is present before eligibility work begins.'],
          ['Gate 02 · Coverage status','Eligibility findings are documented and unresolved questions are visible.'],
          ['Gate 03 · Authorization status','Requirement, owner, status, and next action are clear before claim readiness.'],
          ['Gate 04 · Documentation readiness','Required information is complete enough to support the next workflow step.'],
          ['Gate 05 · Claim-readiness validation','Key simulated data elements are reviewed before submission.'],
          ['Gate 06 · Submission acceptance','Rejected claims are classified and routed rather than treated as completed work.'],
          ['Gate 07 · Downstream feedback','Denials and other exceptions are traced to possible workflow origins.'],
          ['Gate 08 · Closure','Resolved exceptions are validated before the workflow is considered complete.']
        ].map(x=><article key={x[0]} style={{border:`1px solid ${brand.black}`,padding:20}}>
          <p style={kicker}>{x[0]}</p><p style={{lineHeight:1.6,fontWeight:800}}>{x[1]}</p>
        </article>)}
      </div>
    </div>
  </section>

  <section style={{background:brand.black,color:brand.white,padding:'64px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Simulated Analysis</p>
      <h2 style={{...sectionTitle,color:brand.white}}>Revenue-Cycle Exception Path</h2>
      <p style={{...body,color:brand.white}}><strong>Scenario:</strong> A simulated claim produces a downstream denial or exception. The denial is treated as a signal, not automatically as the root cause. The workflow review moves backward through the stages until the earliest plausible control loss is identified.</p>
      <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(260px,1fr))',gap:16,marginTop:28}}>
        <div style={{border:`1px solid ${brand.orange}`,padding:22}}><p style={kicker}>If the workflow is controlled</p><h3>Validate → Advance → Confirm</h3><p style={{lineHeight:1.6}}>Each stage meets its readiness condition before the next stage begins.</p></div>
        <div style={{border:`1px solid ${brand.orange}`,padding:22}}><p style={kicker}>If an exception appears</p><h3>Classify → Trace → Assign → Resolve → Validate</h3><p style={{lineHeight:1.6}}>The downstream signal is linked to a possible origin, assigned for next action, and checked again before closure.</p></div>
      </div>
    </div>
  </section>

  <section style={{padding:'64px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Failure-Point Reasoning</p>
      <h2 style={sectionTitle}>Risk-to-Control Matrix</h2>
      <style>{`
        .risk-mobile{display:none}
        @media(max-width:700px){.risk-desktop{display:none}.risk-mobile{display:grid;gap:14px}}
      `}</style>
      <div className="risk-desktop"><table style={{width:'100%',borderCollapse:'collapse'}}>
        <thead><tr>{['Downstream signal / risk','Likely workflow stage','Why it matters','Control response'].map(h=><th key={h} style={{background:brand.black,color:brand.white,padding:13,textAlign:'left',border:`1px solid ${brand.black}`}}>{h}</th>)}</tr></thead>
        <tbody>{risks.map(r=><tr key={r[0]}>{r.map(x=><td key={x} style={{padding:13,border:`1px solid ${brand.black}`,verticalAlign:'top',lineHeight:1.45}}>{x}</td>)}</tr>)}</tbody>
      </table></div>
      <div className="risk-mobile">{risks.map(r=><article key={r[0]} style={{border:`1px solid ${brand.black}`,padding:18}}>
        <p style={{...kicker,margin:'0 0 5px'}}>Downstream Signal / Risk</p><p style={{fontWeight:900,lineHeight:1.45,margin:'0 0 15px'}}>{r[0]}</p>
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
      <p style={body}>These measures show how this student-developed workflow model could make readiness, exceptions, aging, classification, and closure more visible. They are educational measures only and do not represent employer performance results.</p>
      <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(240px,1fr))',gap:12,marginTop:24}}>{measures.map(k=><div key={k[0]} style={{border:`1px solid ${brand.black}`,padding:18}}><strong>{k[0]}</strong><p style={{lineHeight:1.5}}>{k[1]}</p></div>)}</div>
    </div>
  </section>

  <section style={{background:brand.black,color:brand.white,padding:'62px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Skills Demonstrated</p>
      <h2 style={{...sectionTitle,color:brand.white}}>What This Project Demonstrates</h2>
      <div style={{display:'flex',flexWrap:'wrap',gap:10}}>{['Revenue-Cycle Workflow Literacy','Patient-Access Awareness','Eligibility Reasoning','Authorization Awareness','Claim-Readiness Thinking','Workflow Mapping','Control-Point Design','Root-Cause Reasoning','Exception Routing','Handoff Awareness'].map(x=><span key={x} style={{border:`1px solid ${brand.orange}`,color:brand.orange,padding:'11px 14px',fontWeight:900}}>{x}</span>)}</div>
    </div>
  </section>

  <section style={{padding:'64px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Key Takeaway</p>
      <h2 style={sectionTitle}>The Denial Is Not Always Where the Workflow Failed.</h2>
      <p style={body}>This case study demonstrates how a student can practice connected-process thinking across the revenue cycle: define readiness conditions, identify control points, treat downstream problems as signals, trace possible upstream origins, assign the next action, and validate closure.</p>
      <div style={{borderLeft:`5px solid ${brand.orange}`,padding:'6px 0 6px 20px',marginTop:30,maxWidth:850}}>
        <strong>Integrity boundary</strong>
        <p style={{lineHeight:1.65}}>Created by Kori Pickle, Bachelor's Degree in Healthcare Administration Candidate, University of Phoenix. This student-developed project is educational, simulated, and uses no PHI, employer data, payer data, claims data, or real patient information. It demonstrates applied healthcare operations learning and does not represent professional revenue-cycle experience, billing or coding authority, payer authority, live EHR access, or work with real patient accounts.</p>
      </div>
      <a href="/" style={{display:'inline-block',marginTop:28,background:brand.orange,color:brand.white,textDecoration:'none',padding:'14px 20px',fontWeight:900}}>← Return to Portfolio</a>
    </div>
  </section>
</main>
}

export const metadata={title:'Revenue Cycle Workflow Breakdown | Kori Pickle',description:'Student-developed, simulated, no-PHI healthcare operations case study on patient access, eligibility, authorization, claim readiness, denial prevention, workflow controls, and root-cause reasoning.'};
