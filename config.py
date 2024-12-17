from flask import Flask
import os

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost:3306/RuedaSolidaria'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False