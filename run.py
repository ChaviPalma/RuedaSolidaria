from flask import Flask


db = Flask(__name__)
from RuedaSolidaria import create_app

# Registra el Blueprint

app = create_app()

if __name__ == '__main__':
    db.run(debug=True)