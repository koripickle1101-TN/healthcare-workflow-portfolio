"""
Global CSS injection — Tennessee Orange branding, editorial serif aesthetic.
"""

import streamlit as st


def inject_global_css():
    st.markdown(
        """
        <style>
        /* ── Google Fonts ── */
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=Inter:wght@300;400;500;600;700&display=swap');

        /* ── Root Variables ── */
        :root {
            --tn-orange: #FF8200;
            --tn-orange-light: #FFA040;
            --tn-orange-dark: #CC6800;
            --black: #111111;
            --white: #FFFFFF;
            --gray-50: #FAFAFA;
            --gray-100: #F5F5F5;
            --gray-200: #EEEEEE;
            --gray-400: #AAAAAA;
            --gray-600: #666666;
            --gray-800: #333333;
            --font-serif: 'Playfair Display', Georgia, serif;
            --font-sans: 'Inter', system-ui, sans-serif;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
            --shadow-md: 0 4px 16px rgba(0,0,0,0.10);
            --shadow-lg: 0 8px 32px rgba(0,0,0,0.14);
            --radius: 8px;
            --radius-lg: 14px;
        }

        /* ── Base ── */
        html, body, [class*="css"] {
            font-family: var(--font-sans);
            color: var(--black);
        }

        /* ── Streamlit chrome cleanup ── */
        #MainMenu, footer, header { visibility: hidden; }
        .block-container {
            padding: 1.5rem 2rem 3rem 2rem;
            max-width: 1200px;
        }

        /* ── Headings ── */
        h1, h2, h3 {
            font-family: var(--font-serif);
            color: var(--black);
            letter-spacing: -0.01em;
        }
        h1 { font-size: 2.4rem; font-weight: 900; }
        h2 { font-size: 1.7rem; font-weight: 700; }
        h3 { font-size: 1.2rem; font-weight: 600; border-bottom: 2px solid var(--tn-orange);
             padding-bottom: 0.35rem; display: inline-block; margin-bottom: 1rem; }

        /* ── Sidebar ── */
        [data-testid="stSidebar"] {
            background: var(--black) !important;
            border-right: 3px solid var(--tn-orange);
        }
        [data-testid="stSidebar"] * { color: #DDD !important; }
        [data-testid="stSidebar"] a { color: var(--tn-orange) !important; }
        [data-testid="stSidebar"] hr { border-color: var(--tn-orange) !important; }
        [data-testid="stSidebarNavLink"] {
            border-radius: var(--radius);
            margin: 2px 0;
            transition: background 0.15s;
        }
        [data-testid="stSidebarNavLink"]:hover,
        [data-testid="stSidebarNavLink"][aria-current="page"] {
            background: rgba(255,130,0,0.18) !important;
            color: var(--tn-orange) !important;
        }

        /* ── Hero Banner ── */
        .hero-banner {
            background: linear-gradient(135deg, #111 0%, #1a1a1a 50%, #1f0f00 100%);
            border-left: 6px solid var(--tn-orange);
            border-radius: var(--radius-lg);
            padding: 2.8rem 3rem;
            margin-bottom: 1.5rem;
            position: relative;
            overflow: hidden;
        }
        .hero-banner::after {
            content: '';
            position: absolute;
            top: 0; right: 0;
            width: 35%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,130,0,0.06));
            pointer-events: none;
        }
        .hero-eyebrow {
            font-family: var(--font-sans);
            font-size: 0.7rem;
            font-weight: 700;
            letter-spacing: 0.2em;
            text-transform: uppercase;
            color: var(--tn-orange);
            margin-bottom: 0.8rem;
        }
        .hero-name {
            font-family: var(--font-serif);
            font-size: 3rem;
            font-weight: 900;
            color: var(--white);
            line-height: 1.1;
            margin-bottom: 0.5rem;
        }
        .hero-name span { color: var(--tn-orange); }
        .hero-subtitle {
            font-size: 1.05rem;
            color: #ccc;
            margin-bottom: 1.2rem;
            line-height: 1.6;
            max-width: 600px;
        }
        .hero-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 1rem;
        }
        .hero-tag {
            background: rgba(255,130,0,0.15);
            border: 1px solid rgba(255,130,0,0.4);
            color: var(--tn-orange);
            font-size: 0.7rem;
            font-weight: 600;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            padding: 0.3rem 0.75rem;
            border-radius: 100px;
        }

        /* ── Signature Question ── */
        .signature-question {
            background: var(--tn-orange);
            border-radius: var(--radius-lg);
            padding: 1.4rem 2rem;
            text-align: center;
            margin: 0.5rem 0 1.5rem 0;
        }
        .sq-label {
            font-size: 0.72rem;
            font-weight: 600;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: rgba(0,0,0,0.6);
        }
        .sq-text {
            display: block;
            font-family: var(--font-serif);
            font-size: 1.45rem;
            font-weight: 700;
            color: var(--black);
            margin-top: 0.35rem;
            font-style: italic;
        }

        /* ── Metric Cards ── */
        .metric-card {
            background: var(--white);
            border: 1px solid var(--gray-200);
            border-radius: var(--radius);
            padding: 1.1rem 0.9rem;
            text-align: center;
            box-shadow: var(--shadow-sm);
            transition: box-shadow 0.2s, transform 0.2s;
            height: 100%;
        }
        .metric-card:hover {
            box-shadow: var(--shadow-md);
            transform: translateY(-2px);
        }
        .metric-icon { font-size: 1.6rem; margin-bottom: 0.4rem; }
        .metric-title {
            font-weight: 700; font-size: 0.82rem;
            color: var(--black); margin-bottom: 0.25rem;
        }
        .metric-desc { font-size: 0.7rem; color: var(--gray-600); line-height: 1.45; }

        /* ── Section Cards ── */
        .section-card {
            background: var(--white);
            border-radius: var(--radius-lg);
            padding: 1.4rem;
            box-shadow: var(--shadow-sm);
            border: 1px solid var(--gray-200);
            height: 100%;
            transition: box-shadow 0.2s, transform 0.2s;
            margin-bottom: 0.5rem;
        }
        .section-card:hover {
            box-shadow: var(--shadow-md);
            transform: translateY(-3px);
        }
        .sc-icon { font-size: 1.8rem; margin-bottom: 0.5rem; }
        .sc-title {
            font-family: var(--font-serif);
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--black);
            margin-bottom: 0.2rem;
        }
        .sc-tag {
            font-size: 0.65rem;
            font-weight: 600;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            color: var(--tn-orange);
            margin-bottom: 0.55rem;
        }
        .sc-desc { font-size: 0.77rem; color: var(--gray-600); line-height: 1.55; }

        /* ── Remote Cards ── */
        .remote-card {
            background: var(--gray-50);
            border: 1px solid var(--gray-200);
            border-radius: var(--radius);
            padding: 1.1rem;
            text-align: center;
            height: 100%;
        }

        /* ── Page Header ── */
        .page-header {
            background: linear-gradient(135deg, #111 0%, #1a1a1a 100%);
            border-left: 5px solid var(--tn-orange);
            border-radius: var(--radius-lg);
            padding: 2rem 2.5rem;
            margin-bottom: 1.5rem;
            color: var(--white);
        }
        .page-header-eyebrow {
            font-size: 0.68rem;
            font-weight: 700;
            letter-spacing: 0.18em;
            text-transform: uppercase;
            color: var(--tn-orange);
            margin-bottom: 0.5rem;
        }
        .page-header-title {
            font-family: var(--font-serif);
            font-size: 2rem;
            font-weight: 900;
            color: var(--white);
            margin-bottom: 0.4rem;
        }
        .page-header-sub {
            font-size: 0.88rem;
            color: #ccc;
            line-height: 1.55;
        }

        /* ── Info Cards ── */
        .info-card {
            background: var(--white);
            border-radius: var(--radius);
            padding: 1.3rem 1.4rem;
            box-shadow: var(--shadow-sm);
            border: 1px solid var(--gray-200);
            margin-bottom: 0.75rem;
        }
        .info-card-title {
            font-weight: 700;
            font-size: 0.88rem;
            color: var(--black);
            margin-bottom: 0.3rem;
        }
        .info-card-body {
            font-size: 0.78rem;
            color: var(--gray-600);
            line-height: 1.6;
        }

        /* ── Orange Callout ── */
        .orange-callout {
            background: rgba(255,130,0,0.08);
            border-left: 4px solid var(--tn-orange);
            border-radius: 0 var(--radius) var(--radius) 0;
            padding: 1rem 1.2rem;
            margin: 1rem 0;
        }
        .orange-callout strong { color: var(--tn-orange); }

        /* ── KPI Grid ── */
        .kpi-box {
            background: var(--black);
            border-radius: var(--radius);
            padding: 1.2rem;
            text-align: center;
        }
        .kpi-value {
            font-family: var(--font-serif);
            font-size: 2rem;
            font-weight: 900;
            color: var(--tn-orange);
        }
        .kpi-label {
            font-size: 0.72rem;
            color: #ccc;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            margin-top: 0.2rem;
        }

        /* ── Process Step ── */
        .process-step {
            display: flex;
            gap: 1rem;
            align-items: flex-start;
            margin-bottom: 1rem;
        }
        .step-num {
            background: var(--tn-orange);
            color: var(--black);
            font-weight: 900;
            font-size: 0.85rem;
            width: 28px; height: 28px;
            border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            flex-shrink: 0;
        }
        .step-body { flex: 1; }
        .step-title { font-weight: 700; font-size: 0.85rem; color: var(--black); }
        .step-desc { font-size: 0.76rem; color: var(--gray-600); line-height: 1.5; margin-top: 0.15rem; }

        /* ── Tag Chips ── */
        .chip {
            display: inline-block;
            background: var(--gray-100);
            border: 1px solid var(--gray-200);
            border-radius: 100px;
            font-size: 0.68rem;
            font-weight: 600;
            color: var(--gray-800);
            padding: 0.2rem 0.6rem;
            margin: 0.15rem;
        }
        .chip-orange {
            background: rgba(255,130,0,0.12);
            border-color: rgba(255,130,0,0.4);
            color: var(--tn-orange-dark);
        }

        /* ── Body text helper ── */
        .body-text {
            font-size: 0.86rem;
            line-height: 1.75;
            color: var(--gray-800);
        }

        /* ── Footer ── */
        .footer {
            border-top: 1px solid var(--gray-200);
            padding-top: 1.2rem;
            text-align: center;
            font-size: 0.76rem;
            color: var(--gray-600);
            line-height: 2;
        }

        /* ── Streamlit widget overrides ── */
        div[data-testid="stMetric"] {
            background: var(--white);
            border: 1px solid var(--gray-200);
            border-radius: var(--radius);
            padding: 0.8rem 1rem;
            box-shadow: var(--shadow-sm);
        }
        div[data-testid="stMetric"] label {
            font-size: 0.7rem !important;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--gray-600) !important;
        }
        div[data-testid="stMetricValue"] {
            font-family: var(--font-serif);
            color: var(--tn-orange) !important;
            font-weight: 700 !important;
        }

        /* ── Tab styling ── */
        .stTabs [data-baseweb="tab-list"] {
            gap: 0.25rem;
            border-bottom: 2px solid var(--gray-200);
        }
        .stTabs [data-baseweb="tab"] {
            font-size: 0.8rem;
            font-weight: 600;
            padding: 0.6rem 1.2rem;
            color: var(--gray-600);
        }
        .stTabs [aria-selected="true"] {
            color: var(--tn-orange) !important;
            border-bottom-color: var(--tn-orange) !important;
        }

        /* ── Expander ── */
        details summary {
            font-weight: 600;
            font-size: 0.85rem;
            color: var(--black);
        }
        details[open] summary { color: var(--tn-orange); }

        /* ── Button ── */
        .stButton > button {
            background: var(--tn-orange) !important;
            color: var(--black) !important;
            border: none !important;
            font-weight: 700 !important;
            border-radius: var(--radius) !important;
            letter-spacing: 0.04em;
        }
        .stButton > button:hover {
            background: var(--tn-orange-dark) !important;
            color: var(--white) !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
