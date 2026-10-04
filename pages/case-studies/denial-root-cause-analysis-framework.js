const brand={orange:'#FF8200',black:'#000000',white:'#FFFFFF'};

const denialSteps=[
['Detect denial / rejection','Capture the downstream signal','What exactly became visible?'],
['Classify category','Group the denial by reason or operational theme','What type of problem is this?'],
['Locate detection point','Identify where the issue surfaced in the workflow','Where was the signal detected?'],
['Trace upstream','Review earlier workflow stages for plausible control loss','Where could the problem have started?'],
['Assign ownership','Route the issue to the appropriate simulated workflow owner','Who owns the next action?'],
['Resolve / rework','Address the simulated exception or correct the workflow condition','What action would move the case forward?'],
['Validate outcome','Confirm the issue is resolved or appropriately escalated','Did the corrective action work?'],
['Feed back learning','Connect the denial pattern to prevention opportunities','What should change upstream next time?']
];

const matrix=[
['Eligibility-related denial','Eligibility verification','Coverage status, payer/member mismatch, or unresolved eligibility question','Recheck coverage status and trace whether the issue originated before claim submission.'],
['Authorization denial','Prior authorization','Requirement not identified, incomplete, expired, or unresolved','Trace whether the authorization control failed before the service or claim advanced.'],
['Missing-information denial','Documentation / claim readiness','Required information may have been incomplete or unavailable','Identify which readiness check should have caught the missing information.'],
['Registration / demographic issue','Patient intake','Demographic or payer information may be inaccurate or inconsistent','Review the intake control point and validate the information that moved downstream.'],
['Submission-related rejection','Claim submission','Claim may fail before adjudication because of format, routing, or required-field issues','Separate rejection from denial and route the issue to the correct preparation/submission stage.'],
['Medical-necessity / policy-related denial','Payer adjudication / clinical-policy review','The denial may depend on payer policy or documentation that this student project does not interpret clinically','Classify the signal and route it for appropriate professional review without claiming clinical or payer-policy authority.'],
['Duplicate / coordination-related issue','Claim history / payer order','Multiple submissions or payer-order uncertainty may create downstream conflict','Trace claim history and coordination logic conceptually without assuming the detection point is the origin.'],
['Patient-responsibility discrepancy','Adjudication / posting feedback','The balance may reflect earlier eligibility, adjudication, posting, or documentation issues','Verify the upstream basis before treating the patient balance as the root cause.']
];

const measures=[
['Denial category count','Number of simulated denials grouped by operational category'],
['First-pass classification rate','Whether simulated denials are categorized correctly on initial review'],
['Upstream-origin identification rate','Whether a plausible workflow origin is documented for each simulated denial'],
['Rework volume','Number of simulated cases requiring correction or additional action'],
['Exception aging','How long simulated denial issues remain unresolved'],
['Repeat-pattern count','How often the same simulated denial pattern appears across cases'],
['Closure validation rate','Whether simulated denial cases include evidence of review and closure'],
['Prevention-feedback count','Number of simulated cases linked to an upstream prevention opportunity']
];

const kicker={color:brand.orange,fontWeight:900,letterSpacing:'0.2em',textTransform:'uppercase',fontSize:12};
const sectionTitle={fontFamily:'Georgia, Times New Roman, serif',fontSize:'clamp(34px,5vw,58px)',lineHeight:1.02,margin:'8px 0 20px'};
const body={fontSize:17,lineHeight:1.7,maxWidth:850};

export default function DenialRootCauseAnalysisFramework(){
return <main style={{fontFamily:'Arial, Helvetica, sans-serif',background:brand.white,color:brand.black}}>
  <header style={{borderTop:`10px solid ${brand.orange}`,padding:'28px 22px 64px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <a href="/" style={{color:brand.black,textDecoration:'none',fontWeight:900,fontSize:13}}>← Portfolio Home</a>
      <p style={{...kicker,marginTop:42}}>Case Study 03 · Denial Prevention / Root-Cause Reasoning / Workflow Feedback</p>
      <h1 style={{fontFamily:'Georgia, Times New Roman, serif',fontSize:'clamp(46px,8vw,86px)',lineHeight:.96,margin:'14px 0 22px',maxWidth:1000}}>Denial Root Cause Analysis Framework</h1>
      <p style={{fontSize:'clamp(20px,3vw,28px)',fontWeight:800,lineHeight:1.35,maxWidth:850}}>A student-developed denial-analysis case study built around one question: when a denial appears downstream, how do we trace it back to the plausible workflow failure point without assuming the denial itself is the root cause?</p>
      <div style={{display:'flex',flexWrap:'wrap',gap:10,marginTop:26}}>
        {['Student-developed','Simulated','No PHI','Healthcare Administration Candidate'].map(x=><span key={x} style={{border:`1px solid ${brand.black}`,padding:'9px 12px',fontSize:12,fontWeight:900,textTransform:'uppercase',letterSpacing:'.06em'}}>{x}</span>)}
      </div>
    </div>
  </header>

  <section style={{background:brand.black,color:brand.white,padding:'48px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Core Operations Insight</p>
      <h2 style={{...sectionTitle,color:brand.white}}>A Denial Is a Signal, Not Automatically the Root Cause</h2>
      <p style={{...body,color:brand.white}}>Denials are visible downstream, but their causes may originate earlier in patient intake, eligibility verification, authorization, documentation readiness, claim preparation, submission, or payer processing. This simulated framework treats the denial as the starting point for investigation: classify the signal, locate where it surfaced, trace upstream for plausible control loss, assign the next action, validate closure, and feed the learning back into prevention.</p>
    </div>
  </section>

  <section style={{padding:'66px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Problem → Analysis Path</p>
      <h2 style={sectionTitle}>How a Denial Becomes a Root-Cause Question</h2>
      <p style={body}>This student-developed model separates the <strong>detection point</strong> from the <strong>plausible failure point</strong>. The denial is where the issue becomes visible. The analysis then moves backward through the workflow to identify which earlier control may have failed, remained unresolved, or lacked clear ownership.</p>
      <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(210px,1fr))',gap:14,marginTop:32}}>
        {denialSteps.map((s,i)=><article key={s[0]} style={{border:`1px solid ${brand.black}`,padding:18}}>
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
      <h2 style={sectionTitle}>Eight Denial-Analysis Control Gates</h2>
      <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(260px,1fr))',gap:14}}>
        {[
          ['Gate 01 · Signal capture','The denial or rejection is recorded clearly enough to support classification.'],
          ['Gate 02 · Category classification','The issue is grouped into an operational category before root-cause assumptions are made.'],
          ['Gate 03 · Detection-point identification','The workflow stage where the problem became visible is separated from where it may have begun.'],
          ['Gate 04 · Upstream trace','Earlier workflow stages are reviewed for plausible control loss.'],
          ['Gate 05 · Ownership','The next simulated action has a clear owner or escalation path.'],
          ['Gate 06 · Corrective action','The issue is resolved, reworked, or escalated rather than left open.'],
          ['Gate 07 · Closure validation','The outcome is checked before the denial case is considered closed.'],
          ['Gate 08 · Prevention feedback','The pattern is connected to an upstream control or prevention opportunity.']
        ].map(x=><article key={x[0]} style={{border:`1px solid ${brand.black}`,padding:20}}>
          <p style={kicker}>{x[0]}</p><p style={{lineHeight:1.6,fontWeight:800}}>{x[1]}</p>
        </article>)}
      </div>
    </div>
  </section>

  <section style={{background:brand.black,color:brand.white,padding:'64px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Simulated Analysis</p>
      <h2 style={{...sectionTitle,color:brand.white}}>Denial Root-Cause Decision Path</h2>
      <p style={{...body,color:brand.white}}><strong>Scenario:</strong> A simulated denial is identified after claim submission. Instead of treating the denial code or payer response as the complete explanation, the framework asks where the issue was detected, which earlier control points could plausibly have contributed, and what evidence would be needed before closure.</p>
      <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(260px,1fr))',gap:16,marginTop:28}}>
        <div style={{border:`1px solid ${brand.orange}`,padding:22}}><p style={kicker}>First classify the signal</p><h3>Detect → Classify → Locate</h3><p style={{lineHeight:1.6}}>Define what became visible and where it surfaced before making a root-cause judgment.</p></div>
        <div style={{border:`1px solid ${brand.orange}`,padding:22}}><p style={kicker}>Then trace and close</p><h3>Trace → Assign → Resolve → Validate → Feed Back</h3><p style={{lineHeight:1.6}}>Move upstream, identify the plausible origin, route the next action, validate the result, and connect the pattern to prevention.</p></div>
      </div>
    </div>
  </section>

  <section style={{padding:'64px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Failure-Point Reasoning</p>
      <h2 style={sectionTitle}>Denial-to-Origin Matrix</h2>
      <style>{`
        .risk-mobile{display:none}
        @media(max-width:700px){.risk-desktop{display:none}.risk-mobile{display:grid;gap:14px}}
      `}</style>
      <div className="risk-desktop"><table style={{width:'100%',borderCollapse:'collapse'}}>
        <thead><tr>{['Downstream denial signal','Possible workflow origin','Why it matters','Control response'].map(h=><th key={h} style={{background:brand.black,color:brand.white,padding:13,textAlign:'left',border:`1px solid ${brand.black}`}}>{h}</th>)}</tr></thead>
        <tbody>{matrix.map(r=><tr key={r[0]}>{r.map(x=><td key={x} style={{padding:13,border:`1px solid ${brand.black}`,verticalAlign:'top',lineHeight:1.45}}>{x}</td>)}</tr>)}</tbody>
      </table></div>
      <div className="risk-mobile">{matrix.map(r=><article key={r[0]} style={{border:`1px solid ${brand.black}`,padding:18}}>
        <p style={{...kicker,margin:'0 0 5px'}}>Downstream Denial Signal</p><p style={{fontWeight:900,lineHeight:1.45,margin:'0 0 15px'}}>{r[0]}</p>
        <p style={{...kicker,margin:'0 0 5px'}}>Possible Workflow Origin</p><p style={{lineHeight:1.45,margin:'0 0 15px'}}>{r[1]}</p>
        <p style={{...kicker,margin:'0 0 5px'}}>Why It Matters</p><p style={{lineHeight:1.55,margin:'0 0 15px'}}>{r[2]}</p>
        <p style={{...kicker,margin:'0 0 5px'}}>Control Response</p><p style={{lineHeight:1.55,margin:0}}>{r[3]}</p>
      </article>)}</div>
    </div>
  </section>

  <section style={{padding:'58px 22px',borderTop:`1px solid ${brand.black}`}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Measurement Layer</p>
      <h2 style={sectionTitle}>Simulated Educational Measures</h2>
      <p style={body}>These measures show how this student-developed denial framework could make classification, upstream-origin reasoning, rework, aging, closure, and prevention feedback more visible. They are educational measures only and do not represent employer performance results.</p>
      <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(240px,1fr))',gap:12,marginTop:24}}>{measures.map(k=><div key={k[0]} style={{border:`1px solid ${brand.black}`,padding:18}}><strong>{k[0]}</strong><p style={{lineHeight:1.5}}>{k[1]}</p></div>)}</div>
    </div>
  </section>

  <section style={{background:brand.black,color:brand.white,padding:'62px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Skills Demonstrated</p>
      <h2 style={{...sectionTitle,color:brand.white}}>What This Project Demonstrates</h2>
      <div style={{display:'flex',flexWrap:'wrap',gap:10}}>{['Denial-Prevention Literacy','Root-Cause Reasoning','Exception Classification','Workflow Mapping','Control-Point Design','Upstream Trace Thinking','Ownership & Escalation Awareness','Closure Validation','Pattern Recognition','Patient-Impact Awareness'].map(x=><span key={x} style={{border:`1px solid ${brand.orange}`,color:brand.orange,padding:'11px 14px',fontWeight:900}}>{x}</span>)}</div>
    </div>
  </section>

  <section style={{padding:'64px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Key Takeaway</p>
      <h2 style={sectionTitle}>The Denial Is Where the Investigation Starts—Not Necessarily Where the Workflow Failed.</h2>
      <p style={body}>This case study demonstrates how a student can practice denial root-cause reasoning: classify the signal, separate detection point from plausible failure point, trace upstream controls, assign the next action, validate closure, and connect repeat patterns to prevention opportunities.</p>
      <div style={{borderLeft:`5px solid ${brand.orange}`,padding:'6px 0 6px 20px',marginTop:30,maxWidth:850}}>
        <strong>Integrity boundary</strong>
        <p style={{lineHeight:1.65}}>Created by Kori Pickle, Bachelor's Degree in Healthcare Administration Candidate, University of Phoenix. This student-developed project is educational, simulated, and uses no PHI, employer data, payer data, real claims data, or real patient information. It demonstrates applied healthcare operations learning and does not represent professional denial-management experience, billing or coding authority, clinical decision-making, payer-policy authority, reimbursement authority, live EHR access, or work with real patient accounts.</p>
      </div>
      <a href="/" style={{display:'inline-block',marginTop:28,background:brand.orange,color:brand.white,textDecoration:'none',padding:'14px 20px',fontWeight:900}}>← Return to Portfolio</a>
    </div>
  </section>
</main>
}

export const metadata={title:'Denial Root Cause Analysis Framework | Kori Pickle',description:'Student-developed, simulated, no-PHI healthcare operations case study on denial classification, root-cause reasoning, upstream workflow tracing, exception ownership, closure validation, and prevention feedback.'};
