from flask import Blueprint, render_template, request, redirect, url_for, flash
from modelo.administrador import AdministradorModel  

administradores_bp = Blueprint('administradores', __name__)

@administradores_bp.route('/administrador_crear', methods=['GET', 'POST'])
def crear_administrador():
    if request.method == 'POST':
        # Obtener los datos del formulario
        pnombre_admin = request.form.get('pnombre_admin')
        snombre_admin = request.form.get('snombre_admin')
        apaterno_admin = request.form.get('apaterno_admin')
        amaterno_admin = request.form.get('amaterno_admin')
        email = request.form.get('email')
        contrasena = request.form.get('contrasena')
        telefono = request.form.get('telefono')
        id_tipo_usuario = request.form.get('id_tipo_usuario')  # id_tipo_usuario debe ser enviado en el formulario

        # Validar que todos los campos obligatorios estén completos
        if not pnombre_admin or not email or not contrasena or not id_tipo_usuario:
            flash('Los campos nombre, correo y tipo de usuario son obligatorios.', 'error')
            return redirect(url_for('administradores.crear_administrador'))

        administrador_model = AdministradorModel()
        try:
            # Llamada al modelo para crear el administrador sin admin_ID
            administrador_model.crear_administrador(pnombre_admin, snombre_admin, apaterno_admin, amaterno_admin, email, contrasena, telefono, id_tipo_usuario)
            flash('Administrador creado exitosamente.', 'success')
            return redirect(url_for('administradores.listar_administradores'))
        except Exception as e:
            flash(f'Error al crear administrador: {e}', 'error')

    return render_template('administrador_crear.html')


@administradores_bp.route('/administrador_listar')
def listar_administradores():
    administrador_model = AdministradorModel()
    administradores = administrador_model.listar_administradores()
    return render_template('administrador_listar.html', administradores=administradores)


@administradores_bp.route('/administrador_buscar/<int:admin_ID>')
def buscar_administrador(admin_ID):
    administrador_model = AdministradorModel()
    administrador = administrador_model.buscar_administrador(admin_ID)
    if administrador:
        return render_template('administrador_detalle.html', administrador=administrador)
    else:
        flash('Administrador no encontrado.', 'error')
        return redirect(url_for('administradores.listar_administradores'))


@administradores_bp.route('/administrador_actualizar/<int:admin_ID>', methods=['GET', 'POST'])
def actualizar_administrador(admin_ID):
    administrador_model = AdministradorModel()

    # Obtener la información del administrador para el formulario
    administrador = administrador_model.buscar_administrador(admin_ID)
    if not administrador:
        flash('Administrador no encontrado.', 'error')
        return redirect(url_for('administradores.listar_administradores'))

    if request.method == 'POST':
        # Obtener los datos del formulario
        pnombre_admin = request.form.get('pnombre_admin')
        snombre_admin = request.form.get('snombre_admin')
        apaterno_admin = request.form.get('apaterno_admin')
        amaterno_admin = request.form.get('amaterno_admin')
        email = request.form.get('email')
        contrasena = request.form.get('contrasena')
        telefono = request.form.get('telefono')
        id_tipo_usuario = request.form.get('id_tipo_usuario')  # id_tipo_usuario debe ser enviado en el formulario

        # Validar que todos los campos obligatorios estén completos
        if not pnombre_admin or not email or not id_tipo_usuario:
            flash('Los campos nombre, correo y tipo de usuario son obligatorios.', 'error')
            return redirect(url_for('administradores.actualizar_administrador', admin_ID=admin_ID))

        try:
            # Llamada al modelo para actualizar el administrador
            administrador_model.actualizar_administrador(admin_ID, pnombre_admin, snombre_admin, apaterno_admin, amaterno_admin, email, contrasena, telefono, id_tipo_usuario)
            flash('Administrador actualizado exitosamente.', 'success')
            return redirect(url_for('administradores.listar_administradores'))
        except Exception as e:
            flash(f'Error al actualizar administrador: {e}', 'error')

    return render_template('administrador_actualizar.html', administrador=administrador)


@administradores_bp.route('/administrador_eliminar/<int:admin_ID>', methods=['POST'])
def eliminar_administrador(admin_ID):
    administrador_model = AdministradorModel()
    try:
        # Llamada al modelo para eliminar el administrador
        administrador_model.eliminar_administrador(admin_ID)
        flash('Administrador eliminado exitosamente.', 'success')
    except Exception as e:
        flash(f'Error al eliminar administrador: {e}', 'error')
    return redirect(url_for('administradores.listar_administradores'))
