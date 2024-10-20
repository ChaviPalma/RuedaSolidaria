from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..modelo.usuario import Usuario
from .. import db
from werkzeug.security import generate_password_hash

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuario_crear', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        email = request.form.get('email')
        contrasena = request.form.get('contrasena')

        if not email or not contrasena:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('usuario.crear_usuario'))

        contrasena_hash = generate_password_hash(contrasena)

        nuevo_usuario = Usuario(email=email, contrasena=contrasena_hash)

        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Usuario creado exitosamente.', 'success')
        return redirect(url_for('usuarios.crear_usuario'))

    return render_template('usuario_crear.html')

@usuarios_bp.route('/usuario')
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuario_listar.html', usuarios=usuarios)

@usuarios_bp.route('/usuario/<int:id>/editar', methods=['GET', 'POST'])
def editar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    if request.method == 'POST':
        usuario.email = request.form.get('email')
        if request.form.get('contrasena'):
            usuario.contrasena = generate_password_hash(request.form.get('contrasena'))
        db.session.commit()
        flash('Usuario actualizado exitosamente.', 'success')
        return redirect(url_for('usuario.listar_usuarios'))
    