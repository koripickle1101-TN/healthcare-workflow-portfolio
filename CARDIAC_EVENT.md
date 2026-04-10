# 🫀 Informatics Project: Post-Discharge Cardiac Event Capture (Remote Monitoring)

### **RCM Informatics Objective**
The primary objective is to optimize the Revenue Cycle Management (RCM) stream by minimizing "Lag Days" between a patient’s out-of-hospital cardiac event and the successful billing of professional services. This workflow leverages AI-driven clinical documentation triggers to ensure 100% data integrity for remote patient monitoring billing (e.g., CPT 99457).

---

## 🚀 The Clinical & Financial Challenge
Patients with remote cardiac monitoring devices may experience critical, billable "events" (e.g., severe arrhythmia) outside of a standard office visit. In traditional workflows, these events may not be documented and billed for weeks, leading to massive financial leakage and potential data-compliance audit risks.

---

## 🛠️ The Informatics Workflow (Mermaid Process Diagram)

This process map models the flow from the clinical trigger (the remote event) to final RCM action (Billing/Denial). The "Informatics Audit Loop" is the key to minimizing lag and maximizing CDI.

```mermaid
graph TD
    %% Clinical Action Stream
    A[Remote Cardiac Device] -->|Trigger: Arrhythmia/Event| B[Device API Transmits Raw Data]
    B -->|Transfers to| C{EHR AI CDI Audit Loop}

    %% AI CDI Audit Decisions
    C -->|Trigger: Incomplete CDI| D(AI-Generated CDI Query to Provider)
    D -->|Wait Loop: 24h| C
    C -->|Trigger: CDI Complete & HIPAA Audit Pass| E[Documentation is 'Audit Ready' & Finalized]

    %% Final Financial Stream
    E -->|Automated RCM Trigger| F[CPT 99457 Claim Draft Generated]
    F -->|Sends to| G[Claim Adjudication]
    G -->|Result: Paid| H(Workflow Optimized)
    G -->|Result: Denial/Audit| I(Workflow Failed)
    
    %% Styles
    style C fill:#f9f,stroke:#333,stroke-width:2px;
    style I fill:#f66,stroke:#333,stroke-width:2px;
