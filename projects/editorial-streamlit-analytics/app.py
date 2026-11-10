"""Editorial Analytics — a synthetic-data Streamlit portfolio demonstration."""

from datetime import date

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

ORANGE = "#FF8200"
BLACK = "#000000"
WHITE = "#FFFFFF"
GRID = "#EAEAEA"
SEGMENTS = ("Enterprise", "Mid-Market", "SMB", "Professional")
REGIONS = ("North America", "Europe", "Asia-Pacific", "Latin America")


@st.cache_data(show_spinner=False)
def sample_data(as_of: str) -> pd.DataFrame:
    """Reproducible fictional transactions; no real customer data."""
    rng = np.random.default_rng(42)
    rows = []
    for day in pd.date_range(end=pd.Timestamp(as_of), periods=365):
        for _ in range(int(rng.integers(5, 13))):
            clicks = int(rng.integers(30, 150))
            signups = int(rng.integers(0, min(clicks, 16) + 1))
            rows.append({
                "Date": day,
                "Segment": str(rng.choice(SEGMENTS)),
                "Region": str(rng.choice(REGIONS)),
                "Revenue": round(float(rng.gamma(2.5, 110)), 2),
                "Signups": signups,
                "Clicks": clicks,
            })
    return pd.DataFrame(rows)


def calculate_kpis(data: pd.DataFrame) -> dict:
    revenue = float(data["Revenue"].sum())
    signups = int(data["Signups"].sum())
    clicks = int(data["Clicks"].sum())
    return {
        "revenue": revenue,
        "signups": signups,
        "clicks": clicks,
        "conversion": (100.0 * signups / clicks) if clicks else 0.0,
    }


def chart_style(fig):
    fig.update_layout(
        template="plotly_white",
        height=355,
        margin=dict(l=5, r=5, t=12, b=5),
        paper_bgcolor=WHITE,
        plot_bgcolor=WHITE,
        font=dict(family="DM Sans, Arial, sans-serif", color=BLACK),
        showlegend=False,
        xaxis=dict(gridcolor=GRID, linecolor=GRID),
        yaxis=dict(gridcolor=GRID, linecolor=GRID),
    )
    return fig


def main() -> None:
    st.set_page_config(
        page_title="Editorial Analytics | Portfolio Demo",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="auto",
    )
    st.markdown("""
    <style>
      @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&display=swap');
      .stApp, h1, h2, h3, p, button, label, input {
        font-family: 'DM Sans', 'Helvetica Neue', Arial, sans-serif !important;
      }
      .stApp { background: #FFFFFF; color: #000000; }
      [data-testid="stSidebar"] { background: #F7F7F7; border-right: 1px solid #EAEAEA; }
      .block-container { max-width: 1320px; padding-top: 2rem; }
      h1 { font-weight: 800 !important; letter-spacing: -.045em !important; }
      h2, h3 { letter-spacing: -.025em !important; }
      [data-testid="stMetric"] {
        border: 1px solid #EAEAEA; border-top: 3px solid #FF8200;
        border-radius: 12px; padding: 16px 18px; background: #FFFFFF;
      }
      [data-testid="stMetricLabel"] { color: #4B4B4B; font-size: .82rem; }
      [data-testid="stMetricValue"] { color: #000000; letter-spacing: -.04em; }
      .eyebrow { color: #A65300; font-size: .78rem; font-weight: 800;
                 letter-spacing: .16em; text-transform: uppercase; }
      .subtle { color: #555555; font-size: 1.02rem; }
      .stDownloadButton button { background: #FF8200; color: #000000;
                                  border: 1px solid #FF8200; font-weight: 700; }
      @media (max-width: 640px) {
        .block-container { padding-top: 1.2rem; }
        h1 { font-size: 2.1rem !important; }
      }
    </style>
    """, unsafe_allow_html=True)

    data = sample_data(date.today().isoformat())
    first = data["Date"].min().date()
    last = data["Date"].max().date()

    st.sidebar.subheader("Report filters")
    st.sidebar.caption("Adjust the date, segment, and region.")
    chosen_dates = st.sidebar.date_input(
        "Reporting period", value=(first, last), min_value=first, max_value=last
    )
    segment = st.sidebar.selectbox("Customer segment", ["All segments", *SEGMENTS])
    region = st.sidebar.selectbox("Region", ["All regions", *REGIONS])

    filtered = data.copy()
    if isinstance(chosen_dates, (tuple, list)) and len(chosen_dates) == 2:
        start, end = chosen_dates
        filtered = filtered.loc[
            (filtered["Date"].dt.date >= start)
            & (filtered["Date"].dt.date <= end)
        ]
    else:
        st.sidebar.warning("Select an end date to complete the reporting period.")
    if segment != "All segments":
        filtered = filtered.loc[filtered["Segment"] == segment]
    if region != "All regions":
        filtered = filtered.loc[filtered["Region"] == region]

    st.markdown('<p class="eyebrow">Portfolio / Interactive Reporting</p>',
                unsafe_allow_html=True)
    st.title("Executive Performance Dashboard")
    st.markdown(
        '<p class="subtle">Branded analytics with genuine interactive filters '
        'and reproducible sample data.</p>', unsafe_allow_html=True
    )
    st.info(
        "FICTIONAL DEMONSTRATION — All transactions are randomly generated. "
        "No actual revenue, customers, advertising accounts or databases are connected."
    )

    kpis = calculate_kpis(filtered)
    a, b, c, d = st.columns(4)
    a.metric("Sample gross revenue", "$" + f"{kpis['revenue']:,.2f}")
    b.metric("Sample signups", f"{kpis['signups']:,}")
    c.metric("Sample ad clicks", f"{kpis['clicks']:,}")
    d.metric("Signup / click rate", f"{kpis['conversion']:.2f}%")

    st.divider()
    st.subheader("Performance intelligence")
    left, right = st.columns(2)
    if filtered.empty:
        st.info("No fictional records match the current filters.")
    else:
        with left:
            st.caption("Revenue timeline")
            daily = filtered.groupby("Date", as_index=False)["Revenue"].sum()
            fig = px.line(
                daily, x="Date", y="Revenue",
                color_discrete_sequence=[ORANGE],
                labels={"Revenue": "Synthetic revenue ($)", "Date": "Date"}
            )
            fig.update_traces(line=dict(width=3))
            st.plotly_chart(chart_style(fig), use_container_width=True)
        with right:
            st.caption("Revenue by customer segment")
            groups = filtered.groupby("Segment", as_index=False)["Revenue"].sum()
            fig = px.bar(
                groups, x="Segment", y="Revenue",
                color_discrete_sequence=[ORANGE],
                labels={"Revenue": "Synthetic revenue ($)", "Segment": "Segment"}
            )
            st.plotly_chart(chart_style(fig), use_container_width=True)

    st.divider()
    st.subheader("Transaction ledger")
    st.caption("Table search changes the ledger and CSV export, not the headline KPIs.")
    search = st.text_input(
        "Search segment or region", placeholder="Type a segment or region"
    ).strip()
    ledger = filtered.copy()
    if search:
        matches = (
            ledger["Segment"].str.contains(search, case=False, regex=False, na=False)
            | ledger["Region"].str.contains(search, case=False, regex=False, na=False)
        )
        ledger = ledger.loc[matches]
    ledger = ledger.sort_values("Date", ascending=False).copy()
    ledger["Date"] = ledger["Date"].dt.strftime("%Y-%m-%d")
    st.caption(f"{len(ledger):,} matching rows / {len(data):,} total fictional rows")
    if ledger.empty:
        st.info("No sample rows match.")
    else:
        st.dataframe(
            ledger, use_container_width=True, hide_index=True,
            column_config={
                "Revenue": st.column_config.NumberColumn(
                    "Revenue (sample)", format="$%.2f"
                )
            },
        )
    st.download_button(
        "Download filtered sample CSV",
        data=ledger.to_csv(index=False).encode("utf-8"),
        file_name="editorial_analytics_sample.csv",
        mime="text/csv", disabled=ledger.empty
    )
    st.caption(
        "Educational demonstration only. No authentication, persistent "
        "storage, production integration, or private data."
    )


if __name__ == "__main__":
    main()
