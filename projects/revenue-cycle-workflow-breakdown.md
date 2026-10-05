# Case Study: Revenue Cycle Workflow Breakdown

**Project Type:** Student-developed, simulated, no-PHI healthcare operations portfolio case study  
**Degree:** Bachelor's of Science degree in Healthcare Administration @ the University of Phoenix  
**Focus Area:** Patient access, claims readiness, denial prevention, workflow validation  
**Brand System:** Pure White `#FFFFFF`, True Black `#000000`, Tennessee Orange `#FF8200`

---

## Executive Summary

This case study analyzes how revenue cycle failures can begin upstream before a claim is submitted. The purpose is to demonstrate practical healthcare operations and revenue-cycle workflow thinking without implying employer, payer, coding, billing, EHR, or client experience.

The analysis follows the Healthcare Operations Intelligence Engine™ question:

**Where did the workflow first lose control?**

The case study identifies front-end breakdown points, traces downstream consequences, and proposes validation checkpoints that could reduce avoidable rework and denial risk.

---

## Scenario

A simulated healthcare organization is experiencing recurring claim issues related to eligibility, authorization, documentation readiness, claim submission, payer processing, and aging accounts receivable.

Instead of treating each denial or unpaid balance as a separate billing problem, this case study evaluates the full workflow from patient intake through follow-up.

---

## Problem Statement

A revenue-cycle problem may become visible long after it actually began.

An unpaid balance discovered during A/R follow-up can require tracing the account back through registration, eligibility, authorization, documentation, claim submission, or payer processing. The operational task is therefore not only to identify the current problem, but also to determine the earliest point where the workflow failed to contain it.

Common upstream risk points include:

- Incomplete patient demographic information
- Incorrect or outdated insurance details
- Missing eligibility verification
- Authorization requirements not confirmed before service
- Documentation that does not fully support claim readiness
- Claim submission issues that are not resolved promptly
- Weak handoffs between patient access, documentation, billing, and follow-up
- Unclear ownership when an exception requires escalation

These issues can create downstream rework, delayed reimbursement, avoidable denials, aging A/R, and patient confusion.

---

## Workflow Map

```text
Patient Intake
   ↓
Insurance Capture
   ↓
Eligibility Verification
   ↓
Authorization Review
   ↓
Documentation Check
   ↓
Claim Preparation
   ↓
Claim Submission
   ↓
Payer Processing / Claim Status
   ↓
Payment / Adjustment / Denial
   ↓
A/R Follow-Up
```

---

## Revenue-Cycle Control Logic

The portfolio analysis now evaluates each stage through four operational control questions:

1. **Owner** — Who is responsible for the next action?
2. **Status** — Is the item complete, pending, rejected, denied, or unresolved?
3. **Evidence** — What documentation or system evidence shows the step was completed?
4. **Escalation** — What happens when the workflow cannot safely move forward?

This reframes the revenue cycle from a list of independent tasks into a chain of connected controls and handoffs.

---

## Key Risk Analysis

| Workflow Stage | Potential Breakdown | Failure Signal | Downstream Impact | Prevention / Control Opportunity |
|---|---|---|---|---|
| Patient Intake | Missing demographics or incorrect patient information | Required data incomplete | Rework, claim edits, patient contact delays | Required-field validation before progression |
| Insurance Capture | Wrong payer, inactive coverage, outdated plan | Payer or plan mismatch | Eligibility and claim risk | Validate payer, member, and plan information |
| Eligibility Verification | No validation before service | Coverage or benefit uncertainty | Rejection, denial, patient balance risk | Verify eligibility and document findings close to service |
| Authorization Review | Requirement unclear, pending, or missed | Unresolved authorization status | Delay or authorization-related denial risk | Confirm requirement, owner, status, and escalation path |
| Documentation Check | Missing support for service or incomplete documentation | Documentation not claim-ready | Claim delay or denial risk | Pre-bill documentation completeness check |
| Claim Preparation | Claim moves forward without final validation | Unresolved edits or missing data | Increased rework risk | Claim-readiness checklist |
| Claim Submission | Submission is rejected or not accepted | Rejection / acceptance failure | Claim never reaches adjudication | Resolve rejection and document resubmission |
| Payer Processing / Status | Claim remains pending or unresolved | No clear movement or status | Aging and delayed reimbursement | Status follow-up and escalation |
| Payment / Denial | Adjustment or denial appears | Unpaid or reduced balance | Rework, appeal, correction, or write-off review | Route issue to correct owner and classify root cause |
| A/R Follow-Up | Aging balance remains unresolved | 30/60/90+ day aging | Cash-flow delay and repeated manual work | Trace backward to first failed control, not only current balance |

---

## Root-Cause Trace: Where Did the Workflow First Lose Control?

A downstream problem should be traced backward until the first failed control is identified.

```text
Aging A/R balance
   ↑
Denial / unresolved payer outcome
   ↑
Claim submission or claim-status problem
   ↑
Documentation or claim-readiness issue
   ↑
Authorization requirement not resolved
   ↑
Eligibility or insurance discrepancy
   ↑
Registration / intake data problem
```

The point where the problem becomes visible is not necessarily the point where it began.

This distinction adds operational value because it separates:

- **Current location of the problem**
from
- **Originating control failure**

That difference is critical for root-cause analysis, ownership, corrective action, and prevention.


---

## Denial Signal → Upstream Control Matrix

Denial information is treated here as a **diagnostic signal**, not as proof that the failure began in billing. The purpose of this matrix is to connect a downstream outcome to the earliest workflow control that should be investigated.

| Downstream Signal | First Control Area to Investigate | Control Question | Appropriate Operational Response |
|---|---|---|---|
| Coverage / eligibility issue | Insurance capture + eligibility verification | Was coverage valid for the date of service, and was the correct plan verified? | Recheck source data and coverage evidence; correct routing/data when appropriate |
| Prior-authorization issue | Scheduling + authorization review | Was authorization required, obtained, documented, and still valid for the service? | Verify requirement/status and route unresolved issues to the appropriate owner |
| Patient / insurance data mismatch | Registration + insurance capture | Were demographics, subscriber/member identifiers, payer, and plan information validated? | Correct source data before allowing the error to continue downstream |
| Duplicate-claim signal | Claim status + submission control | Was an earlier claim already accepted, pending, or adjudicated? | Check claim status before any resubmission |
| Timely-filing signal | Claim submission + work-queue monitoring | When was the claim ready, submitted, rejected, corrected, and resubmitted relative to the applicable payer deadline? | Track payer-specific filing limits and unresolved submission exceptions; do not assume one universal filing window |
| Missing / incomplete information | Documentation + claim-readiness control | What required information was absent, and where should completeness have been verified? | Route to the correct owner, complete the missing information, and strengthen the pre-submission checkpoint |
| Coordination-of-benefits issue | Insurance capture + payer-order validation | Was other coverage identified and was payer order established correctly? | Validate primary/secondary coverage and update payer routing as appropriate |
| Coding / modifier / bundling signal | Coding / claim-edit workflow | Does the issue require coding review rather than an administrative correction? | Route to qualified coding/billing personnel; this portfolio does not simulate coding authority |
| Medical-necessity signal | Documentation / coverage-policy workflow | What payer or coverage requirement generated the outcome, and what documentation or review is required? | Route for qualified clinical/coding/payer-policy review rather than making a student-level determination |

### Remittance-Code Guardrail

A remittance adjustment should not be interpreted from a number alone. The workflow should consider the **Claim Adjustment Group Code (CAGC), Claim Adjustment Reason Code (CARC), any applicable Remittance Advice Remark Code (RARC), payer context, and the underlying claim/account history** before assigning root cause.

Examples used only for educational recognition:

- **CARC 18** — duplicate claim/service signal.
- **CARC 27** — expenses incurred after coverage terminated; this is more precise than labeling every eligibility problem simply “CO-27.”
- **CARC 29** — filing time limit expired.
- **CARC 197** — precertification/authorization/notification/pre-treatment absent.
- **CARC 97** — payment included in the allowance for another service/procedure.

The **CO** prefix is a Claim Adjustment Group Code meaning Contractual Obligation; it is not part of the CARC number itself. Group-code use depends on the adjudication context.

### Control-Gate Lesson

The useful question is not:

> “Which denial code do I memorize?”

It is:

> **“What downstream signal appeared, what evidence explains it, which upstream control should have caught the issue, who owns the next action, and where did the workflow first lose control?”**

This keeps denial analysis connected to patient access, authorization, documentation quality, claim readiness, payer processing, A/R, and prevention without implying coding, billing, clinical, or payer authority.

---

## Proposed Workflow Controls

1. Confirm complete patient demographics before account progression.
2. Verify insurance and eligibility information close to the date of service.
3. Confirm payer-specific authorization requirements and document status.
4. Check that required documentation is complete before claim preparation.
5. Validate claim readiness before submission.
6. Confirm that rejected submissions are corrected and resubmitted.
7. Track unresolved claim status before balances age unnecessarily.
8. Classify denial or payment issues by likely upstream origin.
9. Assign ownership and escalation when an exception cannot be resolved at the current stage.
10. Feed denial and A/R findings back upstream so the same control failure is less likely to recur.

---

## Simulated Improvement Targets

These targets are educational only and are not based on employer, payer, claim, EHR, or patient data.

| Metric | Current Risk Signal | Target Direction |
|---|---|---|
| Eligibility-related denials | High repeat risk | Reduce through earlier verification and documented handoff |
| Authorization-related denials | Requirement unresolved before service | Improve confirmation, ownership, and escalation |
| Claim rework | Frequent manual correction | Reduce through validation checkpoints |
| Clean claim readiness | Inconsistent | Improve through pre-submission review |
| Aging A/R | Problems discovered late | Trace root cause earlier and escalate unresolved accounts sooner |
| Repeat denial patterns | Same failure recurs | Feed downstream findings back to upstream controls |


---

## Measurement Layer: KPIs as Workflow Signals

Revenue-cycle metrics are most useful here as **signals that tell the analyst where to investigate**, not as proof of a root cause by themselves.

| KPI / Signal | What It Can Reveal | Root-Cause Question |
|---|---|---|
| Clean-claim performance | Whether claims are moving forward without avoidable correction | Which upstream control is allowing incomplete or inaccurate information to reach submission? |
| Denial rate / denial pattern | Where payment problems are recurring | Are repeated denials tracing back to eligibility, authorization, documentation, submission, or payer processing? |
| Days in A/R / aging distribution | How long balances remain unresolved | At what earlier handoff did ownership, status, evidence, or escalation break down? |
| Reimbursement trend | Whether payment outcomes are changing over time | Is the change tied to workflow quality, payer processing, unresolved denials, or another factor that requires investigation? |
| Prior-authorization outcomes | Whether authorization requests are being approved, denied, delayed, or returned for more information | Was the requirement identified early, was documentation complete, and was the request escalated when necessary? |

**Control principle:** A KPI identifies a signal. Root-cause analysis determines where the workflow first lost control.

### EOB and Denial Information as Downstream Evidence

An Explanation of Benefits (EOB) can help a patient understand how a health plan processed a claim, including charges, plan payment, and potential patient responsibility. It is not itself a bill.

For workflow analysis, payment, adjustment, denial, and reason information should be treated as **downstream evidence** that can trigger investigation. A denial should not automatically be treated as the originating failure point. The analysis traces the issue backward through the relevant handoffs until the first failed control is identified.

This preserves the distinction between:

- **Signal:** what became visible downstream
- **Root cause:** where the workflow first lost control
- **Corrective action:** what resolves the current issue
- **Preventive control:** what reduces recurrence upstream

### 2026–2027 Operational Relevance

Prior authorization is becoming more measurable and more digital. CMS requirements for impacted payers include specific denial reasons and public reporting of prior-authorization metrics beginning in 2026, while certain standards-based Prior Authorization API requirements begin in 2027. For this simulated project, that makes **status, reason, documentation, ownership, turnaround, and escalation** especially relevant workflow-control concepts.

This project does not claim hands-on payer, billing, coding, EHR, API, or prior-authorization experience. It demonstrates student-level analysis of how those operational signals can be organized into a workflow-control framework.

### Authoritative Reference Points

- Centers for Medicare & Medicaid Services. *How to read a health insurance explanation of benefits.* https://www.cms.gov/initiatives/your-patient-rights/medical-bill-rights/get-help/medical-bill-guides-resources/how-read-health-insurance-explanation-benefits
- Centers for Medicare & Medicaid Services. *CMS Interoperability and Prior Authorization Final Rule (CMS-0057-F).* https://www.cms.gov/initiatives/burden-reduction/overview/interoperability/policies-regulations/cms-interoperability-prior-authorization-final-rule-cms-0057-f
- Centers for Medicare & Medicaid Services. *Improving Prior Authorization Processes.* https://www.cms.gov/initiatives/burden-reduction/overview/interoperability/frequently-asked-questions/prior-authorization-api/improving-prior-authorization-processes
- Centers for Medicare & Medicaid Services. *Electronic Prior Authorization.* https://www.cms.gov/priorities/electronic-prior-authorization/overview

---

## Analyst Takeaway

The strongest revenue-cycle improvements often happen before the claim is submitted.

A denial-prevention and workflow-integrity mindset asks:

- Where did the workflow first lose control?
- What allowed the issue to move downstream?
- Which control should have caught it earlier?
- Who owned the unresolved step?
- What evidence should have shown completion?
- When should the issue have escalated?
- How can the workflow prevent the same failure from recurring?

---

## Skills Demonstrated

- Revenue-cycle workflow analysis
- Patient access process thinking
- Eligibility verification awareness
- Prior-authorization workflow awareness
- Claims-readiness logic
- Denial-prevention strategy
- A/R root-cause reasoning
- Workflow handoff analysis
- Control-point identification
- Ownership and escalation logic
- Healthcare operations communication

---

## Ethical Note

Created by Kori Pickle, Bachelor's of Science degree in Healthcare Administration @ the University of Phoenix.

This project is educational, simulated, and does not use PHI, employer data, payer data, claims data, EHR data, or real patient information.

**Healthcare Operations Intelligence Engine™**  
*Where healthcare workflows break before patients, staff, and revenue feel the impact.*

**Core question:** Where did the workflow first lose control?
