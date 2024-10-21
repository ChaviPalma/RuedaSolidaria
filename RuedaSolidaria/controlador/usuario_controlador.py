from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from modelo.usuario import UsuarioModel

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuario_crear', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        email = request.form.get('email')
        contrasena = request.form.get('contrasena')

        usuario_model = UsuarioModel()
        usuario_model.crear_usuario(email, contrasena)

        if not email or not contrasena:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('usuarios.crear_usuario')) 

        return redirect(url_for('usuarios.crear_usuario'))

    return render_template('usuario_crear.html')

@usuarios_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        contrasena = request.form.get('contrasena')

        usuario_model = UsuarioModel()
        usuario = usuario_model.buscar_usuario(email)

        if usuario and usuario[2] == contrasena:  # Asegúrate de que el índice 2 sea la contraseña
            session['usuario_id'] = usuario[0]  # Guardar ID de usuario en la sesión
            
            # Extraer el dominio del email
            dominio = email.split('@')[1]
            
            # Redirigir dependiendo del dominio
            if dominio == 'estudiante.com':
                return redirect(url_for('usuarios.estudiante'))  # Redirige a estudiante.html
            elif dominio == 'conductor.com':
                return redirect(url_for('usuarios.conductor'))  # Redirige a conductor.html
            else:
                flash('Dominio de email no reconocido', 'error')

        else:
            flash('Usuario o contraseña incorrectos', 'error')

    return render_template('login.html')

@usuarios_bp.route('/estudiante')
def estudiante():
    return render_template('estudiante.html')  # Asegúrate de tener este archivo en templates

@usuarios_bp.route('/conductor')
def conductor():
    return render_template('conductor.html')  # Asegúrate de tener este archivo en templates
