import duckdb

def init_db():
    conn = duckdb.connect("app_data.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            email TEXT,
            password TEXT,
            role TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS devices (
            service_tag TEXT PRIMARY KEY,
            employee_id TEXT,
            device_type TEXT,
            memory TEXT
        )
    """)
    return conn
