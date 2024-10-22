from flask import Flask, render_template
from controlador.usuario_controlador import usuarios_bp;
from controlador.conductor_controlador import conductores_bp
from controlador.establecimiento_controlador import establecimientos_bp
from controlador.ruta_controlador import rutas_bp
from controlador.vehiculo_controlador import vehiculos_bp
from controlador.alumno_controlador import alumnos_bp
from controlador.administrador_controlador import administradores_bp
from controlador.viaje_controlador import viajes_bp

import mysql.connector

app = Flask(__name__)
app.secret_key = 'admin123'
app.register_blueprint(usuarios_bp)
app.register_blueprint(conductores_bp)
app.register_blueprint(establecimientos_bp)
app.register_blueprint(rutas_bp)
app.register_blueprint(vehiculos_bp)
app.register_blueprint(alumnos_bp)
app.register_blueprint(administradores_bp)
app.register_blueprint(viajes_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
from controlador.usuario_controlador import usuarios_bp
app.register_blueprint(usuarios_bp)
