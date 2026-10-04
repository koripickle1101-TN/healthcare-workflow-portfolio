const brand = {
  orange: '#FF8200',
  black: '#000000',
  white: '#FFFFFF',
  line: '#000000',
};

const caseStudies = [
  {
    title: 'Revenue Cycle Workflow Breakdown',
    focus: 'Patient access, claim readiness, workflow validation',
    problem: 'Revenue cycle failures often appear at denial, but many root causes begin upstream in intake, eligibility, authorization, and documentation.',
    outcome: 'Maps risk points and proposes validation checkpoints before claim submission.',
    href: '/case-studies/revenue-cycle-workflow-breakdown',
  },
  {
    title: 'Eligibility & Insurance Verification Analysis',
    focus: 'Insurance verification, payer validation, eligibility risk',
    problem: 'Incorrect or incomplete coverage information can create avoidable denials, rework, delays, and patient billing confusion.',
    outcome: 'Defines verification controls and eligibility status logic for cleaner claim readiness.',
    href: '/case-studies/eligibility-insurance-verification-analysis',
  },
  {
    title: 'Denial Root Cause Analysis Framework',
    focus: 'Denial categories, pattern recognition, workflow feedback loops',
    problem: 'Denials are often treated as one-off billing issues instead of repeatable system signals.',
    outcome: 'Connects denial categories to workflow stages and prevention opportunities.',
    href: '/case-studies/denial-root-cause-analysis-framework',
  },
  {
    title: 'Payment Posting Control Gate + Exception-Origin Matrix',
    focus: 'ERA/EOB review, exception routing, reconciliation, downstream control',
    problem: 'A payment-posting exception may be where a problem becomes visible even when the workflow first lost control upstream in eligibility, authorization, documentation, claim submission, or payer processing.',
    outcome: 'Uses a simulated control gate to classify downstream signals, trace possible failure origins, assign ownership, document action, validate resolution, and close the workflow.',
    href: '/case-studies/payment-posting-control-gate',
  },
];

const skills = ['Revenue Cycle Management', 'Insurance Verification', 'Claims Workflow Analysis', 'Denial Prevention', 'Workflow Mapping', 'Exception Management', 'Revenue-Cycle Readiness', 'Healthcare Operations', 'Health Informatics', 'Data Validation'];

export default function Home() {
  return (
    <main style={{ fontFamily: 'Arial, Helvetica, sans-serif', background: brand.white, color: brand.black }}>
      <section style={{ borderTop: `10px solid ${brand.orange}`, padding: '34px 22px 86px' }}>
        <div style={{ maxWidth: 1180, margin: '0 auto' }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 18, marginBottom: 54 }}>
            <div style={{ height: 2, width: 180, background: brand.orange }} />
            <div style={{ color: brand.orange, fontWeight: 900, letterSpacing: '0.18em', fontSize: 18 }}>HEALTHCARE OPERATIONS PORTFOLIO</div>
            <div style={{ height: 2, width: 180, background: brand.orange }} />
          </div>

          <p style={{ color: brand.orange, fontWeight: 900, letterSpacing: '0.28em', textTransform: 'uppercase', fontSize: 14, marginBottom: 22 }}>Kori Pickle</p>
          <h1 style={{ fontFamily: 'Georgia, Times New Roman, serif', fontSize: 'clamp(48px, 8vw, 94px)', lineHeight: 0.95, margin: 0, maxWidth: 980 }}>
            Healthcare Operations Intelligence Engine™
          </h1>
          <p style={{ marginTop: 28, maxWidth: 840, fontSize: 'clamp(21px, 3vw, 31px)', lineHeight: 1.35, fontWeight: 800 }}>
            Where healthcare workflows break before patients, staff, and revenue feel the impact.
          </p>
          <p style={{ marginTop: 22, maxWidth: 780, fontSize: 18, lineHeight: 1.75, color: brand.black }}>
            I am a Bachelor's Degree in Healthcare Administration Candidate building an honest patient-to-professional healthcare operations foundation through student-developed, simulated, no-PHI portfolio projects. I study where workflow control is lost across patient access, eligibility, authorization, documentation, revenue-cycle readiness, denial prevention, and downstream exception handling.
          </p>

          <div style={{ display: 'flex', flexWrap: 'wrap', gap: 14, marginTop: 34 }}>
            <a href="#case-studies" style={{ background: brand.orange, color: brand.white, textDecoration: 'none', padding: '15px 24px', borderRadius: 0, fontWeight: 900, letterSpacing: '0.04em' }}>View Case Studies</a>
            <a href="https://github.com/koripickle1101-TN/healthcare-workflow-portfolio" style={{ background: brand.white, color: brand.black, textDecoration: 'none', padding: '15px 24px', borderRadius: 0, fontWeight: 900, letterSpacing: '0.04em', border: `1px solid ${brand.black}` }}>View GitHub Repo</a>
          </div>
        </div>
      </section>

      <section style={{ background: brand.white, padding: '70px 22px' }}>
        <div style={{ maxWidth: 1180, margin: '0 auto' }}>
          <p style={{ color: brand.orange, fontWeight: 900, letterSpacing: '0.22em', textTransform: 'uppercase', fontSize: 13 }}>Operating Focus</p>
          <h2 style={{ fontFamily: 'Georgia, Times New Roman, serif', fontSize: 'clamp(36px, 5vw, 62px)', margin: '10px 0 26px' }}>Systems Over Symptoms</h2>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: 18 }}>
            {['Patient Intake', 'Eligibility Verification', 'Authorization Gaps', 'Claim Readiness', 'Denial Root Cause', 'Workflow Feedback'].map((item) => (
              <div key={item} style={{ background: brand.white, border: `1px solid ${brand.line}`, borderRadius: 0, padding: 24 }}>
                <div style={{ width: 52, height: 52, borderRadius: '50%', border: `1px solid ${brand.black}`, display: 'grid', placeItems: 'center', marginBottom: 16 }}>
                  <div style={{ width: 38, height: 38, borderRadius: '50%', border: `2px solid ${brand.orange}` }} />
                </div>
                <h3 style={{ margin: 0, fontSize: 19 }}>{item}</h3>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section id="case-studies" style={{ padding: '82px 22px' }}>
        <div style={{ maxWidth: 1180, margin: '0 auto' }}>
          <p style={{ color: brand.orange, fontWeight: 900, letterSpacing: '0.22em', textTransform: 'uppercase', fontSize: 13 }}>Recruiter-Facing Case Studies</p>
          <h2 style={{ fontFamily: 'Georgia, Times New Roman, serif', fontSize: 'clamp(38px, 5vw, 66px)', margin: '10px 0 18px' }}>Where Did the Workflow First Lose Control?</h2>
          <p style={{ maxWidth: 780, color: brand.black, fontSize: 18, lineHeight: 1.7, marginBottom: 34 }}>
            Each case study is student-developed, simulated, and no-PHI. The goal is to demonstrate workflow mapping, control-point thinking, exception management, root-cause reasoning, and responsible healthcare operations learning without claiming professional healthcare experience.
          </p>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: 22 }}>
            {caseStudies.map((study, index) => (
              <article key={study.title} style={{ border: `1px solid ${brand.line}`, borderRadius: 0, padding: 28, background: brand.white }}>
                <p style={{ color: brand.orange, fontWeight: 900, letterSpacing: '0.16em', textTransform: 'uppercase', fontSize: 12 }}>Case Study 0{index + 1}</p>
                <h3 style={{ fontSize: 27, lineHeight: 1.1, margin: '10px 0 14px' }}>{study.title}</h3>
                <p style={{ fontWeight: 900, color: brand.black }}>{study.focus}</p>
                <p><strong>Problem:</strong> {study.problem}</p>
                <p><strong>Approach:</strong> {study.outcome}</p>
                {study.href !== '#' ? (
                  <a href={study.href} style={{ display: 'inline-block', marginTop: 12, background: brand.black, color: brand.white, borderBottom: `3px solid ${brand.orange}`, textDecoration: 'none', padding: '12px 16px', fontWeight: 900, letterSpacing: '0.04em' }}>Open Case Study →</a>
                ) : (
                  <span style={{ display: 'inline-block', marginTop: 12, border: `1px solid ${brand.black}`, padding: '10px 14px', fontSize: 12, fontWeight: 800, letterSpacing: '0.08em', textTransform: 'uppercase' }}>Evidence page in development</span>
                )}
              </article>
            ))}
          </div>
        </div>
      </section>

      <section style={{ background: brand.black, color: brand.white, padding: '76px 22px' }}>
        <div style={{ maxWidth: 1180, margin: '0 auto' }}>
          <p style={{ color: brand.orange, fontWeight: 900, letterSpacing: '0.22em', textTransform: 'uppercase', fontSize: 13 }}>Skills Demonstrated</p>
          <h2 style={{ fontFamily: 'Georgia, Times New Roman, serif', fontSize: 'clamp(36px, 5vw, 62px)', margin: '10px 0 28px' }}>Evidence for Healthcare Operations Pathways</h2>
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: 12 }}>
            {skills.map((skill) => (
              <span key={skill} style={{ border: `1px solid ${brand.orange}`, color: brand.orange, borderRadius: 0, padding: '12px 18px', fontWeight: 900 }}>{skill}</span>
            ))}
          </div>
        </div>
      </section>

      <section style={{ padding: '72px 22px', textAlign: 'center' }}>
        <div style={{ maxWidth: 900, margin: '0 auto' }}>
          <p style={{ color: brand.orange, fontWeight: 900, letterSpacing: '0.22em', textTransform: 'uppercase', fontSize: 13 }}>Professional Direction</p>
          <h2 style={{ fontFamily: 'Georgia, Times New Roman, serif', fontSize: 'clamp(34px, 5vw, 56px)', margin: '10px 0 18px' }}>
            Building toward entry-level opportunities in patient access, revenue-cycle support, healthcare operations, documentation workflow, health informatics, quality improvement, and implementation support.
          </h2>
          <p style={{ color: brand.black, fontSize: 18, lineHeight: 1.7 }}>
            Created by Kori Pickle, Bachelor's Degree in Healthcare Administration Candidate, University of Phoenix. Student-developed, simulated, no-PHI healthcare operations portfolio work.
          </p>
        </div>
      </section>
    </main>
  );
}

export const metadata = {
  title: 'Healthcare Operations Intelligence Engine™ | Kori Pickle',
  description: 'Student-developed, simulated, no-PHI healthcare operations case studies focused on patient access, workflow intelligence, denial prevention, documentation quality, revenue-cycle readiness, and responsible AI.',
  openGraph: {
    title: 'Healthcare Operations Intelligence Engine™ | Kori Pickle',
    description: 'Where healthcare workflows break before patients, staff, and revenue feel the impact.',
    images: ['/api/og'],
  },
};