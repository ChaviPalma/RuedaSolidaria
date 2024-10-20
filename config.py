import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class ConfiguracionBd:
    SECRET_KEY = os.urandom(24)  
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/RuedaSolidaria'
    SQLALCHEMY_TRACK_MODIFICATIONS = False