"""Serve the premium self-contained CareFlow web dashboard inside Streamlit.

This keeps the user's existing public Streamlit URL without requiring a new
paid host, database, account, API key, or migration.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


def launch():
    st.set_page_config(
        page_title="CareFlow OS | Revenue Cycle Intelligence",
        page_icon="🟧",
        layout="wide",
        initial_sidebar_state="collapsed",
        menu_items={"About": "Volunteer CareFlow Systems · Synthetic interactive portfolio demonstration."},
    )
    st.markdown(
        """
        <style>
            #MainMenu, footer, [data-testid="stToolbar"], [data-testid="stSidebar"],
            [data-testid="stHeader"] { display:none !important; }
            html, body, .stApp { background:#f7f7f4 !important; margin:0 !important; }
            .block-container {
                max-width:100vw !important;
                padding:0 !important;
                margin:0 !important;
            }
            [data-testid="stMain"] { padding:0 !important; }
            div[data-testid="stElementContainer"] { margin:0 !important; }
            iframe {
                display:block !important;
                border:0 !important;
                width:100% !important;
                border-radius:0 !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    root = Path(__file__).resolve().parent.parent
    html_file = root / "careflow-intelligence-web" / "index.html"
    source = html_file.read_text(encoding="utf-8")
    # Embedded responsive single-page application. Isolated browser iframe;
    # client-side simulation only, never store personal health information.
    components.html(source, height=785, scrolling=True)


if __name__ == "__main__":
    launch()
