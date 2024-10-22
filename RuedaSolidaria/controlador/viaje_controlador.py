from flask import Blueprint, render_template, request, redirect, url_for, flash
from modelo.viaje import ViajeModel  # Asegúrate de tener este modelo

viajes_bp = Blueprint('viajes', __name__)

@viajes_bp.route('/viaje_crear', methods=['GET', 'POST'])
def crear_viaje():
    if request.method == 'POST':
        viaje_ID = request.form.get('viaje_ID')
        ID_ruta = request.form.get('ID_ruta')
        alumno_ID = request.form.get('alumno_ID')
        fecha = request.form.get('fecha')
        hora = request.form.get('hora')
        calificacion = request.form.get('calificacion')
        comentario = request.form.get('comentario')

        if not viaje_ID or not ID_ruta or not alumno_ID or not fecha or not hora or not calificacion:
            flash('Todos los campos excepto "comentario" son obligatorios.', 'error')
            return redirect(url_for('viajes.crear_viaje'))

        viaje_model = ViajeModel()
        try:
            viaje_model.crear_viaje(viaje_ID, ID_ruta, alumno_ID, fecha, hora, calificacion, comentario)
            flash('Viaje creado exitosamente.', 'success')
            return redirect(url_for('viajes.listar_viajes'))
        except Exception as e:
            flash(f'Error al crear viaje: {e}', 'error')

    return render_template('viaje_crear.html')


@viajes_bp.route('/viaje_listar')
def listar_viajes():
    viaje_model = ViajeModel()
    viajes = viaje_model.listar_viajes()
    return render_template('viaje_listar.html', viajes=viajes)


@viajes_bp.route('/viaje_buscar/<int:viaje_ID>')
def buscar_viaje(viaje_ID):
    viaje_model = ViajeModel()
    viaje = viaje_model.buscar_viaje(viaje_ID)
    if viaje:
        return render_template('viaje_detalle.html', viaje=viaje) 
    else:
        flash('Viaje no encontrado.', 'error')
        return redirect(url_for('viajes.listar_viajes'))


@viajes_bp.route('/viaje_actualizar/<int:viaje_ID>', methods=['GET', 'POST'])
def actualizar_viaje(viaje_ID):
    viaje_model = ViajeModel()
    if request.method == 'POST':
        ID_ruta = request.form.get('ID_ruta')
        alumno_ID = request.form.get('alumno_ID')
        fecha = request.form.get('fecha')
        hora = request.form.get('hora')
        calificacion = request.form.get('calificacion')
        comentario = request.form.get('comentario')

        if not ID_ruta or not alumno_ID or not fecha or not hora or not calificacion:
            flash('Todos los campos excepto "comentario" son obligatorios.', 'error')
            return redirect(url_for('viajes.actualizar_viaje', viaje_ID=viaje_ID))

        try:
            viaje_model.actualizar_viaje(viaje_ID, ID_ruta, alumno_ID, fecha, hora, calificacion, comentario)
            flash('Viaje actualizado exitosamente.', 'success')
            return redirect(url_for('viajes.listar_viajes'))
        except Exception as e:
            flash(f'Error al actualizar viaje: {e}', 'error')

    viaje = viaje_model.buscar_viaje(viaje_ID)
    if viaje:
        return render_template('viaje_actualizar.html', viaje=viaje)
    else:
        flash('Viaje no encontrado.', 'error')
        return redirect(url_for('viajes.listar_viajes'))


@viajes_bp.route('/viaje_eliminar/<int:viaje_ID>', methods=['POST'])
def eliminar_viaje(viaje_ID):
    viaje_model = ViajeModel()
    try:
        viaje_model.eliminar_viaje(viaje_ID)
        flash('Viaje eliminado exitosamente.', 'success')
    except Exception as e:
        flash(f'Error al eliminar viaje: {e}', 'error')
    return redirect(url_for('viajes.listar_viajes'))
