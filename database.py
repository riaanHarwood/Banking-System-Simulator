# database.py
import sqlite3

def connect():
    return sqlite3.connect("banking.db")

def initialize():
    conn = connect()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id TEXT PRIMARY KEY,
            name TEXT,
            email TEXT,
            phone TEXT,
            address TEXT,
            id_number TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_customer(customer_id, name, email, phone, address, id_number):
    conn = connect()
    c = conn.cursor()
    c.execute('''
        INSERT INTO customers (customer_id, name, email, phone, address, id_number)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (customer_id, name, email, phone, address, id_number))
    conn.commit()
    conn.close()

def get_customer_by_email(email):
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM customers WHERE email = ?", (email,))
    row = c.fetchone()
    conn.close()
    return row
