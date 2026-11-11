"""Advanced interactive decision workbench using fictional RCM claim records.

All annotations remain in the browser's Streamlit session; no backend persistence.
"""
from datetime import date

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

ORANGE = "#FF8200"
BLACK = "#0B0B0B"
REASONS = ["Eligibility", "Authorization", "Documentation", "Coding",
           "Payer processing", "Timely filing"]
OWNERS = ["Unassigned", "Registration", "Authorization", "Coding",
          "Billing", "Payer follow-up"]
STATUSES = ["Unreviewed", "Investigating", "Correction needed",
            "Payer follow-up", "Escalated", "Closed in demo"]


def percent(numerator, denominator):
    return 100.0 * float(numerator) / float(denominator) if denominator else 0.0


def summary(data):
    open_rows = data[data["Open A/R"] > 0]
    return dict(
        claims=len(data),
        denied=int(data["Denial"].sum()),
        denial_rate=percent(data["Denial"].sum(), len(data)),
        clean_rate=percent(data["First-Pass Clean"].sum(), len(data)),
        gross_ar=float(open_rows["Open A/R"].sum()),
    )


def payer_breakdown(data):
    if data.empty:
        return pd.DataFrame(columns=["Payer", "Claims", "Denied",
                                     "Denial rate (%)", "Gross A/R"])
    grouped = data.groupby("Payer", as_index=False).agg(
        Claims=("Claim ID", "count"),
        Denied=("Denial", "sum"),
        **{"Gross A/R": ("Open A/R", "sum")}
    )
    grouped["Denial rate (%)"] = grouped.apply(
        lambda r: percent(r["Denied"], r["Claims"]), axis=1
    )
    return grouped.sort_values("Denial rate (%)", ascending=False)


def pareto(data):
    denied = data[data["Denial"]]
    if denied.empty:
        return pd.DataFrame(columns=["Denial Reason", "Count", "Cumulative (%)"])
    grouped = denied.groupby("Denial Reason", as_index=False).agg(
        Count=("Claim ID", "count")
    ).sort_values(["Count", "Denial Reason"], ascending=[False, True])
    grouped["Cumulative (%)"] = 100.0 * grouped["Count"].cumsum() / len(denied)
    return grouped


def period_compare(data, days=90):
    if data.empty:
        return data.copy(), data.copy()
    end = data["Submitted"].max().normalize()
    split = end - pd.Timedelta(days=days-1)
    start = split - pd.Timedelta(days=days)
    now = data[(data["Submitted"] >= split) & (data["Submitted"] <= end)]
    before = data[(data["Submitted"] >= start) & (data["Submitted"] < split)]
    return now, before


def quality_checks(data):
    rules = [
        ("Duplicate claim IDs", int(data["Claim ID"].duplicated().sum())),
        ("Missing IDs", int(data["Claim ID"].isna().sum() + data["Claim ID"].eq("").sum())),
        ("Nonpositive charges", int(data["Charge"].le(0).sum())),
        ("Negative payments", int(data["Paid"].lt(0).sum())),
        ("Payments above charges", int(data["Paid"].gt(data["Charge"]).sum())),
        ("Negative open amounts", int(data["Open A/R"].lt(0).sum())),
        ("Paid claims showing gross open A/R", int(
            ((data["Status"] == "Paid") & data["Open A/R"].gt(0)).sum())),
        ("Denied claims missing reasons", int(
            (data["Denial"] & data["Denial Reason"].eq("")).sum())),
        ("Non-denied claims with denial reasons", int(
            ((~data["Denial"]) & data["Denial Reason"].ne("")).sum())),
        ("Future submission dates", int(
            data["Submitted"].gt(pd.Timestamp(date.today())).sum())),
    ]
    return pd.DataFrame([{"Rule": title, "Flagged rows": count,
                          "Status": "PASS" if count == 0 else "REVIEW"}
                         for title, count in rules])


def filter_claims(data, payer="All payers", reason="All reasons"):
    filtered = data
    if payer != "All payers":
        filtered = filtered[filtered["Payer"] == payer]
    if reason != "All reasons":
        filtered = filtered[filtered["Denial"] &
                            filtered["Denial Reason"].eq(reason)]
    return filtered


def save_case(notes, claim_id, owner, disposition, comment):
    if owner not in OWNERS or disposition not in STATUSES:
        raise ValueError("Invalid fictional review state")
    changed = dict(notes)
    changed[claim_id] = dict(owner=owner, disposition=disposition,
                             comment=str(comment).strip()[:750])
    return changed


def chart(fig, height=330):
    fig.update_layout(
        template="plotly_white", height=height, paper_bgcolor="white",
        plot_bgcolor="white", margin=dict(l=8, r=8, t=24, b=14),
        font=dict(family="DM Sans, Arial, sans-serif", color=BLACK),
        xaxis=dict(gridcolor="#EEEEEE"),
        yaxis=dict(gridcolor="#EEEEEE"),
    )
    return fig


def selection(event, coordinate):
    try:
        items = event["selection"]["points"]
        return items[0].get(coordinate) if items else None
    except (TypeError, KeyError, IndexError):
        return None


def explore(data):
    st.markdown("### Linked chart and record investigation")
    st.caption("Tap payer bars and cause columns to intersect the underlying claim records.")
    p = payer_breakdown(data)
    c = pareto(data)
    if p.empty:
        st.info("No records match the global filters.")
        return

    left, right = st.columns(2)
    with left:
        fig = px.bar(p, x="Denial rate (%)", y="Payer", orientation="h",
                     color_discrete_sequence=[ORANGE], custom_data=["Claims", "Denied"])
        fig.update_xaxes(ticksuffix="%")
        event = st.plotly_chart(chart(fig), use_container_width=True,
                                on_select="rerun", selection_mode=("points",),
                                key="advanced_payer_chart")
        selected_payer = selection(event, "y")
    with right:
        if c.empty:
            st.info("No denials in this selection.")
            selected_cause = None
        else:
            fig = go.Figure()
            fig.add_bar(x=c["Denial Reason"], y=c["Count"],
                        marker_color=ORANGE, name="Denials")
            fig.add_scatter(x=c["Denial Reason"], y=c["Cumulative (%)"],
                            yaxis="y2", mode="lines+markers", name="Cumulative %",
                            line=dict(color=BLACK))
            fig.update_layout(yaxis2=dict(overlaying="y", side="right",
                                          range=[0, 105], ticksuffix="%"),
                              xaxis_tickangle=-25,
                              legend=dict(orientation="h", y=1.25))
            event = st.plotly_chart(chart(fig), use_container_width=True,
                                    on_select="rerun", selection_mode=("points",),
                                    key="advanced_cause_chart")
            selected_cause = selection(event, "x")
    a, b = st.columns(2)
    with a:
        payer_choice = st.selectbox("Payer drilldown", ["All payers", *sorted(data["Payer"].unique())],
                                    key="advanced_payer_choice")
    with b:
        reason_choice = st.selectbox("Root cause drilldown", ["All reasons", *REASONS],
                                     key="advanced_cause_choice")
    # Selected chart marks override dropdowns, so a touch selection changes rows immediately.
    payer_filter = payer_choice if payer_choice != "All payers" else (selected_payer if selected_payer in set(data["Payer"]) else "All payers")
    cause_filter = reason_choice if reason_choice != "All reasons" else (selected_cause if selected_cause in REASONS else "All reasons")
    drilled = filter_claims(data, payer_filter, cause_filter)
    s = summary(drilled)
    st.caption(f"Active drilldown: {payer_filter} / {cause_filter}")
    a, b, c = st.columns(3)
    a.metric("Claims", f"{s['claims']:,}")
    b.metric("Denial incidence", f"{s['denial_rate']:.1f}%")
    c.metric("Gross open charges", "$" + f"{s['gross_ar']:,.0f}")
    visible = drilled[["Claim ID", "Submitted", "Payer", "Service Line",
                        "Denial Reason", "Status", "Charge", "Open A/R"]].copy()
    visible["Submitted"] = visible["Submitted"].dt.strftime("%Y-%m-%d")
    st.dataframe(visible, hide_index=True, use_container_width=True, height=280)
    st.download_button("Export drilldown CSV",
                       visible.to_csv(index=False).encode("utf-8"),
                       "careflow-drilldown-demo.csv", "text/csv",
                       disabled=visible.empty, key="advanced_drill_export")
    st.markdown("#### Denial concentration heatmap")
    if not data[data["Denial"]].empty:
        matrix = data[data["Denial"]].pivot_table(
            index="Denial Reason", columns="Payer",
            values="Claim ID", aggfunc="count", fill_value=0,
        ).reindex(REASONS, fill_value=0)
        fig = px.imshow(matrix, text_auto=True, aspect="auto",
                        color_continuous_scale=["#FFF8EC", "#FFB866", ORANGE])
        st.plotly_chart(chart(fig), use_container_width=True)


def compare(data):
    st.markdown("### Side-by-side reporting cohorts")
    days = st.select_slider("Window length (days)", options=[30, 60, 90],
                            value=90, key="advanced_period")
    current, previous = period_compare(data, days)
    if current.empty or previous.empty:
        st.warning("Insufficient data for both reporting windows. Expand global filters.")
        return
    curr, prior = summary(current), summary(previous)
    cols = st.columns(4)
    for col, title, key, digits, negative in [
        (cols[0], "Claims", "claims", 0, False),
        (cols[1], "Denial rate", "denial_rate", 1, True),
        (cols[2], "Clean rate", "clean_rate", 1, False),
        (cols[3], "Gross open A/R", "gross_ar", 0, True),
    ]:
        suffix = "%" if key.endswith("rate") else ""
        prefix = "$" if key == "gross_ar" else ""
        col.metric(title, prefix + f"{curr[key]:,.{digits}f}" + suffix,
                   f"{curr[key] - prior[key]:+,.1f}" + (" pp" if suffix else ""),
                   delta_color="inverse" if negative else "normal")
    comparisons = []
    for period, subset in (("Current", current), ("Previous", previous)):
        for _, row in payer_breakdown(subset).iterrows():
            comparisons.append({"Period": period, "Payer": row["Payer"],
                                "Denial rate (%)": row["Denial rate (%)"],
                                "Claim denominator": row["Claims"]})
    table = pd.DataFrame(comparisons)
    fig = px.bar(table, x="Payer", y="Denial rate (%)", color="Period",
                 barmode="group", color_discrete_map={"Current": ORANGE, "Previous": BLACK},
                 hover_data=["Claim denominator"])
    fig.update_yaxes(ticksuffix="%")
    st.plotly_chart(chart(fig), use_container_width=True)
    st.dataframe(table, hide_index=True, use_container_width=True)
    st.caption("Equal-length, disjoint claim submission cohorts; not historical "
               "payer status snapshots or causal evidence. Gross charges are not payments.")


def case_lab(data):
    st.markdown("### Interactive claim investigation")
    st.caption("Review simulated denial cases. Case changes are session-only and do not "
               "change the original claims or publish to an external database.")
    work = data[data["Denial"]].copy()
    if work.empty:
        st.info("No denied claims in current global filters.")
        return
    if "lab_notes" not in st.session_state:
        st.session_state["lab_notes"] = {}
    work["Priority score"] = (
        45 * work["Charge"].clip(upper=10000) / 10000
        + 45 * work["Days Open"].clip(upper=180) / 180
        + 10 * work["Authorization"].eq("Missing").astype(int)
    ).round(1)
    work = work.sort_values("Priority score", ascending=False)
    c1, c2 = st.columns(2)
    with c1:
        reason = st.selectbox("Queue reason", ["All reasons", *REASONS],
                              key="advanced_queue_reason")
    with c2:
        query = st.text_input("Find claim ID", placeholder="DEMO-01234",
                              key="advanced_queue_query").strip()
    if reason != "All reasons":
        work = work[work["Denial Reason"] == reason]
    if query:
        work = work[work["Claim ID"].str.contains(query, case=False, regex=False)]
    if work.empty:
        st.info("No cases match.")
        return
    decisions = st.session_state["lab_notes"]
    work["Owner"] = work["Claim ID"].map(
        lambda cid: decisions.get(cid, {}).get("owner", "Unassigned"))
    work["Review status"] = work["Claim ID"].map(
        lambda cid: decisions.get(cid, {}).get("disposition", "Unreviewed"))
    view = work[["Claim ID", "Payer", "Denial Reason", "Charge", "Days Open",
                 "Priority score", "Owner", "Review status"]]
    event = st.dataframe(view, hide_index=True, use_container_width=True, height=265,
                         selection_mode="single-row", on_select="rerun",
                         key="advanced_queue_table")
    rows = event.selection.rows if hasattr(event, "selection") else []
    default_id = str(view.iloc[rows[0]]["Claim ID"]) if rows else str(view.iloc[0]["Claim ID"])
    ids = list(work["Claim ID"])
    cid = st.selectbox("Open case file", ids, index=ids.index(default_id),
                       key="advanced_case_id")
    case = work.set_index("Claim ID").loc[cid]
    a, b, c = st.columns(3)
    a.metric("Gross charge", "$" + f"{case['Charge']:,.2f}")
    b.metric("Age", f"{case['Days Open']:,} days")
    c.metric("Priority score", f"{case['Priority score']:.1f}/100")
    with st.expander("Claim control evidence", expanded=True):
        st.dataframe(pd.DataFrame([
            {"Control": "Eligibility / documentation complete",
             "Value": "Yes" if bool(case["Intake Complete"]) else "No"},
            {"Control": "Authorization", "Value": case["Authorization"]},
            {"Control": "First-pass clean", "Value": "Yes" if bool(case["First-Pass Clean"]) else "No"},
            {"Control": "Cause", "Value": case["Denial Reason"]},
            {"Control": "Claim status", "Value": case["Status"]},
        ]), hide_index=True, use_container_width=True)
    previous = decisions.get(cid, {})
    with st.form("advanced_case_form_" + cid):
        a, b = st.columns(2)
        with a:
            owner = st.selectbox("Assign synthetic owner", OWNERS,
                                 index=OWNERS.index(previous.get("owner", "Unassigned")))
        with b:
            disposition = st.selectbox("Investigation disposition", STATUSES,
                                       index=STATUSES.index(previous.get("disposition", "Unreviewed")))
        note = st.text_area("Reviewer note (no real patient information)",
                            value=previous.get("comment", ""), max_chars=750)
        if st.form_submit_button("Save case decision in session", type="primary"):
            st.session_state["lab_notes"] = save_case(decisions, cid, owner, disposition, note)
            st.success("Decision recorded in session memory, not permanent storage.")
    saved = st.session_state["lab_notes"]
    st.caption(f"{len(saved):,} local investigation decisions in this session")
    if saved:
        exported = pd.DataFrame([{"Claim ID": k, **v} for k, v in saved.items()])
        st.download_button("Export case decisions CSV",
                           exported.to_csv(index=False).encode("utf-8"),
                           "careflow-investigation-decisions.csv", "text/csv",
                           key="advanced_case_export")
        if st.button("Reset session decisions", key="advanced_case_reset"):
            st.session_state["lab_notes"] = {}
            st.rerun()
    st.caption("Priority score is a fictional triage heuristic for charge, age, "
               "and missing authorization. It is not a recoverability or payer-deadline model.")


def qa(data):
    st.markdown("### Audit and definition explorer")
    quality = quality_checks(data)
    failures = quality.loc[quality["Flagged rows"] > 0]
    a, b, c = st.columns(3)
    a.metric("Rules checked", len(quality))
    b.metric("Passed rules", len(quality) - len(failures))
    c.metric("Flagged rules", len(failures))
    st.dataframe(quality, hide_index=True, use_container_width=True)
    st.download_button("Export QA checks", quality.to_csv(index=False).encode("utf-8"),
                       "careflow-data-audit.csv", "text/csv", key="advanced_qa_export")
    st.markdown("**Definitions:** Denial rate = denied/appealed ÷ filtered claim count. "
                "Clean rate = synthetic eligibility, documentation, authorization, and coding "
                "checks passed ÷ filtered claim count. Gross open A/R = full original "
                "charge for unpaid sample claims, not collectible net A/R.")
    st.warning("This public simulation has no HIPAA controls, secure login, real payers, "
               "persistent records, or patient data. Never enter PHI.")


def render_advanced(data):
    st.markdown("## Decision Intelligence · Advanced Workbench")
    st.caption("Cross-linked selections, cohort comparisons, simulated case review, "
               "and data-audit evidence. All views respect global dashboard filters.")
    mode = st.radio("Investigate", ["Linked exploration", "Cohort comparison",
                                    "Case investigations", "Quality and definitions"],
                    horizontal=True, key="advanced_workbench_mode")
    if mode == "Linked exploration":
        explore(data)
    elif mode == "Cohort comparison":
        compare(data)
    elif mode == "Case investigations":
        case_lab(data)
    else:
        qa(data)
