# Eligibility & Insurance Verification Analysis

**Project Type:** Self-directed learning project  
**Focus Area:** Insurance verification, eligibility checks, patient access, revenue cycle risk prevention  
**Brand System:** White background, black text, Vols Orange `#FF8200` accents

---

## Project Summary

This self-directed project examines how insurance verification and eligibility accuracy affect the healthcare revenue cycle. The goal is to show practical understanding of how front-end verification gaps can create downstream claim denials, patient confusion, rework, and reimbursement delays.

This project does not use patient data, employer data, payer data, or protected health information. It is a simulated workflow analysis built for portfolio demonstration and learning.

---

## Problem Statement

Eligibility-related issues often begin before a claim is ever submitted. If coverage is inactive, payer information is entered incorrectly, or plan requirements are not confirmed, the organization may not discover the problem until after services are rendered or the claim is denied.

Common eligibility and insurance verification breakdowns include:

- Incorrect payer selected during registration
- Outdated insurance information copied forward
- Coverage not verified close enough to the service date
- Missing subscriber or policy details
- Coordination of benefits not confirmed
- Plan-specific referral or authorization rules missed
- Eligibility results not clearly documented for billing follow-up

---

## Workflow Map

```text
Patient Schedules Visit
   ↓
Insurance Information Collected
   ↓
Coverage / Eligibility Verified
   ↓
Payer Requirements Reviewed
   ↓
Authorization or Referral Need Confirmed
   ↓
Eligibility Status Documented
   ↓
Claim Prepared with Verified Coverage
```

---

## Risk Table

| Workflow Point | Risk | Possible Revenue Cycle Impact | Prevention Step |
|---|---|---|---|
| Registration | Incorrect payer entered | Claim rejection or denial | Confirm payer name and plan type |
| Insurance Capture | Missing subscriber details | Rework and claim delay | Require complete policy fields |
| Eligibility Check | Coverage not active | Eligibility denial | Verify coverage before service |
| COB Review | Other coverage not identified | Payer sequencing issue | Confirm coordination of benefits |
| Authorization Review | Requirement missed | Authorization denial | Check payer rules before service |
| Documentation | Verification result not recorded | Billing follow-up delays | Standardize eligibility notes |

---

## Proposed Verification Controls

1. Require complete insurance fields before moving the account forward.
2. Verify active coverage close to the date of service.
3. Confirm payer, plan type, subscriber details, and policy number.
4. Check coordination of benefits when multiple plans are listed.
5. Review payer-specific authorization or referral requirements.
6. Document eligibility results in a consistent format.
7. Route exceptions for review before claim submission.

---

## Sample Eligibility Status Categories

| Status | Meaning | Recommended Action |
|---|---|---|
| Verified | Coverage active and payer information confirmed | Proceed with normal workflow |
| Needs Review | Coverage response unclear or incomplete | Route to verification follow-up |
| Authorization Check Needed | Coverage active but payer rules may require authorization | Confirm requirements before service |
| Coverage Issue | Coverage inactive, mismatched, or not found | Contact patient or payer before claim submission |

---

## RCM Insight

Eligibility verification is not just an administrative task. It is a front-end revenue cycle control point.

A strong verification process helps prevent:

- Eligibility denials
- Rework loops
- Patient billing confusion
- Delayed reimbursement
- Avoidable claim follow-up

The goal is not only to collect insurance information. The goal is to validate whether the claim has a clean path forward before it enters the billing cycle.

---

## Skills Demonstrated

- Insurance verification workflow analysis
- Eligibility risk identification
- Patient access process thinking
- Revenue cycle control logic
- Claims readiness awareness
- Denial prevention strategy
- Healthcare operations communication

---

## Ethical Note

This is a self-directed educational portfolio project. It uses simulated workflow logic and general healthcare operations concepts. It does not represent client work, employer work, patient data, payer data, or protected health information.
