import streamlit as st
import pandas as pd
import plotly.express as px
from components.styles import inject_global_css
from components.header import render_sidebar_header

st.set_page_config(page_title="Denials Management | Kori Pickle", page_icon="🚫", layout="wide")
inject_global_css()
render_sidebar_header()

st.markdown("<div class='page-header'><div class='page-header-eyebrow'>Section 04 · Denial Prevention</div><div class='page-header-title'>Denials Management</div><div class='page-header-sub'>Root cause pattern analysis · Repeat denial identification · Prevention checkpoints</div></div>", unsafe_allow_html=True)
st.markdown("<div class='orange-callout'><strong>Core Argument:</strong> A denial is not a billing problem — it is a workflow failure that started upstream. Sustainable denial reduction requires identifying where the process broke, not just resubmitting the claim.</div>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Denial Patterns", "Repeat Denials", "Prevention Plan"])

with tab1:
    st.markdown("### Denial Volume by Payer and Type (Synthetic Data)")
    df = pd.DataFrame({
        "Payer": ["United","Cigna","Aetna","BCBS","Medicaid","Medicare Adv"],
        "Authorization": [18,14,8,11,6,3],
        "Eligibility": [12,9,7,8,14,4],
        "Coding": [6,8,5,7,3,4],
        "Documentation": [9,6,4,5,8,2]
    })
    df_melt = df.melt(id_vars="Payer", var_name="Denial Type", value_name="Volume")
    color_map = {"Authorization": "#FF8200", "Eligibility": "#E86B00", "Coding": "#C45500", "Documentation": "#FF9A33"}
    fig = px.bar(df_melt, x="Payer", y="Volume", color="Denial Type", barmode="stack", title="Denial Volume by Payer and Type", color_discrete_map=color_map)
    fig.update_layout(plot_bgcolor="white", paper_bgcolor="white", font_family="Inter")
    st.plotly_chart(fig, use_container_width=True)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Top Denial Payer", "United Healthcare")
    c2.metric("Top Denial Type", "Authorization — 60")
    c3.metric("Eligibility Denials", "54 cases")
    c4.metric("Preventable Denials", "73%")

with tab2:
    st.markdown("### Repeat Denial Patterns — High Risk Accounts")
    for account, count, reason, action in [
        ("PT-1042","4 denials","Authorization not obtained before service","Escalate to PA team. Flag account for pre-service PA verification."),
        ("PT-2187","3 denials","Eligibility error — wrong payer billed","Audit registration. Re-verify insurance at every visit."),
        ("PT-3301","3 denials","Missing documentation — medical necessity","Clinical team to complete documentation template before billing."),
        ("PT-4455","2 denials","Timely filing — claims submitted after deadline","Review submission workflow. Automate claim submission within 48 hours."),
    ]:
        st.markdown(f"<div class='info-card'><div class='info-card-title'>{account} — {count} — {reason}</div><div class='info-card-body'>{action}</div></div>", unsafe_allow_html=True)

with tab3:
    st.markdown("### Denial Prevention Checkpoint Plan")
    for i, (title, desc) in enumerate([
        ("Eligibility verified at scheduling and check-in","Two-touch verification catches coverage changes before service."),
        ("Authorization confirmed before procedure or service","No auth, no service. PA must be in hand before the appointment."),
        ("Coding reviewed against diagnosis and documentation","CPT and ICD-10 codes must match the clinical note exactly."),
        ("Documentation supports medical necessity","If the chart does not justify the service, the claim will be denied."),
        ("Claims submitted within 5 business days of service","Timely filing windows vary by payer — 90 days is the common minimum."),
        ("Denial root causes tracked and reported weekly","Pattern data drives process improvement. Track every denial by root cause."),
        ("Appeals filed within payer deadline with supporting documentation","First-level appeals with strong documentation reverse 60-70% of denials."),
    ], 1):
        st.markdown(f"<div class='process-step'><div class='step-num'>{i}</div><div><div class='step-title'>{title}</div><div class='step-desc'>{desc}</div></div></div>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<div class='footer'><div class='footer-created'>Created by</div><div class='footer-signature'>Kori Pickle</div><div class='footer-icons'><a class='footer-icon-link' href='https://github.com/koripickle1101-TN' target='_blank'>GH</a><a class='footer-icon-link' href='https://linkedin.com' target='_blank'>in</a></div></div>", unsafe_allow_html=True)
