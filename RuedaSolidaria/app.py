# app.py

from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'RuedaSolidaria'

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM Alumnos") 
    alumnos = cursor.fetchall()  
    cursor.close()  #
    return render_template('index.html', alumnos=alumnos)
if __name__ == '__main__':
    app.run(debug=True)