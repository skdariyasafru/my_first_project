from flask import Flask, render_template
import psycopg2
import os


app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")

def get_db_connection():
    return psycopg2.connect(DATABASE_URL)


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
