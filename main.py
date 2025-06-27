import streamlit as st
from signup import signup
from login import login
from home import home
from admin_dashboard import admin_dashboard
from user_management import user_management
from resource_management import resource_management

# Set page title and layout
st.set_page_config(page_title="Device Management System", layout="wide")

# Initialize session state
if "username" not in st.session_state:
    st.session_state["username"] = None
    st.session_state["role"] = None

# If user is logged in
if st.session_state["username"]:
    st.sidebar.markdown(f"👋 Logged in as: {st.session_state.username}")

    # Logout Button
    if st.sidebar.button("Logout"):
        st.session_state.clear()
        st.success("You have been logged out.")
        st.experimental_rerun()

    # Admin Role
    if st.session_state["role"] == "admin":
        menu = st.sidebar.selectbox("Admin Menu", ["Dashboard", "User Management", "Resource Management"])
        if menu == "Dashboard":
            admin_dashboard()
        elif menu == "User Management":
            user_management()
        elif menu == "Resource Management":
            resource_management()

    # Normal User Role
    elif st.session_state["role"] == "user":
        menu = st.sidebar.selectbox("User Menu", ["User Management", "Resource Management"])
        if menu == "User Management":
            user_management()
        elif menu == "Resource Management":
            resource_management()

# If user is not logged in
else:
    menu = st.sidebar.selectbox("Menu", ["Home", "Signup", "Login"])
    if menu == "Home":
        home()
    elif menu == "Signup":
        signup()
    elif menu == "Login":
        login()
