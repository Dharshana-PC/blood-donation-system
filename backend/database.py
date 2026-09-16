import sqlite3

def create_tables():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS donors(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        blood TEXT,
        phone TEXT,
        location TEXT,
        pincode TEXT,
        last_donation TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS patients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        blood TEXT,
        phone TEXT,
        location TEXT,
        pincode TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS chosen(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        donor_name TEXT,
        patient_name TEXT,
        blood TEXT,
        phone TEXT
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()