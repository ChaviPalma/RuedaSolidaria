from flask import Blueprint, render_template, request, redirect, url_for, flash
from modelo.conductor import ConductorModel
from modelo.tipo_usuario import TipoUsuarioModel  # Para cargar los tipos de usuario disponibles

conductores_bp = Blueprint('conductores', __name__)

@conductores_bp.route('/conductor_crear', methods=['GET', 'POST'])
def crear_conductor():
    tipo_usuario_model = TipoUsuarioModel()
    tipos_usuario = tipo_usuario_model.listar_tipo_usuarios()  

    if request.method == 'POST':
        conductor_id = request.form.get('conductor_id')
        pnombre_cond = request.form.get('pnombre_cond')
        snombre_cond = request.form.get('snombre_cond')
        appaterno_cond = request.form.get('appaterno_cond')
        apmaterno_cond = request.form.get('apmaterno_cond')
        inst_id = request.form.get('inst_id')
        id_tipo_usuario = request.form.get('id_tipo_usuario')  # Obtener el tipo de usuario seleccionado

        if not conductor_id or not pnombre_cond or not snombre_cond or not inst_id or not id_tipo_usuario:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('conductores.crear_conductor'))

        conductor_model = ConductorModel()
        conductor_model.crear_conductor(conductor_id, pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_id, id_tipo_usuario)

        flash('Conductor creado exitosamente.', 'success')
        return redirect(url_for('conductores.listar_conductores'))

    return render_template('conductor_crear.html', tipos_usuario=tipos_usuario)

@conductores_bp.route('/conductor_listar')
def listar_conductores():
    conductor_model = ConductorModel()
    conductores = conductor_model.listar_conductores()  
    return render_template('conductor_listar.html', conductores=conductores)

@conductores_bp.route('/conductores/<int:conductor_ID>/eliminar', methods=['POST'])
def eliminar_conductor(conductor_ID):
    conductor_model = ConductorModel()
    try:
        conductor_model.eliminar_conductor(conductor_ID)
        flash('Conductor eliminado exitosamente.', 'success')
    except Exception as e:
        flash(f'Error al eliminar conductor: {e}', 'error')
    return redirect(url_for('conductores.listar_conductores'))

@conductores_bp.route('/conductores/<int:conductor_ID>/actualizar', methods=['GET', 'POST'])
def actualizar_conductor(conductor_ID):
    conductor_model = ConductorModel()
    tipo_usuario_model = TipoUsuarioModel()
    tipos_usuario = tipo_usuario_model.listar_tipo_usuarios()  # Cargar los tipos de usuario disponibles

    if request.method == 'POST':
        pnombre_cond = request.form.get('pnombre_cond')
        snombre_cond = request.form.get('snombre_cond')
        appaterno_cond = request.form.get('appaterno_cond')
        apmaterno_cond = request.form.get('apmaterno_cond')
        inst_ID = request.form.get('inst_id')
        id_tipo_usuario = request.form.get('id_tipo_usuario')  # Obtener el tipo de usuario seleccionado

        if not pnombre_cond or not snombre_cond or not inst_ID or not id_tipo_usuario:
            flash('Los campos Primer Nombre, Segundo Nombre, Establecimiento e ID Tipo Usuario son obligatorios.', 'error')
            return redirect(url_for('conductores.actualizar_conductor', conductor_ID=conductor_ID))

        try:
            conductor_model.actualizar_conductor(conductor_ID, pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_ID, id_tipo_usuario)
            flash('Conductor actualizado exitosamente.', 'success')
            return redirect(url_for('conductores.listar_conductores'))
        except Exception as e:
            flash(f'Error al actualizar conductor: {e}', 'error')
            return redirect(url_for('conductores.actualizar_conductor', conductor_ID=conductor_ID))

    conductor = conductor_model.buscar_conductor(conductor_ID)
    return render_template('conductor_actualizar.html', conductor=conductor, tipos_usuario=tipos_usuario)
