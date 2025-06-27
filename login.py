import streamlit as st
from db import init_db

def login():
    st.title("Login")
    conn = init_db()

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        result = conn.execute("SELECT role FROM users WHERE username = ? AND password = ?", (username, password)).fetchone()
        if result:
            st.session_state["username"] = username
            st.session_state["role"] = result[0]
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")
