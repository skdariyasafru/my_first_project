from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return print(" hrllo rendring is worikun:")
if __name__ == "__main__":
    app.run()
