# 🕵️‍♀️ Informatics Tool: Denial Detective (RCM Python Script)

### **RCM Informatics Objective**
The primary objective of this project is to automate the analysis of denied claims (835 ERA files) using RCM Informatics. This Python tool uses specialized Informatics logic—bridging standard Claim Adjustment Reason Codes (CARCs) with actionable CDI workflows—to minimize "Denial-to-Response Lag."

---

## 🚀 The Financial & Documentation Challenge
Traditional RCM denial management is a manually intensive process. Claims may remain denied for weeks before an actionable query is triggered. This massive lag in cash flow is an audit risk. This tool eliminates the manual lag by instantly identifying and analyzing the root cause of every denial.

---

## 🛠️ The Technical RCM Workflow (Python Logic Loop)

This tool follows this specific technical logic flow:

1.  **Ingest Claim Data:** The script is fed a raw list of denied claims.
2.  **Informatics Audit:** The script uses `pandas` (a data library) to filter and segment claims by specific rules:
    * **Rule A: Is denial "CARC 16" (CDI Issue)?** If yes, tag for immediate CDI audit loop.
    * **Rule B: Is denial "CARC 18" (RPM/Event Capture Issue)?** If yes, tag for immediate clinical device data check.
3.  **Action Trigger:** The script outputs a prioritized summary (the "CDI Audit Trigger") that alerts providers to correct documentation integrity.

```mermaid
graph TD
    %% Tool Data Stream
    A[Denied Claims Data] -->|Injects| B[Python Script: Denial Detective Tool]
    B -->|Rules Engine| C{Informatics Logic Check}

    %% RCM Informatics Decisions
    C -->|CARC 16: CDI Query Triggered| D(Immediate CDI Review & Root Cause Analysis)
    C -->|CARC 18: RPM Data Capture Query Triggered| E(Immediate RPM Data Loop Check)
    D & E -->|wait loop: 24h| C
    C -->|Trigger: Incomplete CDI/RPM Pass| F(Actionable & Documented for Resubmission)

    %% Styles
    style C fill:#f9f,stroke:#333,stroke-width:2px;
