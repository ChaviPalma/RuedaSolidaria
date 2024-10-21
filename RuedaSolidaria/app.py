from flask import Flask, render_template, request, redirect, flash
from controlador.usuario_controlador import usuarios_bp;
from controlador.conductor_controlador import conductores_bp
import mysql.connector

app = Flask(__name__)
app.secret_key = 'admin123'
app.register_blueprint(usuarios_bp)
app.register_blueprint(conductores_bp)

@app.route('/')
def home():
    return render_template('index.html')

def get_db_connection():
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'RuedaSolidaria'
    )
    return connection

if __name__ == '__main__':
    app.run(debug=True)