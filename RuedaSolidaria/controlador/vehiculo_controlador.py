from flask import Blueprint, render_template, request, redirect, url_for, flash
from modelo.vehiculo import VehiculoModel

vehiculos_bp = Blueprint('vehiculos', __name__)

@vehiculos_bp.route('/vehiculo_crear', methods=['GET', 'POST'])
def crear_vehiculo():
    if request.method == 'POST':
        vehi_ID = request.form.get('vehi_ID')
        nombre_vehi = request.form.get('nombre_vehi')
        color = request.form.get('color')
        patente = request.form.get('patente')
        conductor_ID = request.form.get('conductor_ID')

        if not vehi_ID or not nombre_vehi or not color or not patente or not conductor_ID:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('vehiculos.crear_vehiculo'))

        vehiculo_model = VehiculoModel()
        try:
            vehiculo_model.crear_vehiculo(vehi_ID, nombre_vehi, color, patente, conductor_ID)
            flash('Vehículo creado exitosamente.', 'success')
            return redirect(url_for('vehiculos.listar_vehiculos'))
        except Exception as e:
            flash(f'Error al crear vehículo: {e}', 'error')

    return render_template('vehiculo_crear.html')


@vehiculos_bp.route('/vehiculo_listar')
def listar_vehiculos():
    vehiculo_model = VehiculoModel()
    vehiculos = vehiculo_model.listar_vehiculos()
    return render_template('vehiculo_listar.html', vehiculos=vehiculos)


@vehiculos_bp.route('/vehiculo_buscar/<int:vehi_ID>')
def buscar_vehiculo(vehi_ID):
    vehiculo_model = VehiculoModel()
    vehiculo = vehiculo_model.buscar_vehiculo(vehi_ID)
    if vehiculo:
        return render_template('vehiculo_detalle.html', vehiculo=vehiculo) 
    else:
        flash('Vehículo no encontrado.', 'error')
        return redirect(url_for('vehiculos.listar_vehiculos'))


@vehiculos_bp.route('/vehiculo_actualizar/<int:vehi_ID>', methods=['GET', 'POST'])
def actualizar_vehiculo(vehi_ID):
    vehiculo_model = VehiculoModel()
    if request.method == 'POST':
        nombre_vehi = request.form.get('nombre_vehi')
        color = request.form.get('color')
        patente = request.form.get('patente')
        conductor_ID = request.form.get('conductor_ID')

        if not nombre_vehi or not color or not patente or not conductor_ID:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('vehiculos.actualizar_vehiculo', vehi_ID=vehi_ID))

        try:
            vehiculo_model.actualizar_vehiculo(vehi_ID, nombre_vehi, color, patente, conductor_ID)
            flash('Vehículo actualizado exitosamente.', 'success')
            return redirect(url_for('vehiculos.listar_vehiculos'))
        except Exception as e:
            flash(f'Error al actualizar el vehículo: {e}', 'error')

    vehiculo = vehiculo_model.buscar_vehiculo(vehi_ID)
    if vehiculo:
        return render_template('vehiculo_actualizar.html', vehiculo=vehiculo)
    else:
        flash('Vehículo no encontrado.', 'error')
        return redirect(url_for('vehiculos.listar_vehiculos'))


@vehiculos_bp.route('/vehiculo_eliminar/<int:vehi_ID>', methods=['POST'])
def eliminar_vehiculo(vehi_ID):
    vehiculo_model = VehiculoModel()
    try:
        vehiculo_model.eliminar_vehiculo(vehi_ID)
        flash('Vehículo eliminado exitosamente.', 'success')
    except Exception as e:
        flash(f'Error al eliminar el vehículo: {e}', 'error')
    return redirect(url_for('vehiculos.listar_vehiculos'))
