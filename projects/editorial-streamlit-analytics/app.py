"""Volunteer CareFlow Systems — Revenue Cycle Intelligence (synthetic portfolio lab).

No patient data, live payer records, authenticated accounts or persistent records.
"""

from datetime import datetime, timedelta
from html import escape
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

ORANGE = "#FF8200"
INK = "#0B0B0B"
GRAY = "#626262"
PALE = "#F5F5F3"
PLOT_GRID = "#ECECEA"
PAYERS = ("Payer A", "Payer B", "Payer C", "Payer D")
SERVICES = ("Primary Care", "Specialty", "Imaging", "Outpatient Surgery")
REASONS = (
    "Eligibility",
    "Authorization",
    "Documentation",
    "Coding",
    "Payer processing",
    "Timely filing",
)
BUCKETS = ("0–30 days", "31–60 days", "61–90 days", "91+ days")


@st.cache_data(show_spinner=False)
def generate_claims(as_of_text: str) -> pd.DataFrame:
    """Seeded, reproducible fictitious claims; not an industry benchmark."""
    rng = np.random.default_rng(20261110)
    as_of = pd.Timestamp(as_of_text)
    records = []
    for number in range(1, 3001):
        days_since = int(rng.integers(0, 271))
        submitted = as_of - pd.Timedelta(days=days_since)
        payer = str(rng.choice(PAYERS, p=[0.29, 0.27, 0.25, 0.19]))
        service = str(rng.choice(SERVICES, p=[0.33, 0.28, 0.23, 0.16]))
        charge = round(float(np.clip(rng.lognormal(7.05, 0.83), 130, 18000)), 2)
        eligibility_ok = bool(rng.random() < 0.92)
        auth_required = service in ("Imaging", "Outpatient Surgery") or bool(rng.random() < 0.14)
        auth_ok = (not auth_required) or bool(rng.random() < 0.91)
        documentation_ok = bool(rng.random() < 0.93)
        coding_ok = bool(rng.random() < 0.96)
        intake_ok = eligibility_ok and documentation_ok
        clean = intake_ok and auth_ok and coding_ok

        denial_chance = (
            0.055
            + (0.27 if not eligibility_ok else 0.0)
            + (0.28 if not auth_ok else 0.0)
            + (0.18 if not documentation_ok else 0.0)
            + (0.15 if not coding_ok else 0.0)
        )
        denied = bool(rng.random() < min(denial_chance, 0.85))
        if denied:
            status = "Appealed" if rng.random() < 0.26 else "Denied"
            if not eligibility_ok:
                reason = "Eligibility"
            elif not auth_ok:
                reason = "Authorization"
            elif not documentation_ok:
                reason = "Documentation"
            elif not coding_ok:
                reason = "Coding"
            else:
                reason = str(rng.choice(["Payer processing", "Timely filing", "Coding"]))
        else:
            paid_probability = 0.25 if days_since < 15 else (0.57 if days_since < 45 else 0.80)
            status = "Paid" if rng.random() < paid_probability else "Pending"
            reason = ""

        paid = round(charge * float(rng.uniform(0.57, 0.94)), 2) if status == "Paid" else 0.0
        open_ar = charge if status != "Paid" else 0.0
        days_open = days_since if status != "Paid" else 0
        if status == "Paid":
            aging = "Closed"
        elif days_open <= 30:
            aging = BUCKETS[0]
        elif days_open <= 60:
            aging = BUCKETS[1]
        elif days_open <= 90:
            aging = BUCKETS[2]
        else:
            aging = BUCKETS[3]
        records.append({
            "Claim ID": f"DEMO-{number:05d}",
            "Submitted": submitted,
            "Payer": payer,
            "Service Line": service,
            "Charge": charge,
            "Paid": paid,
            "Open A/R": open_ar,
            "Status": status,
            "Denial": denied,
            "Denial Reason": reason,
            "Intake Complete": intake_ok,
            "Authorization": "Not required" if not auth_required else ("Verified" if auth_ok else "Missing"),
            "First-Pass Clean": clean,
            "Days Open": days_open,
            "Aging Bucket": aging,
        })
    return pd.DataFrame(records)


def money(value: float, decimals: bool = False) -> str:
    amount = abs(float(value))
    if amount >= 1_000_000:
        return ("-$" if value < 0 else "$") + f"{amount / 1_000_000:.2f}M"
    if amount >= 10_000:
        return ("-$" if value < 0 else "$") + f"{amount / 1_000:.1f}K"
    return ("-$" if value < 0 else "$") + f"{amount:,.2f}" if decimals else (
        ("-$" if value < 0 else "$") + f"{amount:,.0f}"
    )


def rate(top: float, bottom: float) -> float:
    return 100.0 * float(top) / float(bottom) if bottom else 0.0


def metrics(frame: pd.DataFrame) -> dict:
    n = len(frame)
    denied = int(frame["Denial"].sum())
    open_items = frame.loc[frame["Open A/R"] > 0]
    return {
        "claims": n,
        "denied": denied,
        "denial_rate": rate(denied, n),
        "clean_rate": rate(frame["First-Pass Clean"].sum(), n),
        "open_ar": float(frame["Open A/R"].sum()),
        "avg_days": float(open_items["Days Open"].mean()) if not open_items.empty else 0.0,
        "open_count": len(open_items),
    }


def charts(fig, *, height=335, percent=False):
    fig.update_layout(
        height=height,
        margin=dict(l=10, r=10, t=16, b=12),
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        font=dict(family="DM Sans, Arial, sans-serif", color=INK, size=12),
        xaxis=dict(gridcolor=PLOT_GRID, zeroline=False, showline=False),
        yaxis=dict(gridcolor=PLOT_GRID, zeroline=False, showline=False),
        hoverlabel=dict(bgcolor=INK, font_color="#FFFFFF"),
        legend=dict(orientation="h", y=1.15, x=0),
    )
    if percent:
        fig.update_yaxes(ticksuffix="%")
    return fig


def display_table(frame: pd.DataFrame, *, key: str) -> None:
    visible = frame.copy()
    if "Submitted" in visible.columns:
        visible["Submitted"] = visible["Submitted"].dt.strftime("%Y-%m-%d")
    for field in ("Denial", "First-Pass Clean", "Intake Complete"):
        if field in visible.columns:
            visible[field] = visible[field].map({True: "Yes", False: "No"})
    st.dataframe(
        visible,
        use_container_width=True,
        hide_index=True,
        height=350,
        column_config={
            "Charge": st.column_config.NumberColumn(format="$%.2f"),
            "Paid": st.column_config.NumberColumn(format="$%.2f"),
            "Open A/R": st.column_config.NumberColumn(format="$%.2f"),
        },
    )
    st.download_button(
        "Export these synthetic records · CSV",
        data=visible.to_csv(index=False).encode("utf-8"),
        file_name=f"volunteer-careflow-{key}-demo.csv",
        mime="text/csv",
        disabled=visible.empty,
        key=f"export_{key}",
    )


def metric_cards(items):
    blocks = []
    for eyebrow, value, description in items:
        blocks.append(
            '<section class="vc-metric">'
            f'<div class="vc-metric-label">{escape(eyebrow)}</div>'
            f'<div class="vc-metric-value">{escape(value)}</div>'
            f'<div class="vc-metric-note">{escape(description)}</div>'
            '</section>'
        )
    st.html('<div class="vc-metrics">' + "".join(blocks) + "</div>")


def style():
    st.html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');
:root { color-scheme: light; }
html, body, .stApp, p, button, input, select, textarea,
[data-testid="stMarkdownContainer"], [data-testid="stWidgetLabel"] {
  font-family: 'DM Sans', 'Helvetica Neue', Arial, sans-serif !important;
}
.stApp { background: #FFFFFF; color: #0B0B0B; }
.block-container { max-width: 1180px; padding: 1.25rem 1rem 4rem; }
header[data-testid="stHeader"] { background: rgba(255,255,255,.96); }
h1, h2, h3 { font-family: 'DM Sans', Arial, sans-serif !important;
  letter-spacing: -.035em !important; color: #0B0B0B !important; }
h3 { font-weight: 700 !important; }
.stTabs [data-baseweb="tab-list"] {
  gap: .4rem; overflow-x: auto; border-bottom: 1px solid #E8E8E8;
}
.stTabs [data-baseweb="tab"] {
  color: #0B0B0B; font-size: .89rem; font-weight: 700;
  white-space: nowrap; padding: .9rem 1rem;
}
.stTabs [aria-selected="true"] { color: #BD5C00 !important; }
div[data-testid="stVerticalBlockBorderWrapper"] > div { border-radius: 16px; }
button[kind="primary"] { background: #FF8200; border: #FF8200; color: #0B0B0B; }
button { border-radius: 11px !important; }
div[data-testid="stDownloadButton"] button {
  background: #FF8200; color: #0B0B0B; border: 1px solid #FF8200;
  font-weight: 700; min-height: 44px;
}
div[data-testid="stDataFrame"] { border: 1px solid #E7E7E7; border-radius: 14px; }
.vc-brandrow { display: flex; gap: 11px; align-items: center; margin: 0 0 24px; }
.vc-mark { display: grid; place-items: center; width: 40px; height: 40px;
  background: #FF8200; color: #0B0B0B; font-size: 20px; font-weight: 800;
  border-radius: 12px; }
.vc-brand { font-size: 15px; font-weight: 800; letter-spacing: -.03em; line-height: 1.1; }
.vc-brand small { display: block; font-size: 10px; font-weight: 700;
  color: #6A6A6A; letter-spacing: .12em; margin-top: 5px; }
.vc-hero {
  border-radius: 23px; padding: clamp(22px, 5vw, 42px);
  background: #0B0B0B; color: #FFFFFF;
  border-bottom: 5px solid #FF8200; margin: 0 0 20px;
  background-image: radial-gradient(circle at 100% 0%, #252525 0, transparent 58%);
}
.vc-eyebrow { font-weight: 800; font-size: 11px; letter-spacing: .19em;
  color: #FF9B2F; text-transform: uppercase; }
.vc-hero h1 { margin: 13px 0 12px !important; color: #FFFFFF !important;
  font-size: clamp(30px, 5vw, 56px) !important; font-weight: 800;
  max-width: 820px; line-height: 1.06; letter-spacing: -.055em !important; }
.vc-hero p { margin: 0; color: #DEDEDE; font-size: clamp(13px, 2vw, 15px);
  max-width: 750px; line-height: 1.55; }
.vc-disclosure { border-left: 3px solid #FF8200; padding: 12px 16px;
  background: #FAF9F7; color: #424242; border-radius: 0 10px 10px 0;
  font-size: 12px; line-height: 1.5; margin-bottom: 16px; }
.vc-metrics { display: grid; grid-template-columns: repeat(4, minmax(0,1fr));
  gap: 12px; margin: 19px 0 24px; }
.vc-metric { min-width: 0; border: 1px solid #E9E9E6; border-radius: 17px;
  padding: 20px 18px 17px; background: #FFFFFF;
  box-shadow: 0 8px 28px rgba(0,0,0,.035); position: relative; }
.vc-metric:before { content:""; position:absolute; top:0; left:18px;
  height:3px; width:42px; background:#FF8200; }
.vc-metric-label { font-size: 12px; color:#595959; font-weight: 700;
  min-height: 30px; }
.vc-metric-value { color: #0B0B0B; font-size: clamp(23px, 3.5vw, 35px);
  font-weight: 800; letter-spacing: -.055em; line-height: 1.1;
  margin: 7px 0 11px; overflow-wrap: anywhere; }
.vc-metric-note { font-size: 11px; color: #686868; line-height: 1.4; }
.vc-section { display:flex; align-items: center; gap: 8px; margin: 16px 0 8px; }
.vc-accent { width:7px; height:21px; border-radius: 4px; background:#FF8200; }
.vc-section h2 { margin: 0 !important; font-weight:800;
  font-size: clamp(20px, 2.9vw, 28px) !important; }
.vc-foot { font-size: 11px; color: #666; line-height: 1.5; margin-top: 18px; }
@media (max-width: 830px) {
 .vc-metrics { grid-template-columns: repeat(2, minmax(0,1fr)); }
 .vc-metric { padding: 18px 14px 16px; }
 .block-container { padding-left: .7rem; padding-right: .7rem; }
}
@media (max-width: 440px) {
 .vc-hero { padding: 23px 20px; border-radius: 18px; }
 .vc-metric-label { font-size: 11px; }
 .vc-metric-note { font-size: 10px; }
 .vc-metric-value { font-size: 25px; }
 .stTabs [data-baseweb="tab"] { padding: .75rem .7rem; }
}
@media (prefers-reduced-motion: reduce) {
  *, *:before, *:after { animation: none !important; transition: none !important; }
}
</style>
""")


def section(title: str):
    st.html('<div class="vc-section"><span class="vc-accent"></span>'
            f'<h2>{escape(title)}</h2></div>')


def app():
    st.set_page_config(
        page_title="Volunteer CareFlow | Revenue Cycle Intelligence",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    style()
    st.html("""
<div class="vc-brandrow">
  <div class="vc-mark">V</div>
  <div class="vc-brand">Volunteer CareFlow Systems
    <small>HEALTHCARE OPERATIONS / INTELLIGENCE LAB</small>
  </div>
</div>
<div class="vc-hero">
  <div class="vc-eyebrow">01 / REVENUE CYCLE INTELLIGENCE</div>
  <h1>Clarity at every<br>claim decision.</h1>
  <p>An interactive healthcare operations command center for denial analysis,
  accounts receivable, first-pass quality, and workflow scenarios.</p>
</div>
<div class="vc-disclosure"><b>SYNTHETIC DATA · PUBLIC DEMONSTRATION</b> —
  All claims, payers, dollar amounts, workflow outcomes and scenarios are fictional.
  No PHI, real payer connections, live billing system, or production security controls.</div>
""")
    as_of = datetime.now(ZoneInfo("America/Chicago")).date().isoformat()
    source = generate_claims(as_of)

    with st.expander("REFINE THE DATASET · PAYER / SERVICE / REPORTING WINDOW", expanded=False):
        one, two = st.columns(2)
        with one:
            window = st.selectbox(
                "Reporting period", ("All 270 days", "Last 30 days", "Last 90 days", "Last 180 days"),
                index=0,
            )
            selected_payers = st.multiselect("Payer", PAYERS, default=list(PAYERS))
        with two:
            service = st.selectbox("Service line", ("All service lines", *SERVICES))
            status_filter = st.selectbox(
                "Claim status", ("All statuses", "Paid", "Pending", "Denied", "Appealed")
            )
    frame = source.copy()
    if window != "All 270 days":
        days = {"Last 30 days": 30, "Last 90 days": 90, "Last 180 days": 180}[window]
        threshold = pd.Timestamp(as_of) - pd.Timedelta(days=days-1)
        frame = frame.loc[frame["Submitted"] >= threshold]
    frame = frame.loc[frame["Payer"].isin(selected_payers)]
    if service != "All service lines":
        frame = frame.loc[frame["Service Line"] == service]
    if status_filter != "All statuses":
        frame = frame.loc[frame["Status"] == status_filter]

    m = metrics(frame)
    st.caption(
        f"DEMO DATASET · {m['claims']:,} filtered of {len(source):,} fictional claims · "
        f"Model date {as_of} · Filters apply across all workspaces"
    )
    metric_cards([
        ("Open A/R · gross charges", money(m["open_ar"]), f"{m['open_count']:,} unpaid sample claims"),
        ("Denial incidence", f"{m['denial_rate']:.1f}%", f"{m['denied']:,} denied / appealed claims"),
        ("First-pass clean rate", f"{m['clean_rate']:.1f}%", "Synthetic intake and coding checks"),
        ("Average open aging", f"{m['avg_days']:.0f} days", "Unweighted mean on open claims"),
    ])
    tabs = st.tabs([
        "Advanced Intelligence",
        "Command Center",
        "Denial Intelligence",
        "A/R Workbench",
        "Scenario Studio",
        "Claim Explorer",
    ])

    with tabs[0]:
        from advanced_workbench import render_advanced
        render_advanced(frame)

    with tabs[1]:
        section("Claim quality across time")
        st.caption("Weekly submission and denial trends. Each point is derived from the selected fictional claims.")
        if frame.empty:
            st.info("No claims match your filter combination. Expand the filters and try again.")
        else:
            weekly = (
                frame.groupby(pd.Grouper(key="Submitted", freq="W-MON"))
                .agg(Claims=("Claim ID", "count"), Denied=("Denial", "sum"))
                .reset_index()
            )
            weekly["Denial incidence (%)"] = weekly.apply(
                lambda row: rate(row["Denied"], row["Claims"]), axis=1
            )
            trend = px.line(
                weekly,
                x="Submitted", y="Denial incidence (%)",
                markers=True, color_discrete_sequence=[ORANGE],
                labels={"Submitted": "Week of"},
            )
            trend.update_traces(line_width=3, marker_size=5)
            st.plotly_chart(charts(trend, percent=True), use_container_width=True)

            section("Payer performance breakdown")
            by_payer = (
                frame.groupby("Payer", as_index=False)
                .agg(Claims=("Claim ID", "count"), Denied=("Denial", "sum"))
            )
            by_payer["Denial rate (%)"] = by_payer.apply(
                lambda row: rate(row["Denied"], row["Claims"]), axis=1
            )
            bar = px.bar(
                by_payer.sort_values("Denial rate (%)"),
                x="Denial rate (%)", y="Payer", orientation="h",
                color_discrete_sequence=[ORANGE], text="Denial rate (%)",
            )
            bar.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
            bar.update_xaxes(ticksuffix="%")
            st.plotly_chart(charts(bar, height=285), use_container_width=True)
            st.caption("Payer A–D are invented entities; comparisons are not benchmarks.")
        st.markdown("---")
        st.markdown("**Method:** Denial incidence = denied or appealed ÷ submitted claims. "
                    "The clean rate measures demonstration intake/coding criteria and does not "
                    "represent a measured payer acceptance rate.")

    with tabs[2]:
        section("Denial intelligence")
        st.caption("Root causes, prioritization, and a real filtered worklist for this simulation.")
        denied = frame.loc[frame["Denial"]].copy()
        if denied.empty:
            st.info("No denied or appealed claims in this selection.")
        else:
            causes = (
                denied.groupby("Denial Reason", as_index=False)
                .agg(Claims=("Claim ID", "count"), Gross_Charges=("Charge", "sum"))
                .sort_values("Claims")
            )
            fig = px.bar(
                causes, x="Claims", y="Denial Reason", orientation="h",
                color_discrete_sequence=[ORANGE], text="Claims",
            )
            fig.update_layout(xaxis_title="Claims", yaxis_title="")
            st.plotly_chart(charts(fig), use_container_width=True)
            a, b = st.columns(2)
            with a:
                chosen_reason = st.selectbox(
                    "Investigate root cause",
                    ["All reasons", *sorted(denied["Denial Reason"].unique())],
                )
            with b:
                threshold = st.select_slider(
                    "Queue priority", ["All tiers", "Tier 1", "Tier 2", "Tier 3"],
                    value="All tiers",
                )
            queue = denied.copy()
            if chosen_reason != "All reasons":
                queue = queue.loc[queue["Denial Reason"] == chosen_reason]
            queue["Priority"] = np.select(
                [
                    (queue["Charge"] >= 3000) | (queue["Days Open"] >= 120),
                    (queue["Charge"] >= 1000) | (queue["Days Open"] >= 60),
                ],
                ["Tier 1", "Tier 2"], default="Tier 3",
            )
            if threshold != "All tiers":
                queue = queue.loc[queue["Priority"] == threshold]
            queue = queue.sort_values(
                ["Charge", "Days Open"], ascending=[False, False]
            )
            st.caption(f"{len(queue):,} matching denied/appealed claims · "
                       f"{money(queue['Charge'].sum())} gross charges represented")
            display_table(
                queue[[
                    "Claim ID", "Submitted", "Payer", "Status", "Denial Reason",
                    "Charge", "Days Open", "Priority", "Authorization", "Intake Complete"
                ]],
                key="denials",
            )
            st.caption("Priority tiers use illustrative charge/age rules, not actual payer timely-filing limits. "
                       "Gross charges are not recoverable cash projections.")

    with tabs[3]:
        section("A/R aging workbench")
        st.caption("Unpaid sample claim charges by age. Amounts are gross, not adjusted net receivables.")
        open_items = frame.loc[frame["Open A/R"] > 0].copy()
        if open_items.empty:
            st.info("No open accounts receivable in the current selection.")
        else:
            aging = open_items.groupby("Aging Bucket")["Open A/R"].sum().reindex(
                BUCKETS, fill_value=0
            ).reset_index()
            aging.columns = ["Age", "Gross open A/R"]
            fig = px.bar(
                aging, x="Age", y="Gross open A/R",
                color="Age", color_discrete_sequence=[
                    "#171717", "#6D6D6D", ORANGE, "#F4A747"
                ], text="Gross open A/R",
            )
            fig.update_traces(texttemplate="$%{text:,.0f}", textposition="outside")
            fig.update_layout(showlegend=False)
            st.plotly_chart(charts(fig), use_container_width=True)
            aging_filter = st.selectbox(
                "Drill into aging bucket", ("All open claims", *BUCKETS)
            )
            work = open_items.copy()
            if aging_filter != "All open claims":
                work = work.loc[work["Aging Bucket"] == aging_filter]
            work = work.sort_values(["Days Open", "Open A/R"], ascending=False)
            st.caption(f"{len(work):,} open claims · {money(work['Open A/R'].sum())} "
                       "gross open charges in this worklist")
            display_table(
                work[[
                    "Claim ID", "Submitted", "Payer", "Service Line",
                    "Status", "Open A/R", "Days Open", "Aging Bucket",
                ]],
                key="aging",
            )
        st.caption("Open A/R is modeled as the original gross charge on unpaid claims. "
                   "It excludes allowances, partial payments, bad-debt estimates, and actual collectible value.")

    with tabs[4]:
        section("Scenario studio")
        st.caption("Move the sliders to model hypothetical workload effects. Nothing is written to a database.")
        eligible_causes = frame.loc[
            frame["Denial"] & frame["Denial Reason"].isin(["Eligibility", "Authorization"])
        ]
        base_count = len(eligible_causes)
        base_charge = float(eligible_causes["Charge"].sum())
        l, r = st.columns(2)
        with l:
            reduction = st.slider(
                "Hypothetical preventable denial reduction", 0, 75, 25, 5,
                format="%d%%",
            )
        with r:
            rework_cost = st.slider(
                "Assumed administrative rework cost per claim ($)", 0, 150, 35, 5,
            )
        prevented = round(base_count * reduction / 100)
        avoid_cost = prevented * rework_cost
        affected_charge = base_charge * reduction / 100
        metric_cards([
            ("Eligible demo denials", f"{base_count:,}", "Eligibility + authorization"),
            ("Illustrative cases avoided", f"{prevented:,}", "Rounded claim count"),
            ("Illustrative rework cost avoided", money(avoid_cost), "Cases avoided × assumed cost"),
            ("Gross charges in affected group", money(affected_charge), "NOT projected reimbursement"),
        ])
        section("Assumption sensitivity")
        options = list(range(0, 76, 5))
        sensitivity = pd.DataFrame({
            "Improvement assumption (%)": options,
            "Administrative cost avoidance ($)": [
                round(base_count * x / 100) * rework_cost for x in options
            ],
        })
        fig = px.area(
            sensitivity,
            x="Improvement assumption (%)",
            y="Administrative cost avoidance ($)",
        )
        fig.update_traces(
            line_color=ORANGE, fillcolor="rgba(255,130,0,0.17)"
        )
        st.plotly_chart(charts(fig), use_container_width=True)
        st.caption("This model treats a specified portion of eligibility and authorization denials "
                   "as preventable and applies a user-selected rework-cost assumption. "
                   "No causal effect, recovered cash, ROI, or financial outcome is verified.")

    with tabs[5]:
        section("Claim explorer")
        st.caption("Search across identifiers and choose which data to export.")
        a, b = st.columns(2)
        with a:
            query = st.text_input(
                "Search claim ID or payer", placeholder="DEMO-00001 or Payer A"
            ).strip()
        with b:
            order = st.selectbox(
                "Sort records",
                ("Newest first", "Oldest first", "Largest charge", "Most days open")
            )
        show = frame.copy()
        if query:
            mask = (
                show["Claim ID"].str.contains(query, case=False, regex=False)
                | show["Payer"].str.contains(query, case=False, regex=False)
            )
            show = show.loc[mask]
        sort = {
            "Newest first": ("Submitted", False),
            "Oldest first": ("Submitted", True),
            "Largest charge": ("Charge", False),
            "Most days open": ("Days Open", False),
        }
        field, asc = sort[order]
        show = show.sort_values(field, ascending=asc)
        st.caption(f"{len(show):,} matching fictional claims")
        display_table(show, key="explorer")
        with st.expander("Data dictionary and limitations"):
            st.markdown(
                "**Denial:** Includes both denied and appealed claims. "
                "**First-Pass Clean:** Synthetic eligibility, documentation, "
                "authorization, and coding checks. "
                "**Open A/R:** Gross charge if unpaid; not net collectible revenue. "
                "**Days Open:** Days since submission for unpaid claims. "
                "**Modeling:** Sample records are generated from a fixed random seed. "
                "No real patients, actual payer transactions, EHR, PHI, live APIs, "
                "authentication, HIPAA compliance, or persistent edits."
            )

    st.html(
        '<div class="vc-foot">VOLUNTEER CAREFLOW SYSTEMS / INTELLIGENCE LAB'
        ' &nbsp; · &nbsp; Synthetic portfolio demonstration'
        ' &nbsp; · &nbsp; Not intended for clinical, billing or financial decisions.</div>'
    )


if __name__ == "__main__":
    # Premium mobile-first portal replaces the legacy Streamlit layout.
    from visual_portal import launch
    launch()
