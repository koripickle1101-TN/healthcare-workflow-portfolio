# 📊 Informatics Process Map: AI CDI & RCM Workflow (Lag Reduction)

### **Workflow Description**
This process map visualizes the logic flow that minimizes "Lag Days" in remote cardiac monitoring. The central "EHR AI CDI Audit Loop" ensures 100% data integrity before triggering a billing event, reducing audit risk and denials.

---

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
