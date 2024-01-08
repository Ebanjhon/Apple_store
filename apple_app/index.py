from flask import Flask, render_template, url_for, request, redirect
from apple_app import app, login
from flask_login import login_user
import dao
from apple_app.models import *
import hashlib

@app.route('/')
def index():
    kw = request.args.get('kw')
    products = dao.load_products(kw=kw)

    return render_template('index.html', products = products)

@app.route('/<int:value>')
def view_category(value):
    products = dao.load_products(id=value)

    return render_template('index.html', products=products)

@login.user_loader
def user_load(user_id):
    return User.query.get(user_id)


@app.route('/login-admin', methods=["POST","GET"])
def login_admin():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password", "")
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())

        user = User.query.filter(User.username == username.strip(),
                                User.password == password).first()
        if user:
            login_user(user=user)
    return redirect("/admin")



if __name__ == '__main__':
    app.run(debug=True)