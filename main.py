import streamlit as st
from signup import signup
from login import login
from home import home
from admin_dashboard import admin_dashboard
from user_management import user_management
from resource_management import resource_management

st.set_page_config(page_title="Device Manager", layout="wide")

# Initialize session
if "username" not in st.session_state:
    st.session_state.username = None
    st.session_state.role = None

menu = st.sidebar.selectbox("Menu", ["Home", "Signup", "Login"])

if st.session_state.username:
    if st.session_state.role == "admin":
        menu = st.sidebar.selectbox("Admin Menu", ["Dashboard", "User Management", "Resource Management"])
        if menu == "Dashboard":
            admin_dashboard()
        elif menu == "User Management":
            user_management()
        elif menu == "Resource Management":
            resource_management()
    elif st.session_state.role == "user":
        menu = st.sidebar.selectbox("User Menu", ["User Management", "Resource Management"])
        if menu == "User Management":
            user_management()
        elif menu == "Resource Management":
            resource_management()
else:
    if menu == "Home":
        home()
    elif menu == "Signup":
        signup()
    elif menu == "Login":
        login()
