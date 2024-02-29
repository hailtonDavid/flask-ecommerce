from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
app.config["SECRET_KEY"] = "24195fd5d4baa9393e5e90f0"
db.init_app(app)

from mercado import routes
