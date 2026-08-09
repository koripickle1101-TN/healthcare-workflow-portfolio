"""Sidebar header — branding, nav identity, contact strip."""

import streamlit as st


def render_sidebar_header():
    st.sidebar.markdown(
        """
        <div style="padding:1.2rem 0.5rem 1rem 0.5rem;text-align:center;">
            <div style="width:64px;height:64px;border-radius:50%;
                        background:linear-gradient(135deg,#FF8200,#CC6800);
                        margin:0 auto 0.75rem auto;display:flex;
                        align-items:center;justify-content:center;
                        font-size:1.6rem;font-weight:900;color:#111;
                        box-shadow:0 0 0 3px #FF8200,0 0 0 6px rgba(255,130,0,0.18);">
                KP
            </div>
            <div style="font-family:'Playfair Display',serif;
                        font-size:1.05rem;font-weight:700;color:#fff;
                        letter-spacing:0.02em;">
                Kori Pickle
            </div>
            <div style="font-size:0.68rem;color:#FF8200;font-weight:600;
                        letter-spacing:0.12em;text-transform:uppercase;
                        margin-top:0.2rem;">
                Healthcare Operations
            </div>
            <div style="font-size:0.65rem;color:#aaa;margin-top:0.15rem;">
                RCM · Prior Auth · Denial Prevention
            </div>
        </div>
        <hr style="border:none;border-top:1px solid rgba(255,130,0,0.3);margin:0 0 0.75rem 0;"/>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.markdown(
        """
        <div style="padding:0 0.5rem;font-size:0.7rem;color:#999;
                    text-align:center;line-height:1.8;">
            📍 Tennessee &nbsp;|&nbsp; Remote-Ready<br/>
            🔗 <a href="https://github.com/koripickle1101-TN/healthcare-workflow-portfolio"
                  target="_blank" style="color:#FF8200;">GitHub Portfolio</a>
        </div>
        <hr style="border:none;border-top:1px solid rgba(255,255,255,0.08);
                   margin:0.75rem 0 0.5rem 0;"/>
        """,
        unsafe_allow_html=True,
    )
