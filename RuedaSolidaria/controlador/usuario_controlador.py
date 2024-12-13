from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from collections import namedtuple
from modelo.usuario import UsuarioModel
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash  
from modelo.tipo_usuario import TipoUsuarioModel

usuarios_bp = Blueprint('usuarios', __name__)

# Ruta para crear un usuario
@usuarios_bp.route('/usuario_crear', methods=['GET', 'POST'])
def crear_usuario():
    tipo_usuario_model = TipoUsuarioModel()

    try:
        # Obtener los tipos de usuario directamente desde el modelo
        tipos_usuario = tipo_usuario_model.listar_tipos_usuario() 
    except Exception as e:
        flash(f'Error al recuperar los tipos de usuario: {e}', 'error')
        return redirect(url_for('usuarios.listar_usuarios'))

    if request.method == 'POST':
        email = request.form.get('email')
        contrasena = request.form.get('contrasena')
        tipo_usuario_id = request.form.get('tipo_usuario')

        if not email or not contrasena or not tipo_usuario_id:
            flash('Los campos email, contraseña y tipo de usuario son obligatorios.', 'error')
            return redirect(url_for('usuarios.crear_usuario'))

        usuario_model = UsuarioModel()
        try:
            # Aquí se hace un hash de la contraseña antes de guardarla
            contrasena_hash = generate_password_hash(contrasena)
            usuario_model.crear_usuario(email, contrasena_hash, tipo_usuario_id)
            flash('Usuario creado exitosamente.', 'success')
            return redirect(url_for('usuarios.listar_usuarios'))
        except Exception as e:
            flash(f'Error al crear usuario: {e}', 'error')

    return render_template('usuario_crear.html', tipos_usuario=tipos_usuario)

# Ruta para eliminar un usuario
@usuarios_bp.route('/usuarios/<email>/eliminar', methods=['POST']) 
def eliminar_usuario(email):
    usuario_model = UsuarioModel()
    try:
        usuario_model.eliminar_usuario(email) 
        flash('Usuario eliminado exitosamente.', 'success')
    except Exception as e:
        flash(f'Error al eliminar usuario: {e}', 'error')
    return redirect(url_for('usuarios.listar_usuarios'))

# Ruta para login
@usuarios_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        contrasena = request.form.get('contrasena')

        usuario_model = UsuarioModel()
        usuario = usuario_model.buscar_usuario(email)

        if usuario:
            # Usar check_password_hash para comparar la contraseña introducida con el hash almacenado
            if check_password_hash(usuario[2], contrasena):  
                session['usuario_id'] = usuario[0]
                dominio = email.split('@')[1]

                # Redirigir dependiendo del dominio
                if dominio in ['estcolegionacional.edu', 'estescuelaprimarialibertad.edu', 'estinstitutotecnologicocentral.edu', 'estescuelasecundarialosalamos.edu']:
                    return redirect(url_for('usuarios.estudiante'))  # Redirige a estudiante.html
                elif dominio in ['concolegionacional.edu', 'conescuelaprimarialibertad.edu', 'coninstitutotecnologicocentral.edu', 'conescuelasecundarialosalamos.edu']:
                    return redirect(url_for('usuarios.conductor'))  # Redirige a conductor.html

                # Asegurarse de que el dominio se maneje correctamente
                if dominio == 'estudiante.com':
                    return redirect(url_for('usuarios.estudiante'))  
                elif dominio == 'conductor.com':
                    return redirect(url_for('usuarios.conductor'))  
                else:
                    flash('Dominio de email no reconocido', 'error')

            else:
                flash('Usuario o contraseña incorrectos', 'error')
        else:
            flash('Usuario o contraseña incorrectos', 'error')

    return render_template('login.html')

# Ruta para la página de estudiante
@usuarios_bp.route('/estudiante')
def estudiante():
    return render_template('estudiante.html')  

# Ruta para la página de conductor
@usuarios_bp.route('/conductor')
def conductor():
    return render_template('conductor.html')  

# Ruta para listar todos los usuarios
@usuarios_bp.route('/usuario_listar')
def listar_usuarios():
    usuario_model = UsuarioModel()
    usuarios = usuario_model.listar_usuarios()  # Llamada al método para obtener los usuarios
    return render_template('usuario_listar.html', usuarios=usuarios)

# Ruta para actualizar la información de un usuario
@usuarios_bp.route('/usuarios/<email>/actualizar', methods=['GET', 'POST'])
def actualizar_usuario(email):
    usuario_model = UsuarioModel()

    if request.method == 'POST':
        contrasena = request.form.get('contrasena')
        tipo_usuario = request.form.get('tipo_usuario')

        if not contrasena or not tipo_usuario:
            flash('La contraseña y el tipo de usuario son obligatorios.', 'error')
            return redirect(url_for('usuarios.actualizar_usuario', email=email))

        try:
            # Hacer el hash de la nueva contraseña
            contrasena_hash = generate_password_hash(contrasena)
            usuario_model.actualizar_usuario(email, contrasena_hash, tipo_usuario)
            flash('Contraseña y tipo de usuario actualizados exitosamente.', 'success')
            return redirect(url_for('usuarios.listar_usuarios'))
        except Exception as e:
            flash(f'Error al actualizar la contraseña: {e}', 'error')
            return redirect(url_for('usuarios.actualizar_usuario', email=email))

    try:
        # Obtener los detalles del usuario y el tipo de usuario con un JOIN
        query = """
            SELECT u.*, tu.descripcion 
            FROM usuarios u
            JOIN tipo_usuario tu ON u.id_tipo_usuario = tu.id_tipo_usuario 
            WHERE u.email = %s
        """
        connection = mysql.connector.connect(user='root', password='', host='localhost', database='RuedaSolidaria')
        cursor = connection.cursor()
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()

        if not result:
            flash(f'Usuario con email {email} no encontrado.', 'error')
            return redirect(url_for('usuarios.listar_usuarios'))

        # Crear una namedtuple para el usuario con la descripción del tipo de usuario
        Usuario = namedtuple('Usuario', ['usuario_ID', 'email', 'admin_ID', 'conductor_ID', 'alumno_ID', 'id_tipo_usuario', 'descripcion'])
        usuario = Usuario(*result)

    except Exception as e:
        flash(f'Error al recuperar los datos del usuario: {e}', 'error')
        return redirect(url_for('usuarios.listar_usuarios'))

    tipos_usuario = usuario_model.listar_tipos_usuario()

    return render_template('usuario_actualizar.html', usuario=usuario, tipos_usuario=tipos_usuario)