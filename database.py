import sqlite3
from config import DATABASE_FILE

def create_table():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leaks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT,
        source TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")
    conn.commit()
    conn.close()

def store_leak(data):
    conn = sqlite3.connect("data/leaked_data.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS leaks (id INTEGER PRIMARY KEY, content TEXT)")
    cursor.execute("INSERT INTO leaks (content) VALUES (?)", (data,))
    conn.commit()
    conn.close()

