const brand={orange:'#FF8200',black:'#000000',white:'#FFFFFF'};

const controls=[
['Receive payment','Capture incoming remittance/payment','Did everything expected arrive?'],
['Validate','Confirm payment/remittance details','Does the payment match supporting information?'],
['Identify account','Match payment to the correct account/claim','Are we posting to the correct account?'],
['Review ERA/EOB','Understand adjudication','What did the payer determine?'],
['Post payment','Apply payment correctly','Was the payment applied correctly?'],
['Post adjustments','Record applicable adjustments','Is the adjustment supported?'],
['Patient responsibility','Transfer the appropriate balance','Is this truly patient responsibility?'],
['Review exceptions','Identify denied/partial payments','Who owns the next action?'],
['Unapplied cash','Research unmatched payments',"Why can't this payment be matched?"],
['Credit balances','Identify overpayment/duplicate signals','What created the credit?'],
['Reconciliation','Compare received vs. posted','Does the batch balance?'],
['QA / close','Final validation','Is there evidence the batch is complete and accurate?']
];

const origins=[
['Eligibility-related denial','Registration / eligibility','Was coverage verified correctly before service or claim submission?'],
['Authorization issue','Prior authorization','Was the requirement identified, documented, and resolved?'],
['Missing-information exception','Documentation / work queue','Was required information complete before submission?'],
['Rejected / denied claim','Claim preparation / submission','Where did the claim fail validation or adjudication?'],
['Partial / unexpected payment','Payer / contract / claim issue','Why does the remittance differ from the expected disposition?'],
['Unapplied cash','Payment / account matching',"Why can't the payment be linked confidently?"],
['Credit balance','Posting / payment activity','Could a duplicate payment, overpayment, or posting issue be involved?'],
['Incorrect patient balance','Adjudication / posting','Was responsibility transferred accurately?']
];

const kpis=[
['Posting accuracy rate','Accuracy of simulated transactions'],
['Unapplied cash count / value','Payments awaiting account matching'],
['Exception volume','Transactions requiring intervention'],
['Exception aging','How long unresolved items remain open'],
['Credit balance count / value','Accounts requiring credit review'],
['Reconciliation discrepancy rate','Difference between received and posted totals'],
['First-pass exception classification rate','Whether exceptions were categorized correctly initially'],
['Resolution turnaround time','Time between identification and simulated closure']
];

const sectionTitle={fontFamily:'Georgia, Times New Roman, serif',fontSize:'clamp(34px,5vw,58px)',lineHeight:1.02,margin:'8px 0 20px'};
const kicker={color:brand.orange,fontWeight:900,letterSpacing:'0.2em',textTransform:'uppercase',fontSize:12};
const body={fontSize:17,lineHeight:1.7,maxWidth:850};

export default function PaymentPostingCaseStudy(){
return <main style={{fontFamily:'Arial, Helvetica, sans-serif',background:brand.white,color:brand.black}}>
  <header style={{borderTop:`10px solid ${brand.orange}`,padding:'28px 22px 64px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <a href="/" style={{color:brand.black,textDecoration:'none',fontWeight:900,fontSize:13}}>← Portfolio Home</a>
      <p style={{...kicker,marginTop:42}}>Case Study 04 · Revenue Cycle / Workflow Intelligence / Denial Prevention</p>
      <h1 style={{fontFamily:'Georgia, Times New Roman, serif',fontSize:'clamp(46px,8vw,86px)',lineHeight:.96,margin:'14px 0 22px',maxWidth:1000}}>Payment Posting Control Gate + Exception-Origin Matrix</h1>
      <p style={{fontSize:'clamp(20px,3vw,28px)',fontWeight:800,lineHeight:1.35,maxWidth:850}}>A downstream revenue-cycle control case study built around one question: where did the workflow first lose control?</p>
      <div style={{display:'flex',flexWrap:'wrap',gap:10,marginTop:26}}>
        {['Student-developed','Simulated','No PHI','BSHA Candidate'].map(x=><span key={x} style={{border:`1px solid ${brand.black}`,padding:'9px 12px',fontSize:12,fontWeight:900,textTransform:'uppercase',letterSpacing:'.06em'}}>{x}</span>)}
      </div>
    </div>
  </header>

  <section style={{background:brand.black,color:brand.white,padding:'48px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Core Operations Insight</p>
      <h2 style={{...sectionTitle,color:brand.white}}>Detection Point ≠ Failure Point</h2>
      <p style={{...body,color:brand.white}}>An exception discovered during payment posting may have originated earlier in registration, eligibility verification, prior authorization, documentation, claim preparation or submission, payer processing, or posting itself. The downstream signal is where investigation begins—not automatically where the failure began.</p>
    </div>
  </section>

  <section style={{padding:'66px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}>
      <p style={kicker}>Problem → Workflow</p><h2 style={sectionTitle}>Why Payment Posting Functions as a Control Gate</h2>
      <p style={body}>Payment posting is more than recording a payment. ERA/EOB review can make denials, partial payments, unexpected adjustments, incorrect patient responsibility, unapplied cash, credit balances, and reconciliation discrepancies visible. This simulated project reframes those outcomes as workflow signals that require classification, ownership, follow-up, validation, and closure.</p>
      <div style={{display:'flex',flexWrap:'wrap',alignItems:'center',gap:8,marginTop:32}}>
        {['Payment received','Validate','Account / claim','ERA / EOB','Expected outcome?','Post or exception gate','Reconcile','QA + close'].map((x,i)=><div key={x} style={{display:'flex',alignItems:'center',gap:8}}>
          <div style={{border:`1px solid ${brand.black}`,borderRadius:999,width:92,height:92,display:'grid',placeItems:'center',padding:6,textAlign:'center',fontSize:12,fontWeight:900}}>
            <div style={{border:`2px solid ${brand.orange}`,borderRadius:999,width:72,height:72,display:'grid',placeItems:'center',padding:5}}>{x}</div>
          </div>{i<7&&<span style={{color:brand.orange,fontWeight:900,letterSpacing:3}}>···</span>}
        </div>)}
      </div>
    </div>
  </section>

  <section style={{padding:'58px 22px',borderTop:`1px solid ${brand.black}`}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}><p style={kicker}>Control Design</p><h2 style={sectionTitle}>Twelve Operational Checkpoints</h2>
      <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(250px,1fr))',gap:14}}>
        {controls.map((r,i)=><article key={r[0]} style={{border:`1px solid ${brand.black}`,padding:20}}>
          <p style={{...kicker,margin:0}}>Control {String(i+1).padStart(2,'0')}</p><h3 style={{fontSize:21,margin:'9px 0'}}>{r[0]}</h3>
          <p style={{lineHeight:1.5}}>{r[1]}</p><p style={{fontWeight:900,borderTop:`2px solid ${brand.orange}`,paddingTop:12}}>{r[2]}</p>
        </article>)}
      </div>
    </div>
  </section>

  <section style={{background:brand.black,color:brand.white,padding:'64px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}><p style={kicker}>Simulated Analysis</p><h2 style={{...sectionTitle,color:brand.white}}>Exception-Control Decision Path</h2>
      <p style={{...body,color:brand.white}}><strong>Scenario:</strong> A simulated claim reaches payment posting with an unexpected disposition or payment variance. ERA/remittance review is the detection point. The control gate asks whether the outcome is expected before normal progression continues.</p>
      <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(260px,1fr))',gap:16,marginTop:28}}>
        <div style={{border:`1px solid ${brand.orange}`,padding:22}}><p style={kicker}>Expected</p><h3>Post → Reconcile → QA → Close</h3><p style={{lineHeight:1.6}}>Routine flow continues after validation.</p></div>
        <div style={{border:`1px solid ${brand.orange}`,padding:22}}><p style={kicker}>Unexpected</p><h3>Enter Exception Gate</h3><p style={{lineHeight:1.6}}>Classify variance → identify possible origin → assign owner → document action → resolve/rework/escalate → validate → reconcile → close.</p></div>
      </div>
    </div>
  </section>

  <section style={{padding:'64px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}><p style={kicker}>Failure-Point Reasoning</p><h2 style={sectionTitle}>Exception-Origin Matrix</h2>
      <div style={{overflowX:'auto'}}><table style={{width:'100%',borderCollapse:'collapse',minWidth:700}}>
        <thead><tr>{['Downstream signal','Possible origin','Operational question'].map(h=><th key={h} style={{background:brand.black,color:brand.white,padding:13,textAlign:'left',border:`1px solid ${brand.black}`}}>{h}</th>)}</tr></thead>
        <tbody>{origins.map(r=><tr key={r[0]}>{r.map(x=><td key={x} style={{padding:13,border:`1px solid ${brand.black}`,verticalAlign:'top',lineHeight:1.45}}>{x}</td>)}</tr>)}</tbody>
      </table></div>
    </div>
  </section>

  <section style={{padding:'58px 22px',borderTop:`1px solid ${brand.black}`}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}><p style={kicker}>Measurement Layer</p><h2 style={sectionTitle}>Simulated Educational KPIs</h2>
      <p style={body}>These measures demonstrate how a workflow analyst might think about visibility and control. They are simulated educational measures—not employer performance results.</p>
      <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(240px,1fr))',gap:12,marginTop:24}}>{kpis.map(k=><div key={k[0]} style={{border:`1px solid ${brand.black}`,padding:18}}><strong>{k[0]}</strong><p style={{lineHeight:1.5}}>{k[1]}</p></div>)}</div>
    </div>
  </section>

  <section style={{background:brand.black,color:brand.white,padding:'62px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}><p style={kicker}>Skills Demonstrated</p><h2 style={{...sectionTitle,color:brand.white}}>What This Project Proves</h2>
      <div style={{display:'flex',flexWrap:'wrap',gap:10}}>{['Workflow Mapping','RCM Literacy','Exception Management','Root-Cause Reasoning','Control Design','Reconciliation Awareness','Handoff Awareness','Patient-Impact Awareness'].map(x=><span key={x} style={{border:`1px solid ${brand.orange}`,color:brand.orange,padding:'11px 14px',fontWeight:900}}>{x}</span>)}</div>
    </div>
  </section>

  <section style={{padding:'64px 22px'}}>
    <div style={{maxWidth:1120,margin:'0 auto'}}><p style={kicker}>Key Takeaway</p><h2 style={sectionTitle}>The Visible Problem May Be Downstream of the Actual Breakdown.</h2>
      <p style={body}>This case study demonstrates how a student can use payment-posting outcomes to practice connected-process thinking: identify the signal, avoid assuming the detection point is the root cause, classify the exception, trace possible upstream origins, assign the next action, and verify closure.</p>
      <div style={{borderLeft:`5px solid ${brand.orange}`,padding:'6px 0 6px 20px',marginTop:30,maxWidth:850}}>
        <strong>Integrity boundary</strong><p style={{lineHeight:1.65}}>Created by Kori Pickle, BSHA Candidate, University of Phoenix. This project is educational, simulated, and does not use PHI, employer data, payer data, claims data, or real patient information. It does not claim professional payment-posting experience, coding authority, reimbursement authority, payer-contract interpretation, live EHR access, or real patient-account work.</p>
      </div>
      <a href="/" style={{display:'inline-block',marginTop:28,background:brand.orange,color:brand.white,textDecoration:'none',padding:'14px 20px',fontWeight:900}}>← Return to Portfolio</a>
    </div>
  </section>
</main>
}

export const metadata={title:'Payment Posting Control Gate | Kori Pickle',description:'Student-developed, simulated, no-PHI healthcare operations case study on payment-posting exceptions, root-cause reasoning, exception routing, reconciliation, and control design.'};
