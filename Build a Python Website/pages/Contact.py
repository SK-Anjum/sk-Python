import streamlit as st
import re
from components.navbar import navbar
from components.footer import footer

navbar()

st.title("Contact Me")

with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Your Message")
    submit = st.form_submit_button("Send")

    if submit:
        if not name or not email or not message:
            st.error("Please fill out all fields.")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            st.error("Please enter a valid email address.")
        else:
            st.success(f"Thank you {name}, your message was sent successfully!")

footer()
