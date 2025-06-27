import streamlit as st
from db import init_db

def admin_dashboard():
    st.title("Admin Dashboard")
    conn = init_db()

    st.subheader("Insert New Device")
    tag = st.text_input("Service Tag")
    eid = st.text_input("Employee ID")
    dtype = st.selectbox("Device Type", ["GPU", "Desktop"])
    mem = st.text_input("Memory")

    if st.button("Insert"):
        try:
            conn.execute("INSERT INTO devices VALUES (?, ?, ?, ?)", (tag, eid, dtype, mem))
            st.success("Device added")
        except:
            st.error("Service Tag must be unique")

    st.subheader("All Devices")
    devices = conn.execute("SELECT * FROM devices").fetchall()
    st.table(devices)

    st.subheader("Delete Device")
    del_tag = st.text_input("Enter Service Tag to delete")
    if st.button("Delete"):
        conn.execute("DELETE FROM devices WHERE service_tag = ?", (del_tag,))
        st.success("Deleted")

    st.subheader("Update Memory")
    upd_tag = st.text_input("Service Tag to Update")
    new_mem = st.text_input("New Memory")
    if st.button("Update"):
        conn.execute("UPDATE devices SET memory = ? WHERE service_tag = ?", (new_mem, upd_tag))
        st.success("Updated")
