const brand = {
  orange: '#FF8200',
  black: '#000000',
  white: '#FFFFFF',
  gray: '#F7F4EF',
  line: '#EFE6DA',
};

const caseStudies = [
  {
    title: 'Revenue Cycle Workflow Breakdown',
    focus: 'Patient access, claim readiness, workflow validation',
    problem: 'Revenue cycle failures often appear at denial, but many root causes begin upstream in intake, eligibility, authorization, and documentation.',
    outcome: 'Maps risk points and proposes validation checkpoints before claim submission.',
  },
  {
    title: 'Eligibility & Insurance Verification Analysis',
    focus: 'Insurance verification, payer validation, eligibility risk',
    problem: 'Incorrect or incomplete coverage information can create avoidable denials, rework, delays, and patient billing confusion.',
    outcome: 'Defines verification controls and eligibility status logic for cleaner claim readiness.',
  },
  {
    title: 'Denial Root Cause Analysis Framework',
    focus: 'Denial categories, pattern recognition, workflow feedback loops',
    problem: 'Denials are often treated as one-off billing issues instead of repeatable system signals.',
    outcome: 'Connects denial categories to workflow stages and prevention opportunities.',
  },
];

const skills = ['Revenue Cycle Management', 'Insurance Verification', 'Claims Analysis', 'Denial Prevention', 'Workflow Analysis', 'Healthcare Operations', 'Health Informatics', 'Data Validation'];

export default function Home() {
  return (
    <main style={{ fontFamily: 'Arial, Helvetica, sans-serif', background: brand.white, color: brand.black }}>
      <section style={{ borderTop: `10px solid ${brand.orange}`, padding: '34px 22px 86px' }}>
        <div style={{ maxWidth: 1180, margin: '0 auto' }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 18, marginBottom: 54 }}>
            <div style={{ height: 2, width: 180, background: brand.orange }} />
            <div style={{ color: brand.orange, fontWeight: 900, letterSpacing: '0.18em', fontSize: 18 }}>RCM PORTFOLIO</div>
            <div style={{ height: 2, width: 180, background: brand.orange }} />
          </div>

          <p style={{ color: brand.orange, fontWeight: 900, letterSpacing: '0.28em', textTransform: 'uppercase', fontSize: 14, marginBottom: 22 }}>Kori Pickle</p>
          <h1 style={{ fontFamily: 'Georgia, Times New Roman, serif', fontSize: 'clamp(48px, 8vw, 94px)', lineHeight: 0.95, margin: 0, maxWidth: 980 }}>
            Revenue Cycle Optimization Portfolio
          </h1>
          <p style={{ marginTop: 28, maxWidth: 840, fontSize: 'clamp(21px, 3vw, 31px)', lineHeight: 1.35, fontWeight: 800 }}>
            Denial prevention, claims analysis, and workflow intelligence for healthcare operations.
          </p>
          <p style={{ marginTop: 22, maxWidth: 780, fontSize: 18, lineHeight: 1.75, color: '#333' }}>
            This portfolio contains self-directed RCM case studies designed to show how upstream workflow gaps can create downstream denials, rework, delayed reimbursement, and patient access problems. No PHI, no employer data, and no false work claims are used.
          </p>

          <div style={{ display: 'flex', flexWrap: 'wrap', gap: 14, marginTop: 34 }}>
            <a href="#case-studies" style={{ background: brand.orange, color: brand.white, textDecoration: 'none', padding: '15px 24px', borderRadius: 999, fontWeight: 900 }}>View Case Studies</a>
            <a href="https://github.com/koripickle1101-TN/healthcare-workflow-portfolio" style={{ background: brand.white, color: brand.black, textDecoration: 'none', padding: '15px 24px', borderRadius: 999, fontWeight: 900, border: `1px solid ${brand.black}` }}>View GitHub Repo</a>
          </div>
        </div>
      </section>

      <section style={{ background: brand.gray, padding: '70px 22px' }}>
        <div style={{ maxWidth: 1180, margin: '0 auto' }}>
          <p style={{ color: brand.orange, fontWeight: 900, letterSpacing: '0.22em', textTransform: 'uppercase', fontSize: 13 }}>Operating Focus</p>
          <h2 style={{ fontFamily: 'Georgia, Times New Roman, serif', fontSize: 'clamp(36px, 5vw, 62px)', margin: '10px 0 26px' }}>Systems Over Symptoms</h2>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: 18 }}>
            {['Patient Intake', 'Eligibility Verification', 'Authorization Gaps', 'Claim Readiness', 'Denial Root Cause', 'Workflow Feedback'].map((item) => (
              <div key={item} style={{ background: brand.white, border: `1px solid ${brand.line}`, borderRadius: 24, padding: 24 }}>
                <div style={{ width: 46, height: 46, borderRadius: '50%', border: `2px solid ${brand.orange}`, boxShadow: '0 0 18px rgba(255,130,0,0.16)', marginBottom: 16 }} />
                <h3 style={{ margin: 0, fontSize: 19 }}>{item}</h3>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section id="case-studies" style={{ padding: '82px 22px' }}>
        <div style={{ maxWidth: 1180, margin: '0 auto' }}>
          <p style={{ color: brand.orange, fontWeight: 900, letterSpacing: '0.22em', textTransform: 'uppercase', fontSize: 13 }}>Recruiter-Facing Case Studies</p>
          <h2 style={{ fontFamily: 'Georgia, Times New Roman, serif', fontSize: 'clamp(38px, 5vw, 66px)', margin: '10px 0 18px' }}>Proof of RCM Workflow Thinking</h2>
          <p style={{ maxWidth: 780, color: '#333', fontSize: 18, lineHeight: 1.7, marginBottom: 34 }}>
            Each case study is self-directed and simulated for portfolio demonstration. The goal is to show analyst-level reasoning: problem, workflow risk, root cause logic, prevention strategy, and ethical boundaries.
          </p>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: 22 }}>
            {caseStudies.map((study, index) => (
              <article key={study.title} style={{ border: `1px solid ${brand.line}`, borderRadius: 28, padding: 28, background: brand.white }}>
                <p style={{ color: brand.orange, fontWeight: 900, letterSpacing: '0.16em', textTransform: 'uppercase', fontSize: 12 }}>Case Study 0{index + 1}</p>
                <h3 style={{ fontSize: 27, lineHeight: 1.1, margin: '10px 0 14px' }}>{study.title}</h3>
                <p style={{ fontWeight: 900, color: '#222' }}>{study.focus}</p>
                <p><strong>Problem:</strong> {study.problem}</p>
                <p><strong>Approach:</strong> {study.outcome}</p>
              </article>
            ))}
          </div>
        </div>
      </section>

      <section style={{ background: brand.black, color: brand.white, padding: '76px 22px' }}>
        <div style={{ maxWidth: 1180, margin: '0 auto' }}>
          <p style={{ color: brand.orange, fontWeight: 900, letterSpacing: '0.22em', textTransform: 'uppercase', fontSize: 13 }}>Skills Demonstrated</p>
          <h2 style={{ fontFamily: 'Georgia, Times New Roman, serif', fontSize: 'clamp(36px, 5vw, 62px)', margin: '10px 0 28px' }}>Built for RCM Analyst Pathways</h2>
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: 12 }}>
            {skills.map((skill) => (
              <span key={skill} style={{ border: `1px solid ${brand.orange}`, color: brand.orange, borderRadius: 999, padding: '12px 18px', fontWeight: 900 }}>{skill}</span>
            ))}
          </div>
        </div>
      </section>

      <section style={{ padding: '72px 22px', textAlign: 'center' }}>
        <div style={{ maxWidth: 900, margin: '0 auto' }}>
          <p style={{ color: brand.orange, fontWeight: 900, letterSpacing: '0.22em', textTransform: 'uppercase', fontSize: 13 }}>Professional Direction</p>
          <h2 style={{ fontFamily: 'Georgia, Times New Roman, serif', fontSize: 'clamp(34px, 5vw, 56px)', margin: '10px 0 18px' }}>
            Open to remote RCM, claims, patient access, and health informatics pathways.
          </h2>
          <p style={{ color: '#333', fontSize: 18, lineHeight: 1.7 }}>
            Created by Kori Pickle. Focused on revenue cycle workflow analysis, denial prevention, claims accuracy, and healthcare operations.
          </p>
        </div>
      </section>
    </main>
  );
}

export const metadata = {
  title: 'Revenue Cycle Optimization Portfolio | Kori Pickle',
  description: 'RCM case studies focused on denial prevention, claims analysis, workflow intelligence, and healthcare operations.',
  openGraph: {
    title: 'Revenue Cycle Optimization Portfolio | Kori Pickle',
    description: 'Denial Prevention • Claims Analysis • Workflow Intelligence',
    images: ['/api/og'],
  },
};