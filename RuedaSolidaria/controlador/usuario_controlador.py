from flask import Blueprint, render_template, request, redirect, url_for
from ..modelo import usuario
from .. import db

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuarios')
def listar_usuarios():
    usuarios = usuario.query.all()
    return render_template('usuarios/listar.html', usuarios=usuarios)

@usuarios_bp.route('/usuarios/crear', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        email = request.form['email']
        contrasena = request.form['contrasena']
        admin_ID = request.form['admin_ID']
        conductor_ID = request.form['conductor_ID']
        alumno_ID = request.form['alumno_ID']

        usuario = usuario(email=email, contrasena=contrasena, admin_ID=admin_ID, conductor_ID=conductor_ID, alumno_ID=alumno_ID)
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('usuarios.listar_usuarios'))
    return render_template('usuarios/crear.html')

@usuarios_bp.route('/usuarios/editar/<int:user_ID>', methods=['GET', 'POST'])
def editar_usuario(user_ID):
    usuario = usuario.query.get_or_404(user_ID)

    if request.method == 'POST':
        usuario.email = request.form['email']
        usuario.contrasena = request.form['contrasena']
        usuario.admin_ID = request.form['admin_ID']
        usuario.conductor_ID = request.form['conductor_ID']
        usuario.alumno_ID = request.form['alumno_ID']
        db.session.commit()
        return redirect(url_for('usuarios.listar_usuarios'))

    return render_template('usuarios/editar.html', usuario=usuario)

@usuarios_bp.route('/usuarios/eliminar/<int:user_ID>')
def eliminar_usuario(user_ID):
    usuario = usuario.query.get_or_404(user_ID)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('usuarios.listar_usuarios'))