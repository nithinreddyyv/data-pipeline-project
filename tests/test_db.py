import sqlite3

def test_data_loaded():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM numbers")
    count = cursor.fetchone()[0]

    conn.close()

    assert count > 0