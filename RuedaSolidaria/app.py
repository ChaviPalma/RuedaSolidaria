from flask import Flask, render_template
from controlador.usuario_controlador import usuarios_bp

app = Flask(__name__)
app.secret_key = 'admin123'
app.register_blueprint(usuarios_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
from controlador.usuario_controlador import usuarios_bp
app.register_blueprint(usuarios_bp)
