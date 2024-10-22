from flask import Blueprint, render_template, request, redirect, url_for, flash
from modelo.ruta import RutaModel  

rutas_bp = Blueprint('rutas', __name__)

@rutas_bp.route('/ruta_crear', methods=['GET', 'POST'])
def crear_ruta():
    if request.method == 'POST':
        ID_ruta = request.form.get('ID_ruta')
        Origen = request.form.get('Origen')
        Destino = request.form.get('Destino')
        est_ID = request.form.get('est_ID')
        conductor_ID = request.form.get('conductor_ID')

     
        if not ID_ruta or not Origen or not Destino or not est_ID or not conductor_ID:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('rutas.crear_ruta'))

        ruta_model = RutaModel()
        try:
            ruta_model.crear_ruta(ID_ruta, Origen, Destino, est_ID, conductor_ID)
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


@rutas_bp.route('/ruta_buscar/<int:ID_ruta>')
def buscar_ruta(ID_ruta):
    ruta_model = RutaModel()
    ruta = ruta_model.buscar_ruta(ID_ruta)
    if ruta:
        return render_template('ruta_detalle.html', ruta=ruta) 
    else:
        flash('Ruta no encontrada.', 'error')
        return redirect(url_for('rutas.listar_rutas'))

@rutas_bp.route('/ruta_actualizar/<int:ID_ruta>', methods=['GET', 'POST'])
def actualizar_ruta(ID_ruta):
    ruta_model = RutaModel()
    if request.method == 'POST':
        Origen = request.form.get('Origen')
        Destino = request.form.get('Destino')
        est_ID = request.form.get('est_ID')
        conductor_ID = request.form.get('conductor_ID')

        if not Origen or not Destino or not est_ID or not conductor_ID:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('rutas.actualizar_ruta', ID_ruta=ID_ruta))

        try:
            ruta_model.actualizar_ruta(ID_ruta, Origen, Destino, est_ID, conductor_ID)
            flash('Ruta actualizada exitosamente.', 'success')
            return redirect(url_for('rutas.listar_rutas'))
        except Exception as e:
            flash(f'Error al actualizar la ruta: {e}', 'error')

    ruta = ruta_model.buscar_ruta(ID_ruta)
    if ruta:
        return render_template('ruta_actualizar.html', ruta=ruta)
    else:
        flash('Ruta no encontrada.', 'error')
        return redirect(url_for('rutas.listar_rutas'))

@rutas_bp.route('/ruta_eliminar/<int:ID_ruta>', methods=['POST'])
def eliminar_ruta(ID_ruta):
    ruta_model = RutaModel()
    try:
        ruta_model.eliminar_ruta(ID_ruta)
        flash('Ruta eliminada exitosamente.', 'success')
    except Exception as e:
        flash(f'Error al eliminar la ruta: {e}', 'error')
    return redirect(url_for('rutas.listar_rutas'))