# 🏛️ Public Health Informatics: The PERIE Framework (Diabetes Analytics)

### **Informatics Objective**
The primary objective of this project is to apply the evidence-based PERIE framework to analyze the public health crisis of adult diabetes in Mascot, TN. This analysis uses standard Informatics methods to bridge epidemiological data (prevalence) with actionable Informatics intervention and Revenue Cycle optimization.

---

## 🔍 Etiology: The Data Gap (LAG and Denial Detective)

### **1. 🔍 Problem (Mascot, TN - Adult Diabetes)**
| Data Metric | Value | Informatics Source |
| :--- | :--- | :--- |
| Population | ~2,500 Adults (Mascot, TN 2026 Est.) | U.S. Census Bureau/Loc. Registry |
| Adult Diabetes Prevalence | **14.2%** (Tennessee Average is ~12%) | CDC / TN Dept. of Health |
| Estimated Mascot Cases | **~355 Adults** | Informatics Projection |

### **2. 🚀 Intervention Workflow (Reducing the Lag)**
This framework defines the evidence-based process from problem identification to final impact analysis. We use specified language to bridge the Mascot registry with actionable clinical outcomes.

```mermaid
graph TD
    %% Problem and Intervention Stream
    A[Mascot Registry Trigger: Adult Diabetes Cases] -->|14.2% Prevalence Data| B{Cardiac Event Capture Workflow}
    B -->|AI-Driven CDI Logic Pass| C{Informatics Logic Check}
    
    %% RCM Informatics Decisions
    C -->|Trigger: Incomplete CDI/RPM Pass| D(Wait Loop 24h: Documentation Integrity Audit)
    D -->|Injects| C
    C -->|Trigger: CDI Complete| E[CPT 99457 Billing Draft Generated]
    E -->|Workflow Result: Lag Days < 2| F(Actionable & Documented for Resubmission)

    %% Brand Styles: Orange, Black, Gray, and White
    %% Gray Background for main nodes
    style A fill:#D6D6D6,stroke:#333,stroke-width:2px;
    style B fill:#D6D6D6,stroke:#333,stroke-width:2px;
    style C fill:#D6D6D6,stroke:#333,stroke-width:2px;
    style D fill:#D6D6D6,stroke:#333,stroke-width:2px;

    %% White Background for outcomes
    style E fill:#FFFFFF,stroke:#333,stroke-width:2px;

    %% Orange Background for final success
    style F fill:#F97316,stroke:#333,stroke-width:2px;
