from flask import Blueprint, render_template, request, redirect, url_for, flash
from modelo.ruta import RutaModel

rutas_bp = Blueprint('rutas', __name__)

@rutas_bp.route('/ruta_crear', methods=['GET', 'POST'])
def crear_ruta():
    if request.method == 'POST':
        origen = request.form.get('origen')
        destino = request.form.get('destino')
        puntos = request.form.get('puntos')
        cupos_disponibles = request.form.get('cupos_disponibles', 0)  # Valor por defecto

        # Validación de campos obligatorios
        if not origen or not destino or not puntos:
            flash('Origen, Destino y Puntos son campos obligatorios.', 'error')
            return redirect(url_for('rutas.crear_ruta'))

        # Crear la instancia del modelo y llamar al método de creación
        ruta_model = RutaModel()
        try:
            ruta_model.crear_ruta(origen, destino, puntos, int(cupos_disponibles))
            flash('Ruta creada exitosamente.', 'success')
            return redirect(url_for('rutas.listar_rutas'))
        except Exception as e:
            flash(f'Error al crear ruta: {e}', 'error')

    return render_template('ruta_crear.html')

@rutas_bp.route('/ruta_listar')
def listar_rutas():
    ruta_model = RutaModel()
    rutas = ruta_model.listar_rutas()
    return render_template('ruta_listar.html', rutas=rutas)

@rutas_bp.route('/ruta_actualizar/<int:id>', methods=['GET', 'POST'])
def actualizar_ruta(id):
    ruta_model = RutaModel()
    if request.method == 'POST':
        origen = request.form.get('origen')
        destino = request.form.get('destino')
        puntos = request.form.get('puntos')
        cupos_disponibles = request.form.get('cupos_disponibles', 0)

        if not origen or not destino or not puntos:
            flash('Origen, Destino y Puntos son campos obligatorios.', 'error')
            return redirect(url_for('rutas.actualizar_ruta', id=id))

        try:
            ruta_model.actualizar_ruta(id, origen, destino, puntos, int(cupos_disponibles))
            flash('Ruta actualizada exitosamente.', 'success')
            return redirect(url_for('rutas.listar_rutas'))
        except Exception as e:
            print(f'Error al actualizar la ruta: {e}')
            flash(f'Error al actualizar la ruta: {e}', 'error')

    return render_template('ruta_actualizar.html', id=id)

@rutas_bp.route('/ruta_eliminar/<int:id>', methods=['POST'])
def eliminar_ruta(id):
    ruta_model = RutaModel()
    try:
        ruta_model.eliminar_ruta(id)
        flash('Ruta eliminada exitosamente.', 'success')
    except Exception as e:
        flash(f'Error al eliminar la ruta: {e}', 'error')
    return redirect(url_for('rutas.listar_rutas'))
