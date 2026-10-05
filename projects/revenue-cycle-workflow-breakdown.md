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

## EDI Transaction Lifecycle as a Workflow-Control Layer

Electronic Data Interchange (EDI) adds a **transport and transaction-status layer** to the revenue-cycle workflow. The operational question is not only whether the underlying eligibility, claim, status, or remittance work was performed, but whether the correct standardized transaction was created, transmitted, received, processed, and connected to the next action.

HIPAA Administrative Simplification uses standardized electronic transactions across covered entities. Relevant ASC X12 Version 5010 transactions include:

| Workflow Purpose | Standard Transaction | Operational Meaning |
|---|---|---|
| Eligibility / benefit verification | 270 inquiry → 271 response | Coverage and benefit information can move electronically between trading partners |
| Health care claim | 837 | Claim or equivalent encounter information is transmitted for payer processing |
| Claim status | 276 inquiry → 277 response | A provider can request and receive information about where a claim stands |
| Payment / remittance | 835 | Remittance information communicates how a claim was adjudicated and supports payment reconciliation |
| Prior authorization / referral | 278 | Administrative review / authorization information also has a standardized electronic transaction pathway |

### Transaction-Control Questions

```text
Business event occurs
   ↓
Correct transaction type selected
   ↓
Required data assembled
   ↓
Transaction transmitted
   ↓
Trading partner / clearinghouse / payer receives and processes it
   ↓
Response, status, or remittance returned when applicable
   ↓
Receiving system associates the response with the correct workflow item
   ↓
Exception is resolved or next action proceeds
```

| Control Point | Failure Signal | Operational Question |
|---|---|---|
| Transaction selection | Wrong transaction/workflow pathway | Is the correct standard being used for the business purpose? |
| Data preparation | Required information is incomplete or invalid | Did the source workflow produce complete, correctly structured information? |
| Transmission / routing | Transaction does not reach the intended trading partner | Where did routing or transmission lose control? |
| Processing | Transaction is not accepted or cannot be processed | Is this a transport/format issue, a data-quality issue, or a business-rule issue? |
| Response association | Returned eligibility, status, or remittance information cannot be connected to the originating workflow | Can the response be matched to the correct patient/account/claim/work item? |
| Exception ownership | Electronic failure remains unresolved | Who owns the exception, what evidence shows its status, and when should it escalate? |

### Portfolio Insight

**A digital transaction is not complete merely because it was sent.** Operational control requires visibility into transmission, receipt/processing, the applicable response, correct association back to the originating workflow, and ownership of exceptions.

This adds an important distinction to root-cause analysis: a downstream problem can originate in the **business process**, the **source data**, or the **electronic transaction pathway**. Determining which layer first lost control prevents every electronic failure from being mislabeled as a payer denial or billing problem.

This student-developed analysis is educational and simulated. It does not claim professional EDI configuration, clearinghouse administration, X12 implementation, claims submission, payer-system access, or HIPAA transaction compliance authority.

### Reference Points

- Centers for Medicare & Medicaid Services. *Adopted Standards and Operating Rules.* https://www.cms.gov/priorities/key-initiatives/burden-reduction/administrative-simplification/hipaa/adopted-standards-operating-rules
- Centers for Medicare & Medicaid Services. *About Administrative Simplification.* https://www.cms.gov/initiatives/burden-reduction/overview/administrative-simplification/about-administrative-simplification
- Centers for Medicare & Medicaid Services. *Health Care Claims Status.* https://www.cms.gov/priorities/key-initiatives/burden-reduction/administrative-simplification/transactions/health-care-claims-status

---

## Payment Posting as a Reconciliation Control Gate

Payment posting is not treated here as simple data entry. It is a downstream **reconciliation and exception-detection control** connecting payer adjudication, payment, account balances, patient responsibility, denials, and A/R follow-up.

For an electronic workflow, the operational chain can be viewed as:

```text
Claim adjudicated
   ↓
ERA / remittance information received
   ↓
EFT or other payment received
   ↓
Payment and adjustment details associated with the correct claim/account
   ↓
ERA-to-payment reconciliation
   ↓
Exceptions identified
   ↓
Correct balance / responsibility established
   ↓
Denial, underpayment, credit, or unresolved balance routed for follow-up
```

CMS explains that an Electronic Remittance Advice (ERA) reports final claim adjudication and payment information, including adjustment reasons and values. Medicare ERAs use the X12 835 format. The associated EFT carries the funds; matching the EFT to the correct ERA is called **reassociation**.

### Payment-Posting Control Questions

| Control Point | Failure Signal | Operational Question |
|---|---|---|
| Remittance receipt | ERA/remittance cannot be matched or interpreted | Do we have the adjudication detail needed to explain the payment? |
| Payment association | EFT/check does not align with expected remittance | Has the payment been associated with the correct ERA and account activity? |
| Adjustment review | Posted balance changes without a clear reason | Do the applicable Group Code, CARC, RARC, and remittance details explain the adjustment? |
| Responsibility assignment | Patient/provider responsibility appears inconsistent | Does the remittance support how the remaining balance was classified? |
| Exception detection | Denial, reduced payment, credit, or unapplied amount remains unresolved | Who owns the exception and what evidence is needed next? |
| Reconciliation | Posted totals do not align with payment/remittance evidence | Where did the workflow first lose control: adjudication interpretation, payment association, posting, or follow-up? |

### Portfolio Insight

**Payment posting is both a financial-recording step and a control point.** A posting workflow can expose downstream signals—such as an adjustment, denial, unmatched payment, or unresolved balance—that require investigation before the account can move cleanly into the next stage.

This student-developed analysis focuses on workflow logic, reconciliation, information quality, and exception routing. It does **not** claim professional payment-posting experience, payer-contract interpretation, coding authority, EHR/practice-management-system access, or responsibility for determining patient balances.

### Reference Points

- Centers for Medicare & Medicaid Services. *Health Care Payment and Remittance Advice.* https://www.cms.gov/medicare/coding-billing/electronic-billing/health-care-payment-remittance-advice
- Centers for Medicare & Medicaid Services. *Health Care Payment and Remittance Advice and Electronic Funds Transfer.* https://www.cms.gov/priorities/key-initiatives/burden-reduction/administrative-simplification/transactions/health-care-payment-remittance-advice-electronic-funds-transfer

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

## Quality Reporting as a Data-Integrity Workflow

Quality reporting adds a different operational lens to the revenue cycle: **some claim-associated data may support performance measurement even when the data element itself is not a separately reimbursed service.**

CPT Category II codes are supplemental tracking codes used for performance measurement. Their use is optional and they are not a substitute for Category I codes. Depending on the applicable MIPS measure and collection type, quality data may be collected and submitted through several mechanisms; Medicare Part B claims are only one possible collection type.

For workflow analysis, the important issue is not memorizing individual quality codes. It is protecting the integrity of the reporting chain:

```text
Measure requirement identified
   ↓
Eligible encounter / population recognized
   ↓
Required clinical or process data documented
   ↓
Correct measure-specific data captured
   ↓
Data transmitted through the applicable reporting method
   ↓
Submission / completeness validated
   ↓
Performance result reviewed
   ↓
Workflow gap investigated and corrected
```

### Quality-Reporting Control Gates

| Control Gate | Failure Signal | Operational Question |
|---|---|---|
| Measure identification | Wrong or outdated requirement used | Which performance year, measure specification, and collection type apply? |
| Documentation | Required measure element is absent or incomplete | Was the underlying activity/result documented at the appropriate point in the workflow? |
| Data capture | Documentation exists but structured reporting data is missing | Did the workflow reliably convert documentation into the required reportable data? |
| Transmission | Captured data does not reach the reporting destination | Did the selected claims, registry, EHR, or other reporting pathway transmit the data correctly? |
| Validation | Submission appears complete but required cases/data are missing | Was data completeness and submission status checked before the reporting deadline? |
| Feedback | Performance result is reviewed without workflow follow-through | Where did the reporting workflow first lose control, and what upstream control needs improvement? |

**Portfolio insight:** A `$0.00` or non-payable tracking element can still carry operational value when it supports an applicable quality-measure workflow. Financial value and information value are not the same thing.

This section is educational and simulated. It does not claim MIPS submission, CPT/HCPCS coding, EHR configuration, clinical quality reporting, Medicare billing, or compliance authority.

### Reference Points

- American Medical Association. *Criteria for CPT Category II codes.* https://www.ama-assn.org/practice-management/cpt/criteria-cpt-category-ii-codes
- American Medical Association. *Category II codes.* https://www.ama-assn.org/practice-management/cpt/category-ii-codes
- Centers for Medicare & Medicaid Services, Quality Payment Program. *Traditional MIPS.* https://qpp.cms.gov/reporting-requirements/ways-to-report/traditional-mips
- Centers for Medicare & Medicaid Services, Quality Payment Program. *Collect & Submit Data.* https://qpp.cms.gov/get-started/what-is-mips/data-collection-and-submission
- Centers for Medicare & Medicaid Services, Quality Payment Program. *Explore Measures & Activities — 2026.* https://qpp.cms.gov/reporting-requirements/measures-activities/explore?py=2026


---

## Code-Set Versioning as a Data-Governance Control

ICD knowledge adds the most value to this portfolio when treated as a **version-control and data-governance problem**, not as a claim of coding expertise.

In current U.S. workflows, **ICD-10-CM** is used to classify diagnoses across healthcare settings, while **ICD-10-PCS** is used for inpatient hospital procedure coding. CMS and NCHS publish effective-date-specific releases; therefore, a healthcare system should not treat a stored code value as complete context by itself.

A stronger information model preserves:

```text
Clinical documentation
   ↓
Applicable coding system identified
   ↓
Correct code-set version / effective date identified
   ↓
Authorized coding workflow assigns or validates code
   ↓
Code + system + version context stored
   ↓
Data transmitted / reused downstream
   ↓
Analytics, reporting, claims, or interoperability use validated
```

### Version-Control Questions

| Control Point | Failure Risk | Operational Question |
|---|---|---|
| Code-system identity | Same-looking data is interpreted under the wrong classification | Which coding system does this value belong to? |
| Version / effective date | A code is validated against the wrong release | Which code-set release was effective for the relevant encounter or discharge date? |
| Documentation-to-code handoff | Source documentation does not support reliable downstream classification | Is the documentation complete enough for the qualified coding workflow to act? |
| Data storage | Code is retained without sufficient provenance | Are system, version/effective-date context, and source history preserved? |
| Mapping / conversion | Legacy-to-current mapping is treated as automatically equivalent | Has the mapping been validated for its intended operational or analytic use? |
| Downstream reuse | Claims, analytics, reporting, or interfaces consume stale/misclassified data | Does the receiving workflow know which code system/version it received? |

### 2026–2027 U.S. Relevance

CMS lists FY 2027 ICD-10-CM and ICD-10-PCS updates effective October 1, 2026. ICD-10-CM remains the U.S. diagnosis classification used for healthcare encounters, and ICD-10-PCS remains the U.S. inpatient procedure coding system. ICD-11 is the WHO's latest global revision and has been in effect internationally since 2022, but countries transition on their own timelines. **ICD-11 should therefore not be treated as the current U.S. replacement for ICD-10-CM/PCS in this portfolio.**

**Portfolio insight:** A healthcare code is not merely a value. For reliable downstream use, the workflow also needs to know the **coding system, applicable version/effective date, provenance, and intended use**. That is a data-integrity and interoperability control.

This section is educational and simulated. It demonstrates healthcare data-governance and workflow reasoning; it does **not** claim diagnosis/procedure code assignment, coding certification, reimbursement determination, EHR configuration, or clinical authority.

### Reference Points

- Centers for Medicare & Medicaid Services. *ICD-10.* https://www.cms.gov/medicare/coding-billing/icd-10-codes
- Centers for Disease Control and Prevention, National Center for Health Statistics. *ICD-10-CM.* https://www.cdc.gov/nchs/icd/icd-10-cm/
- World Health Organization. *ICD-11 Implementation.* https://www.who.int/standards/classifications/frequently-asked-questions/icd-11-implementation

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
