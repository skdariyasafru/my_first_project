import sqlite3

def insert_user(username, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?,?)",
                   (username, password))
    conn.commit()
    conn.close()

def view_users():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Example
insert_user("admin", "1234")
print(view_users())
