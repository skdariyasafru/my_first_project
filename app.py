from flask import Flask, render_template, request, redirect, session
import psycopg2
import os

app = Flask(__name__)
app.secret_key = "secret123"

DATABASE_URL = os.environ.get("DATABASE_URL")

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/register_user", methods=["POST"])
def register_user():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username TEXT,
                email TEXT,
                password TEXT
            )
        """)

    
    conn.commit()
    cur.close()
    conn.close()
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name,email,password) VALUES (%s,%s,%s)",
                (name, email, password))
    conn.commit()
    cur.close()
    conn.close()

    return redirect("/")

@app.route("/login_user", methods=["POST"])
def login_user():
    email = request.form["email"]
    password = request.form["password"]

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email=%s AND password=%s",
                (email, password))
    user = cur.fetchone()
    cur.close()
    conn.close()

    if user:
        session["user"] = user[1]
        return redirect("/dashboard")
    else:
        return "Login Failed!"

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", user=session["user"])
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
