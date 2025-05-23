import streamlit as st
from components.navbar import navbar
from components.footer import footer

navbar()

st.title(" About Me")
st.write("""
## Hi! I'm Anjum, a Python developer.
I am a Python developer with a passion for creating efficient and scalable applications. I have experience in web development, data analysis, and machine learning. I enjoy solving complex problems and continuously learning new technologies.
""")

footer()
