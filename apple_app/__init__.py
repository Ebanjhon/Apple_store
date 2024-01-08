from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = "\xca#\x04t\xb30\xd9\xe2\xa4q2\xcf\x16\xbd"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saleapple?charset=utf8mb4" % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)
admin = Admin(app, name="Quan ly ban hang", template_mode="bootstrap4")

login = LoginManager(app=app)
