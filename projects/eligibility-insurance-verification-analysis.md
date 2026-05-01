# Case Study: Eligibility & Insurance Verification Analysis

**Project Type:** Self-directed portfolio case study  
**Role Simulated:** RCM / Patient Access Workflow Analyst  
**Focus Area:** Insurance verification, eligibility checks, patient access, denial prevention  
**Brand System:** White background, black text, Vols Orange `#FF8200` accents

---

## Executive Summary

This case study analyzes how eligibility and insurance verification gaps can create downstream revenue cycle problems. The purpose is to demonstrate practical workflow analysis, patient access thinking, and denial prevention logic without claiming employer or client experience.

The central question:

**How can the front-end workflow prevent eligibility-related claim failures before billing begins?**

This case study maps the verification process, identifies risk points, and proposes validation controls that could improve claim readiness and reduce avoidable rework.

---

## Scenario

A healthcare organization is experiencing recurring eligibility-related claim issues. Patient coverage is sometimes inactive, payer details may be outdated, and authorization or referral requirements are not always identified before service.

Instead of treating these as isolated claim problems, this case study evaluates the patient access workflow as a revenue cycle control point.

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

## Risk Analysis

| Workflow Point | Risk | Revenue Cycle Impact | Prevention Step |
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

## Eligibility Status Logic

| Status | Meaning | Recommended Action |
|---|---|---|
| Verified | Coverage active and payer information confirmed | Proceed with normal workflow |
| Needs Review | Coverage response unclear or incomplete | Route to verification follow-up |
| Authorization Check Needed | Coverage active but payer rules may require authorization | Confirm requirements before service |
| Coverage Issue | Coverage inactive, mismatched, or not found | Contact patient or payer before claim submission |

---

## Simulated Improvement Targets

These targets are for educational demonstration only and are not based on employer or client data.

| Metric | Current Risk Signal | Target Direction |
|---|---|---|
| Eligibility denial risk | Elevated when coverage is not verified | Reduce with pre-service verification |
| Rework volume | Higher when payer data is incomplete | Reduce with required field controls |
| Claim readiness | Inconsistent without standardized notes | Improve with clear eligibility documentation |
| Patient billing confusion | Possible when coverage issues are found late | Reduce through earlier coverage validation |

---

## Analyst Takeaway

Eligibility verification is not only an administrative step. It is a front-end revenue cycle control point.

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

This is a self-directed educational portfolio case study. It uses simulated workflow logic and general healthcare operations concepts. It does not represent client work, employer work, patient data, payer data, or protected health information.
