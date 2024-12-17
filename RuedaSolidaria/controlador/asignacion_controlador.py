from flask import render_template, request, flash, redirect, url_for, Blueprint

asignacion_bp = Blueprint('asignacion_bp', __name__)
from modelo.asignacion import Asignacion, db
from modelo.ruta import Ruta
from modelo.conductor import ConductorModel


@asignacion_bp.route('/asignar_viaje', methods=['GET', 'POST'])
def asignar_viaje():
    if request.method == 'POST':
        alumno_id = request.form.get('alumno_id')  # Obtener el ID del alumno
        ruta_id = request.form.get('ruta_id')  # Obtener el ID de la ruta
        conductor_id = request.form.get('conductor_id')  # Obtener el ID del conductor

        # Buscar la ruta y el conductor
        ruta = Ruta.query.filter_by(id=ruta_id).first()
        conductor = ConductorModel.query.filter_by(conductor_ID=conductor_id).first()

        if ruta and conductor and ruta.cupos_disponibles > 0:
            # Descontamos un cupo
            ruta.cupos_disponibles -= 1

            # Crear una nueva asignación
            asignacion = Asignacion(
                alumno_ID=alumno_id, 
                ruta_ID=ruta.id, 
                conductor_ID=conductor.conductor_ID
            )

            # Guardar en la base de datos
            db.session.add(asignacion)
            db.session.commit()

            # Mostrar mensaje de éxito
            flash('Asignación realizada con éxito, cupo descontado y conductor asignado.', 'success')
        else:
            flash('No hay cupos disponibles o conductor no válido.', 'warning')

        return redirect(url_for('asignacion_bp.asignar_viaje'))  # Redirigir a la misma página

    # Si la petición es GET, se cargan las rutas y conductores
    rutas = Ruta.query.all()  # Obtener todas las rutas disponibles
    conductor = ConductorModel.query.all()  # Obtener todos los conductores disponibles
    return render_template('asignar_viaje.html', rutas=rutas, conductores=conductor)
