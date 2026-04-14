import sqlite3

def extract_data():
    return [1, 2, 3, 4]

def transform_data(data):
    return [x * 2 for x in data]

def load_data(data):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS numbers (value INTEGER)")
    cursor.execute("DELETE FROM numbers")

    for val in data:
        cursor.execute("INSERT INTO numbers (value) VALUES (?)", (val,))

    conn.commit()
    conn.close()