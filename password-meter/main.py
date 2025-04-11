import streamlit as st
import re
import random

# Common weak passwords
weak_passwords = ['password', '123456', 'qwerty', 'pakistan123', 'admin', 'password123', 'abc123']

# Function for password security
def evaluate_strength(pwd):
    points = 0
    advice = []

    if pwd.lower() in weak_passwords:
        return 0, ["This password is too common. Please use a more unique one."]

    if len(pwd) >= 8:
        points += 1
    else:
        advice.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", pwd) and re.search(r"[a-z]", pwd):
        points += 1
    else:
        advice.append("Include both uppercase and lowercase letters.")

    if re.search(r"\d", pwd):
        points += 1
    else:
        advice.append("Add at least one number.")

    if re.search(r"[!@#$%^&*]", pwd):
        points += 1
    else:
        advice.append("Use special characters like ! @ # $ % ^ & *")

    return points, advice

# Function to generate random pw
def create_password(length=12):
    chars = {
        'upper': "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        'lower': "abcdefghijklmnopqrstuvwxyz",
        'digits': "0123456789",
        'symbols': "!@#$%^&*"
    }
    base = chars['upper'] + chars['lower'] + chars['digits'] + chars['symbols']
    result = [
        random.choice(chars['upper']),
        random.choice(chars['lower']),
        random.choice(chars['digits']),
        random.choice(chars['symbols'])
    ]
    result += random.choices(base, k=length - 4)
    random.shuffle(result)
    return ''.join(result)

# Page config
st.set_page_config(page_title="Password Strength Checker", layout="centered")

# Style
st.markdown("""
    <style>
    .main { background-color: #FAFAFA; }
    .strength-bar {
        height: 10px;
        border-radius: 5px;
        margin-top: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# UI Title
st.title("Password Strength Checker")
st.write("Check how secure your password is, or generate a new one with good strength.")

# Input
user_password = st.text_input("Enter your password here", type="password")
check_now = st.button("Check Strength")

# Strength checking l
if check_now and user_password:
    rating, suggestions = evaluate_strength(user_password)

    labels = {
        0: ("Very Weak", "#e74c3c"),
        1: ("Weak", "#e67e22"),
        2: ("Moderate", "#f1c40f"),
        3: ("Good", "#2ecc71"),
        4: ("Strong", "#27ae60")
    }

    label, color = labels.get(rating, ("Unknown", "#ccc"))

    st.subheader(f"Strength: {label}")
    st.markdown(f"""
        <div class="strength-bar" style="width: 100%; background-color: #eee;">
            <div style="width: {rating * 25}%; background-color: {color};" class="strength-bar"></div>
        </div>
    """, unsafe_allow_html=True)

    if rating < 4:
        st.markdown("### Tips to Improve:")
        for tip in suggestions:
            st.markdown(f"- {tip}")
    else:
        st.success("Great! Your password meets strong criteria.")

elif check_now and not user_password:
    st.warning("Please enter a password before checking.")

st.markdown("---")

# Password Generator
st.subheader("Need a strong password?")

with st.expander("Customize and Generate"):
    pwd_length = st.slider("Select length", 8, 20, 12)

if st.button("Generate Secure Password"):
    new_password = create_password(pwd_length)
    st.code(new_password, language="text")
    st.success("You can use this password or generate another.")
