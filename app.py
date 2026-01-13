from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        p = Product(name=request.form['name'], price=request.form['price'])
        db.session.add(p)
        db.session.commit()
    return render_template("index.html", products=Product.query.all())

@app.route("/admin")
def admin():
    return render_template("admin.html", products=Product.query.all())

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
