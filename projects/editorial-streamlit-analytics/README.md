# Volunteer CareFlow Systems — Revenue Cycle Intelligence

**Premium interactive Streamlit portfolio demonstration · 100% synthetic healthcare claims.**

This dashboard has five working workspaces: **Command Center**, **Denial Intelligence**, **A/R Workbench**, **Scenario Studio**, and **Claim Explorer**. It uses Volunteer CareFlow Systems branding: pure white \`#FFFFFF\`, Tennessee Orange \`#FF8200\`, black \`#0B0B0B\`, editorial DM Sans, mobile-friendly two-column KPI cards, a dark editorial hero, and expandable global filtering controls.

## Public demo link

https://volunteer-careflow-analytics.streamlit.app

The link is independently deployed through Streamlit Community Cloud from the \`feat/editorial-streamlit-analytics-demo-2026-11\` branch, not the repository's \`main\` branch. Pushing a change to the selected GitHub branch will prompt Community Cloud to update the app. This repository does not prove live uptime or test all mobile browsers.

## Interactive features

- Global filters: reporting window, 4 fictional payers, 4 service lines, and claim status.
- Executive KPI cards derived from all active filters: gross open A/R, denial incidence, first-pass clean rate, and mean days open.
- Weekly denial trend and fictional payer comparisons.
- Denial reason frequency chart with reason and priority drilldowns, sortable/searchable Streamlit tables, filtered CSV downloads.
- Gross A/R aging analysis, bucketing (0–30, 31–60, 61–90, 91+ days), and per-bucket ledger.
- Scenario sliders for hypothetical preventable denial reduction and administrative cost per rework case, with sensitivity visualization.
- Claim ID/payer text search, sorting, table inspection and CSV export.
- Responsive KPI cards; collapsible filters; scrolling workspace tabs; reduced-motion preference respected in styling.

## Reproducible demonstration model

The Python app generates 3,000 **fictional** claims using NumPy's random generator with seed \`20261110\`, dated within a rolling 270-day window using the current date in \`America/Chicago\`. All payer labels are invented; \`Payer A\`–\`Payer D\` do not identify actual insurance companies. Any displayed rate or gross-dollar amount is computed from those synthetic rows.

| Metric | Calculation | Scope |
| --- | --- | --- |
| Denial incidence | (Denied + Appealed) / all filtered claims × 100 | Not a payer-reported first-pass denial benchmark |
| First-pass clean rate | Claims passing fictional eligibility, authorization, documentation, and coding gates / all filtered claims × 100 | Simulated operational check |
| Gross open A/R | Sum of full original charge on all unpaid filtered claims | **Not** adjusted accounts receivable or estimated collections |
| Average open aging | Arithmetic mean of days since submission for currently unpaid claims | Not a weighted industry-standard days-in-A/R figure |
| Denial priority | Tier 1 if charge ≥ $3,000 or open days ≥ 120; Tier 2 if charge ≥ $1,000 or open days ≥ 60; otherwise Tier 3 | Illustrative, not payer-specific timely-filing logic |
| Scenario cost avoidance | Rounded eligible denial count × improvement % × user-selected rework cost | Not verified savings or ROI |

**No real patient data, personal health information (PHI), database, payer API, EHR integration, authentication, HIPAA security controls, persistent edits, or real revenue** are included. The app cannot be used to make operational, patient-care or financial decisions.

## Cloud deployment configuration

- Repository: \`koripickle1101-TN/healthcare-workflow-portfolio\`
- Branch: \`feat/editorial-streamlit-analytics-demo-2026-11\`
- Main Python file: \`projects/editorial-streamlit-analytics/app.py\`
- Public custom subdomain: \`volunteer-careflow-analytics\`
- Dependencies: \`projects/editorial-streamlit-analytics/requirements.txt\`
- Visual theme: \`projects/editorial-streamlit-analytics/.streamlit/config.toml\`, plus in-app CSS.

## Free operations

Streamlit Community Cloud is a no-required-subscription publishing option with platform-imposed resource limits, public visibility and no guaranteed always-on runtime. No paid APIs, secrets, or app database are needed here. Do not upload real patient data or confidential information into the public demonstration.

For optional local runs, from repository root:

\`\`\`bash
python -m pip install -r projects/editorial-streamlit-analytics/requirements.txt
streamlit run projects/editorial-streamlit-analytics/app.py
\`\`\`

## Evidence standard

The code is committed and statically inspectable in GitHub. A GitHub commit alone does not verify Streamlit Cloud runtime behavior. Validate the deployed URL in a mobile browser, check all five workspaces, filters, CSV export and error logs, then report any remaining issues. Do not claim operational savings or HIPAA compliance.
