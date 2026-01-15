from flask import Flask, render_template, request
import psycopg2
import os
'''


app = Flask(__name__)

# Get database URL from Render environment
DATABASE_URL = os.environ.get("DATABASE_URL")

# Create table if not exists
def init_db():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            password VARCHAR(100)
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

init_db()

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                    (name, email, password))
        conn.commit()
        cur.close()
        conn.close()

        return "Registration Successful!"

    return render_template("register.html")

if __name__ == "__main__":
    app.run()



'''
app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)
def init_db():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100),
            password VARCHAR(100)
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

init_db()
@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                       (name, email, password))
        conn.commit()
        conn.close()

        return "Registration Successful!"

    return render_template("register.html")
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
