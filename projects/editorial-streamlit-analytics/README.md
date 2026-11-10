# Editorial Analytics — Streamlit Portfolio Demonstration

Interactive analytics with fictional, reproducible sample transactions. This is a skills demonstration, **not real business performance or live revenue**.

## Brand and features

- White #FFFFFF, Tennessee Orange #FF8200, black #000000
- Editorial sans-serif typography (DM Sans, fallback Arial)
- Date, segment, and region filtering across KPIs, charts, and ledger
- Derived metrics: sample revenue, signups, clicks and signup/click rate
- Interactive Plotly trend and segment charts
- Searchable ledger and export of the current filtered CSV
- No customer information, credentials, database, or paid APIs

## Deploy online free with GitHub + Streamlit Community Cloud (Android compatible)

1. Review the draft pull request, then merge it only if you want this folder on the main branch. No existing files are overwritten.
2. Visit https://share.streamlit.io and sign in with GitHub.
3. Choose Create app, then Yup, I have an app.
4. Repository: koripickle1101-TN/healthcare-workflow-portfolio
5. Branch: main after merging (or feat/editorial-streamlit-analytics-demo-2026-11 before merging).
6. Main file path: projects/editorial-streamlit-analytics/app.py
7. Choose Deploy; Community Cloud issues a real URL only after successful deployment.

The dependency and local theme files are in this subdirectory and do not alter the hosting or design of the existing portfolio. Free-tier policies, quotas, and uptime are controlled by Streamlit.

## Optional local run

Install requirements with:

    python -m pip install -r projects/editorial-streamlit-analytics/requirements.txt

Launch from the repository root:

    streamlit run projects/editorial-streamlit-analytics/app.py

## Methodology and limits

Synthetic rows are deterministically generated using NumPy seed 42 over a trailing 365-day date range. KPI values are recalculated after the sidebar filters. Signup/click percentage equals sample signups divided by sample clicks times 100. Search applies only to ledger and CSV, not charts or top metrics. No real patient, clinical, financial, or customer information is used. This is not a live enterprise app: user accounts, data persistence, secure roles, API connections and production controls are not present.
