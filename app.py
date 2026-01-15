from flask import Flask, render_template
import psycopg2
import os

app = Flask(__name__)

# Database connection (Render will provide URL)
'''DATABASE_URL = os.environ.get("DATABASE_URL")

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)'''

@app.route("/")
def home():
   ''' conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    cur.close()
    conn.close()'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
