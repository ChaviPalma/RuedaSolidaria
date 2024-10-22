from flask import Blueprint, render_template, request, redirect, url_for, flash
from modelo.establecimiento import EstablecimientoModel  

establecimientos_bp = Blueprint('establecimientos', __name__)

@establecimientos_bp.route('/establecimiento_crear', methods=['GET', 'POST'])
def crear_establecimiento():
    if request.method == 'POST':
        est_ID = request.form.get('est_ID')
        nombre_ins = request.form.get('nombre_ins')
        direccion = request.form.get('direccion')

        if not est_ID or not nombre_ins or not direccion:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('establecimientos.crear_establecimiento'))

        establecimiento_model = EstablecimientoModel()
        try:
            establecimiento_model.crear_establecimiento(est_ID, nombre_ins, direccion)
            flash('Establecimiento creado exitosamente.', 'success')
            return redirect(url_for('establecimientos.listar_establecimientos'))
        except Exception as e:
            flash(f'Error al crear establecimiento: {e}', 'error')

    return render_template('establecimiento_crear.html')


@establecimientos_bp.route('/establecimiento_listar')
def listar_establecimientos():
    establecimiento_model = EstablecimientoModel()
    establecimientos = establecimiento_model.listar_establecimientos()
    return render_template('establecimiento_listar.html', establecimientos=establecimientos)



@establecimientos_bp.route('/establecimiento_buscar/<int:est_ID>')
def buscar_establecimiento(est_ID):
    establecimiento_model = EstablecimientoModel()
    establecimiento = establecimiento_model.buscar_establecimiento(est_ID)
    if establecimiento:
        return render_template('establecimiento_detalle.html', establecimiento=establecimiento) 
    else:
        flash('Establecimiento no encontrado.', 'error')
        return redirect(url_for('establecimientos.listar_establecimientos'))

@establecimientos_bp.route('/establecimiento_actualizar/<int:est_ID>', methods=['GET', 'POST'])
def actualizar_establecimiento(est_ID):
    establecimiento_model = EstablecimientoModel()
    if request.method == 'POST':
        nombre_ins = request.form.get('nombre_ins')
        direccion = request.form.get('direccion')

        if not nombre_ins or not direccion:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('establecimientos.actualizar_establecimiento', est_ID=est_ID))

        try:
            establecimiento_model.actualizar_establecimiento(est_ID, nombre_ins, direccion)
            flash('Establecimiento actualizado exitosamente.', 'success')
            return redirect(url_for('establecimientos.listar_establecimientos'))
        except Exception as e:
            flash(f'Error al actualizar establecimiento: {e}', 'error')


    establecimiento = establecimiento_model.buscar_establecimiento(est_ID)
    if establecimiento:
        return render_template('establecimiento_actualizar.html', establecimiento=establecimiento)
    else:
        flash('Establecimiento no encontrado.', 'error')
        return redirect(url_for('establecimientos.listar_establecimientos'))

@establecimientos_bp.route('/establecimiento_eliminar/<int:est_ID>', methods=['POST'])
def eliminar_establecimiento(est_ID):
    establecimiento_model = EstablecimientoModel()
    try:
        establecimiento_model.eliminar_establecimiento(est_ID)
        flash('Establecimiento eliminado exitosamente.', 'success')
    except Exception as e:
        flash(f'Error al eliminar establecimiento: {e}', 'error')
    return redirect(url_for('establecimientos.listar_establecimientos'))