import os

class ConfiguracionBd:
    SECRET_KEY = os.urandom(14)  
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/RuedaSolidaria'
    SQLALCHEMY_TRACK_MODIFICATIONS = False