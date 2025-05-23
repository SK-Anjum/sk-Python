import streamlit as st
from components.navbar import navbar
from components.footer import footer

st.set_page_config(page_title="My Website", layout="wide")

navbar()

st.title("Welcome to My Website")

col1, = st.columns(1)

with col1:
    st.header(" Hello There!")
    st.write("""
Welcome to my website! This is a simple Streamlit application that showcases my work and projects. Feel free to explore the different pages using the navigation bar above. If you have any questions or would like to get in touch, please use the contact form on the Contact page.
    """)



st.markdown("### Features")
st.markdown("- Responsive design\n- Easy navigation\n- Contact form\n- About me section\n- Project showcase\n")

footer()
