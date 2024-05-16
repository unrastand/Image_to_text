import sqlite3 as sql

def get_connection():
    return sql.connect('license.db')

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS license
                 (license text primary key)''')
    conn.commit()
    conn.close()

def insert_license(license):
    create_table()
    conn = get_connection()
    cur = conn.cursor()
    license = license.upper()
    cur.execute("INSERT INTO license VALUES (?)", (license,))
    conn.commit()
    conn.close()

def read_license():
    create_table()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM license")
    license = cur.fetchall()
    conn.close()
    return license

def delete_license(license):
    create_table()
    conn = get_connection()
    cur = conn.cursor()
    license = license.upper()
    cur.execute("DELETE FROM license WHERE license = ?", (license,))
    conn.commit()
    conn.close()