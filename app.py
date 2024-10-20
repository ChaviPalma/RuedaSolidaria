from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import ConfiguracionBd
from RuedaSolidaria.controlador.usuario_controlador import usuarios_bp


app = Flask(__name__)
app.config.from_object(ConfiguracionBd)



app.register_blueprint(usuarios_bp)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

