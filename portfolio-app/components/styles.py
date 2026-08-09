import streamlit as st

def inject_global_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Inter:wght@300;400;500;600&family=Great+Vibes&display=swap');

    /* ── BASE ── */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #FFFFFF;
        color: #1a1a1a;
    }
    .stApp { background-color: #FFFFFF; }
    .block-container {
        padding: 2.5rem 3rem 4rem 3rem;
        max-width: 1100px;
    }

    /* ── SIDEBAR ── */
    section[data-testid="stSidebar"] {
        background: #000000 !important;
        border-right: 1px solid #1a1a1a;
    }
    section[data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }
    section[data-testid="stSidebar"] a {
        color: #FF8200 !important;
        font-family: 'Inter', sans-serif;
        font-size: 0.82rem;
        font-weight: 500;
        letter-spacing: 0.04em;
        text-decoration: none;
        padding: 0.45rem 0.75rem;
        display: block;
        border-radius: 4px;
        transition: background 0.2s;
    }
    section[data-testid="stSidebar"] a:hover {
        background: rgba(255,130,0,0.12);
    }
    .stSidebarNav { padding-top: 0.5rem; }

    /* ── HERO BANNER ── */
    .hero-banner {
        background: #000000;
        border-radius: 4px;
        padding: 4rem 3.5rem 3.5rem 3.5rem;
        margin-bottom: 3rem;
        position: relative;
        overflow: hidden;
    }
    .hero-banner::before {
        content: '';
        position: absolute;
        top: -60px; right: -60px;
        width: 220px; height: 220px;
        border-radius: 50%;
        border: 1px solid rgba(255,130,0,0.15);
        box-shadow: 0 0 60px rgba(255,130,0,0.08);
    }
    .hero-banner::after {
        content: '';
        position: absolute;
        top: -30px; right: -30px;
        width: 140px; height: 140px;
        border-radius: 50%;
        border: 1px solid rgba(255,130,0,0.25);
    }
    .hero-eyebrow {
        font-family: 'Inter', sans-serif;
        font-size: 0.7rem;
        font-weight: 600;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: #FF8200;
        margin-bottom: 1.2rem;
    }
    .hero-name {
        font-family: 'Playfair Display', serif;
        font-size: 3.8rem;
        font-weight: 700;
        color: #FFFFFF;
        line-height: 1.1;
        margin-bottom: 1.2rem;
    }
    .hero-name span { color: #FF8200; }
    .hero-subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 0.9rem;
        font-weight: 300;
        color: rgba(255,255,255,0.65);
        line-height: 1.8;
        margin-bottom: 2rem;
        max-width: 520px;
    }
    .hero-tags { display: flex; flex-wrap: wrap; gap: 0.5rem; }
    .hero-tag {
        background: rgba(255,130,0,0.12);
        border: 1px solid rgba(255,130,0,0.3);
        color: #FF8200 !important;
        font-family: 'Inter', sans-serif;
        font-size: 0.68rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        padding: 0.3rem 0.75rem;
        border-radius: 2px;
    }

    /* ── SIGNATURE QUESTION ── */
    .signature-question {
        border-left: 3px solid #FF8200;
        padding: 1.5rem 2rem;
        margin: 2.5rem 0;
        background: #FAFAF9;
    }
    .sq-label {
        display: block;
        font-family: 'Inter', sans-serif;
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: #FF8200;
        margin-bottom: 0.6rem;
    }
    .sq-text {
        font-family: 'Playfair Display', serif;
        font-size: 1.25rem;
        font-style: italic;
        color: #000000;
        line-height: 1.5;
    }

    /* ── PAGE HEADER ── */
    .page-header {
        padding: 3rem 0 2.5rem 0;
        border-bottom: 1px solid #F0EDE8;
        margin-bottom: 2.5rem;
    }
    .page-header-eyebrow {
        font-family: 'Inter', sans-serif;
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: #FF8200;
        margin-bottom: 0.75rem;
    }
    .page-header-title {
        font-family: 'Playfair Display', serif;
        font-size: 2.8rem;
        font-weight: 700;
        color: #000000;
        line-height: 1.15;
        margin-bottom: 0.75rem;
    }
    .page-header-sub {
        font-family: 'Inter', sans-serif;
        font-size: 0.88rem;
        font-weight: 300;
        color: #888888;
        line-height: 1.7;
    }

    /* ── ORANGE CALLOUT ── */
    .orange-callout {
        background: #FFF8F2;
        border-left: 3px solid #FF8200;
        border-radius: 0 4px 4px 0;
        padding: 1.25rem 1.5rem;
        margin: 1.5rem 0;
        font-family: 'Inter', sans-serif;
        font-size: 0.88rem;
        color: #333333;
        line-height: 1.7;
    }
    .orange-callout strong { color: #FF8200; font-weight: 600; }

    /* ── SECTION CARDS ── */
    .section-card {
        background: #FFFFFF;
        border: 1px solid #F0EDE8;
        border-radius: 4px;
        padding: 2rem 1.5rem;
        margin-bottom: 1rem;
        transition: border-color 0.2s, box-shadow 0.2s;
        position: relative;
    }
    .section-card:hover {
        border-color: #FF8200;
        box-shadow: 0 4px 24px rgba(255,130,0,0.08);
    }
    .section-card::before {
        content: '';
        position: absolute;
        top: 1.5rem; right: 1.5rem;
        width: 28px; height: 28px;
        border-radius: 50%;
        border: 1.5px solid rgba(255,130,0,0.2);
        box-shadow: 0 0 12px rgba(255,130,0,0.08);
    }
    .section-card::after {
        content: '';
        position: absolute;
        top: 1.85rem; right: 1.85rem;
        width: 14px; height: 14px;
        border-radius: 50%;
        background: rgba(255,130,0,0.15);
    }
    .sc-icon {
        font-size: 1.6rem;
        margin-bottom: 1rem;
        line-height: 1;
    }
    .sc-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.05rem;
        font-weight: 700;
        color: #000000;
        margin-bottom: 0.4rem;
        line-height: 1.3;
    }
    .sc-tag {
        font-family: 'Inter', sans-serif;
        font-size: 0.6rem;
        font-weight: 700;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: #FF8200;
        margin-bottom: 0.75rem;
    }
    .sc-desc {
        font-family: 'Inter', sans-serif;
        font-size: 0.8rem;
        color: #777777;
        line-height: 1.6;
        font-weight: 300;
    }

    /* ── KPI BOXES ── */
    .kpi-box {
        background: #000000;
        border-radius: 4px;
        padding: 1.75rem 1.25rem;
        text-align: center;
    }
    .kpi-value {
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        font-weight: 700;
        color: #FF8200;
        line-height: 1;
        margin-bottom: 0.5rem;
    }
    .kpi-label {
        font-family: 'Inter', sans-serif;
        font-size: 0.7rem;
        font-weight: 500;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: rgba(255,255,255,0.6);
    }

    /* ── INFO CARDS ── */
    .info-card {
        background: #FAFAF9;
        border: 1px solid #F0EDE8;
        border-left: 3px solid #FF8200;
        border-radius: 0 4px 4px 0;
        padding: 1.25rem 1.5rem;
        margin-bottom: 0.85rem;
    }
    .info-card-title {
        font-family: 'Playfair Display', serif;
        font-size: 0.95rem;
        font-weight: 600;
        color: #000000;
        margin-bottom: 0.4rem;
    }
    .info-card-body {
        font-family: 'Inter', sans-serif;
        font-size: 0.82rem;
        color: #666666;
        line-height: 1.65;
        font-weight: 300;
    }

    /* ── PROCESS STEPS ── */
    .process-step {
        display: flex;
        align-items: flex-start;
        gap: 1.25rem;
        padding: 1.25rem 0;
        border-bottom: 1px dotted #E8E4DF;
    }
    .step-num {
        background: #FF8200;
        color: #FFFFFF;
        font-family: 'Playfair Display', serif;
        font-size: 0.85rem;
        font-weight: 700;
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        box-shadow: 0 0 0 4px rgba(255,130,0,0.15);
    }
    .step-title {
        font-family: 'Playfair Display', serif;
        font-size: 0.95rem;
        font-weight: 600;
        color: #000000;
        margin-bottom: 0.3rem;
    }
    .step-desc {
        font-family: 'Inter', sans-serif;
        font-size: 0.8rem;
        color: #777777;
        line-height: 1.6;
        font-weight: 300;
    }

    /* ── BODY TEXT ── */
    .body-text {
        font-family: 'Inter', sans-serif;
        font-size: 0.9rem;
        color: #444444;
        line-height: 1.8;
        font-weight: 300;
        max-width: 680px;
    }

    /* ── SECTION HEADINGS ── */
    h1, h2, h3 {
        font-family: 'Playfair Display', serif !important;
        color: #000000 !important;
        font-weight: 700 !important;
    }
    h2 { font-size: 1.6rem !important; margin-bottom: 1rem !important; }
    h3 { font-size: 1.2rem !important; margin-bottom: 0.75rem !important; }

    /* ── TABS ── */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0;
        border-bottom: 2px solid #F0EDE8;
    }
    .stTabs [data-baseweb="tab"] {
        font-family: 'Inter', sans-serif !important;
        font-size: 0.78rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        color: #999999 !important;
        padding: 0.75rem 1.5rem !important;
        background: transparent !important;
        border: none !important;
        border-bottom: 2px solid transparent !important;
        margin-bottom: -2px;
    }
    .stTabs [aria-selected="true"] {
        color: #FF8200 !important;
        border-bottom: 2px solid #FF8200 !important;
    }
    .stTabs [data-baseweb="tab-panel"] { padding-top: 1.5rem; }

    /* ── METRIC CARDS ── */
    .metric-card {
        background: #FFFFFF;
        border: 1px solid #F0EDE8;
        border-radius: 4px;
        padding: 1rem 1.25rem;
    }
    .metric-title {
        font-family: 'Playfair Display', serif;
        font-size: 0.9rem;
        font-weight: 700;
        color: #000000;
        margin-bottom: 0.25rem;
    }
    .metric-desc {
        font-family: 'Inter', sans-serif;
        font-size: 0.75rem;
        color: #888888;
        font-weight: 300;
    }

    /* ── DIVIDER ── */
    hr {
        border: none;
        border-top: 1px solid #F0EDE8;
        margin: 2.5rem 0;
    }

    /* ── FOOTER ── */
    .footer {
        text-align: center;
        padding: 3rem 0 2rem 0;
        border-top: 1px solid #F0EDE8;
        margin-top: 3rem;
    }
    .footer-created {
        font-family: 'Inter', sans-serif;
        font-size: 0.7rem;
        font-weight: 600;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: #AAAAAA;
        margin-bottom: 0.5rem;
    }
    .footer-signature {
        font-family: 'Great Vibes', cursive;
        font-size: 2.8rem;
        color: #000000;
        line-height: 1.2;
        margin-bottom: 1.25rem;
        letter-spacing: 0.02em;
    }
    .footer-icons {
        display: flex;
        justify-content: center;
        gap: 1.25rem;
        margin-top: 0.5rem;
    }
    .footer-icon-link {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 36px; height: 36px;
        border-radius: 50%;
        border: 1.5px solid #E0DDD8;
        color: #555555 !important;
        text-decoration: none;
        font-size: 0.85rem;
        font-weight: 600;
        transition: border-color 0.2s, color 0.2s;
    }
    .footer-icon-link:hover {
        border-color: #FF8200;
        color: #FF8200 !important;
    }

    /* ── HIDE STREAMLIT CHROME ── */
    #MainMenu, footer, header { visibility: hidden; }
    .stDeployButton { display: none; }
    </style>
    """, unsafe_allow_html=True)
