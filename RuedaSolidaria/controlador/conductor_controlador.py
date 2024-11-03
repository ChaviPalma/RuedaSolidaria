from flask import Blueprint, render_template, request, redirect, url_for, flash
from modelo.conductor import ConductorModel

conductores_bp = Blueprint('conductores', __name__)

@conductores_bp.route('/conductor_crear', methods=['GET', 'POST'])
def crear_conductor():
    if request.method == 'POST':
        conductor_id = request.form.get('conductor_id')
        pnombre_cond = request.form.get('pnombre_cond')
        snombre_cond = request.form.get('snombre_cond')
        appaterno_cond = request.form.get('appaterno_cond')
        apmaterno_cond = request.form.get('apmaterno_cond')
        inst_id = request.form.get('inst_id')

        if not conductor_id or not pnombre_cond or not snombre_cond or not inst_id:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('conductores.crear_conductor')) 

        conductor_model = ConductorModel()
        conductor_model.crear_conductor(conductor_id, pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_id)

        flash('Conductor creado exitosamente.', 'success')
        return redirect(url_for('conductores.listar_conductores'))

    return render_template('conductor_crear.html')

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

    if request.method == 'POST':
        pnombre_cond = request.form.get('pnombre_cond')
        snombre_cond = request.form.get('snombre_cond')
        appaterno_cond = request.form.get('appaterno_cond')
        apmaterno_cond = request.form.get('apmaterno_cond')
        inst_ID = request.form.get('inst_id')

        if not pnombre_cond or not snombre_cond or not inst_ID:
            flash('Los campos Primer Nombre, Segundo Nombre e ID del Establecimiento son obligatorios.', 'error')
            return redirect(url_for('conductores.actualizar_conductor', conductor_ID=conductor_ID))

        try:
            conductor_model.actualizar_conductor(conductor_ID, pnombre_cond, snombre_cond, appaterno_cond, apmaterno_cond, inst_ID)
            flash('Conductor actualizado exitosamente.', 'success')
            return redirect(url_for('conductores.listar_conductores'))
        except Exception as e:
            flash(f'Error al actualizar conductor: {e}', 'error')
            return redirect(url_for('conductores.actualizar_conductor', conductor_ID=conductor_ID))


    conductor = conductor_model.buscar_conductor(conductor_ID)
    return render_template('conductor_actualizar.html', conductor=conductor)