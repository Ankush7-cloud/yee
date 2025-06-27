import streamlit as st
from db import init_db

def user_management():
    st.title("User Management")
    conn = init_db()
    users = conn.execute("SELECT username, email, role FROM users").fetchall()
    st.table(users)
