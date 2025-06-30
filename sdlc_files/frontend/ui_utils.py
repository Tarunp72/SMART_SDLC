import streamlit as st

def set_custom_style():
    st.markdown("""
        <style>
        /* LIGHT THEME (Blue sidebar) */
        :root {
            --sidebar-light: #cde8fc;
            --sidebar-dark: #0f172a;
        }
        
        /* DEFAULT (Light theme) */
        [data-testid="stSidebar"],
        .stSidebar .sidebar-content {
            background-color: var(--sidebar-light) !important;
        }
        
        /* DARK THEME OVERRIDE */
        @media (prefers-color-scheme: dark) {
            [data-testid="stSidebar"],
            .stSidebar .sidebar-content {
                background-color: var(--sidebar-dark) !important;
            }
            
            /* Keep white text in dark mode */
            .stSidebar * {
                color: #e2e8f0 !important;
            }
        }
        
        /* UNIVERSAL SIDEBAR TEXT */
        .stSidebar * {
            color: white !important;
        }
        </style>
    """, unsafe_allow_html=True)

def show_header():
    st.markdown(
        "<h1 style='color:#2563eb; font-weight:700;'>🚀 SmartSDLC: AI-Powered SDLC Automation</h1>",
        unsafe_allow_html=True
    )
    st.caption("Powered by IBM Granite 3.3_2b Instruct, FastAPI & Streamlit")