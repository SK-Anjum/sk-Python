import streamlit as st
import hashlib
import os
import json
import time
from cryptography.fernet import Fernet

# Key Management
KEY_PATH = "secret.key"

def get_key():
    if not os.path.exists(KEY_PATH):
        new_key = Fernet.generate_key()
        with open(KEY_PATH, "wb") as file:
            file.write(new_key)
    else:
        with open(KEY_PATH, "rb") as file:
            new_key = file.read()
    return new_key

cipher = Fernet(get_key())

# Data Storage
DATA_PATH = "data.json"

def load_storage():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r") as file:
            return json.load(file)
    return {}

def save_storage(storage):
    with open(DATA_PATH, "w") as file:
        json.dump(storage, file)

# Initialize session state
if "fail_count" not in st.session_state:
    st.session_state.fail_count = 0
if "auth" not in st.session_state:
    st.session_state.auth = True

storage = load_storage()

# helpers
def make_hash(key_input):
    return hashlib.sha256(key_input.encode()).hexdigest()

def encrypt_text(txt):
    return cipher.encrypt(txt.encode()).decode()

def decrypt_text(enc_txt):
    return cipher.decrypt(enc_txt.encode()).decode()

# UI
st.title("🔐 Secure Data Encryption App")

options = ["Home", "Save Data", "Get Data", "Authorize"]
selection = st.sidebar.radio("Navigate", options)

if selection == "Home":
    st.subheader("🏠 Welcome")
    st.write("This app securely **stores and retrieves your data** using encryption and passkeys.")

elif selection == "Save Data":
    st.subheader("📥 Save Data")
    key_label = st.text_input("Label your data:")
    data_input = st.text_area("Enter your data:")
    key_pass = st.text_input("Create a Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if key_label and data_input and key_pass:
            enc_data = encrypt_text(data_input)
            hash_pass = make_hash(key_pass)
            storage[key_label] = {"encrypted_text": enc_data, "passkey": hash_pass}
            save_storage(storage)
            st.success("✅ Data encrypted and saved!")
        else:
            st.error("⚠️ Please fill all fields.")

elif selection == "Get Data":
    st.subheader("🔎 Get Data")

    if not st.session_state.auth:
        st.warning("🔒 Please reauthorize to continue.")
        st.stop()

    key_label = st.text_input("Data Label:")
    key_pass = st.text_input("Passkey:", type="password")

    if st.button("Decrypt"):
        if key_label in storage:
            stored_hash = storage[key_label]["passkey"]
            enc_data = storage[key_label]["encrypted_text"]

            if make_hash(key_pass) == stored_hash:
                result = decrypt_text(enc_data)
                st.success(f"✅ Decrypted Data:\n\n{result}")
                st.session_state.fail_count = 0
            else:
                st.session_state.fail_count += 1
                tries_left = 3 - st.session_state.fail_count
                st.error(f"❌ Incorrect passkey! Attempts left: {tries_left}")
                if st.session_state.fail_count >= 3:
                    st.session_state.auth = False
                    st.warning("🚫 Too many attempts. Please login again.")
        else:
            st.error("⚠️ Label not found!")

elif selection == "Authorize":
    st.subheader("🔐 Reauthorize")
    master_key = st.text_input("Enter Master Key : (e.g: password) ", type="password")

    if st.button("Login"):
        if master_key == "password":
            st.session_state.fail_count = 0
            st.session_state.auth = True
            st.success("✅ Reauthorized successfully.")
        else:
            st.error("❌ Wrong master password.")
