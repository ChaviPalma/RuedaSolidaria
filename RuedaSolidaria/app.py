from flask import Flask, render_template
from controlador.usuario_controlador import usuarios_bp
from controlador.conductor_controlador import conductores_bp
from controlador.ruta import ruta_blueprint  # Importa el controlador de rutas
from controlador.gestionar_ruta import gestionar_ruta_blueprint  # Importa el controlador de gestionar rutas
from modelo.ruta import db  # Importa la instancia de db

app = Flask(__name__)
app.secret_key = 'admin123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:loki@localhost:3306/RuedaSolidaria'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Inicializa la base de datos
app.register_blueprint(usuarios_bp)
app.register_blueprint(conductores_bp)
app.register_blueprint(ruta_blueprint)  # Registra el controlador de rutas
app.register_blueprint(gestionar_ruta_blueprint)  # Registra el blueprint para gestionar rutas

@app.route('/')
def home():
    return render_template('index.html')

# Ruta para la página "Gestionar Rutas"
@app.route('/gestionar_rutas')  # Asegúrate de que esta ruta coincide con la del blueprint
def gestionar_rutas_view():
    return render_template('gestionar_ruta.html')



if __name__ == '__main__':
    app.run(debug=True)
