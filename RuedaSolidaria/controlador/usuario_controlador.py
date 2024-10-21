from flask import Blueprint, render_template, request, redirect, url_for, flash
from modelo.usuario import UsuarioModel
import mysql.connector
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuario_crear', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        email = request.form.get('email')
        contrasena = request.form.get('contrasena')

        if not email or not contrasena:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('usuarios.crear_usuario')) 

        usuario_model = UsuarioModel()
        usuario_model.crear_usuario(email, contrasena)

        return redirect(url_for('usuarios.crear_usuario'))

    return render_template('usuario_crear.html')

@usuarios_bp.route('/usuario_listar')
def listar_usuarios():
    usuario_model = UsuarioModel()
    usuarios = usuario_model.listar_usuarios()
    return render_template('usuario_listar.html', usuarios=usuarios)