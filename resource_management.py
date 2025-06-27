import streamlit as st
from db import init_db

def resource_management():
    st.title("Resource Management")
    conn = init_db()
    devices = conn.execute("SELECT * FROM devices").fetchall()
    st.table(devices)
