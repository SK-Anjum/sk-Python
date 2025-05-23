import streamlit as st

def navbar():
    st.markdown("""
        <style>
            .nav {
                background-color: #f0f2f6;
                padding: 10px;
                border-radius: 12px;
                margin-bottom: 25px;
                text-align: center;
            }
            .nav a {
                margin: 0 20px;
                color: #262730;
                text-decoration: none;
                font-weight: 600;
            }
            .nav a:hover {
                color: #1f77b4;
            }
        </style>
        <div class="nav">
            <a href="/"> Home</a>
            <a href="/About "> About</a>
            <a href="/Contact "> Contact</a>
        </div>
    """, unsafe_allow_html=True)
