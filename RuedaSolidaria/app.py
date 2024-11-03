from flask import Flask, render_template, redirect
from controlador.usuario_controlador import usuarios_bp
from controlador.conductor_controlador import conductores_bp
from controlador.ruta import ruta_blueprint  # Importa el controlador de rutas
from modelo.ruta import db  # Asegúrate de importar la instancia de db

app = Flask(__name__)
app.secret_key = 'admin123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:loki@localhost:3306/RuedaSolidaria'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Inicializa la base de datos
app.register_blueprint(usuarios_bp)
app.register_blueprint(conductores_bp)
app.register_blueprint(ruta_blueprint)  # Registra el controlador de rutas

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)





