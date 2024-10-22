from flask import Blueprint, render_template, request, redirect, url_for, flash
from modelo.alumno import AlumnoModel  

alumnos_bp = Blueprint('alumnos', __name__)

@alumnos_bp.route('/alumno_crear', methods=['GET', 'POST'])
def crear_alumno():
    if request.method == 'POST':
        alumno_ID = request.form.get('alumno_ID')
        pnombre_alum = request.form.get('pnombre_alum')
        snombre_alum = request.form.get('snombre_alum')
        apaterno_alum = request.form.get('apaterno_alum')
        amaterno_alum = request.form.get('amaterno_alum')
        inst_ID = request.form.get('inst_ID')

        if not alumno_ID or not pnombre_alum or not snombre_alum or not inst_ID:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('alumnos.crear_alumno'))

        alumno_model = AlumnoModel()
        try:
            alumno_model.crear_alumno(alumno_ID, pnombre_alum, snombre_alum, apaterno_alum, amaterno_alum, inst_ID)
            flash('Alumno creado exitosamente.', 'success')
            return redirect(url_for('alumnos.listar_alumnos'))
        except Exception as e:
            flash(f'Error al crear alumno: {e}', 'error')

    return render_template('alumno_crear.html')

@alumnos_bp.route('/alumno_listar')
def listar_alumnos():
    alumno_model = AlumnoModel()
    alumnos = alumno_model.listar_alumnos()
    return render_template('alumno_listar.html', alumnos=alumnos)

@alumnos_bp.route('/alumno_buscar/<int:alumno_ID>')
def buscar_alumno(alumno_ID):
    alumno_model = AlumnoModel()
    alumno = alumno_model.buscar_alumno(alumno_ID)
    if alumno:
        return render_template('alumno_detalle.html', alumno=alumno) 
    else:
        flash('Alumno no encontrado.', 'error')
        return redirect(url_for('alumnos.listar_alumnos'))

@alumnos_bp.route('/alumno_actualizar/<int:alumno_ID>', methods=['GET', 'POST'])
def actualizar_alumno(alumno_ID):
    alumno_model = AlumnoModel()
    if request.method == 'POST':
        pnombre_alum = request.form.get('pnombre_alum')
        snombre_alum = request.form.get('snombre_alum')
        apaterno_alum = request.form.get('apaterno_alum')
        amaterno_alum = request.form.get('amaterno_alum')
        inst_ID = request.form.get('inst_ID')

        if not pnombre_alum or not snombre_alum or not inst_ID:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('alumnos.actualizar_alumno', alumno_ID=alumno_ID))

        try:
            alumno_model.actualizar_alumno(alumno_ID, pnombre_alum, snombre_alum, apaterno_alum, amaterno_alum, inst_ID)
            flash('Alumno actualizado exitosamente.', 'success')
            return redirect(url_for('alumnos.listar_alumnos'))
        except Exception as e:
            flash(f'Error al actualizar alumno: {e}', 'error')

    alumno = alumno_model.buscar_alumno(alumno_ID)
    if alumno:
        return render_template('alumno_actualizar.html', alumno=alumno)
    else:
        flash('Alumno no encontrado.', 'error')
        return redirect(url_for('alumnos.listar_alumnos'))

@alumnos_bp.route('/alumno_eliminar/<int:alumno_ID>', methods=['POST'])
def eliminar_alumno(alumno_ID):
    alumno_model = AlumnoModel()
    try:
        alumno_model.eliminar_alumno(alumno_ID)
        flash('Alumno eliminado exitosamente.', 'success')
    except Exception as e:
        flash(f'Error al eliminar alumno: {e}', 'error')
    return redirect(url_for('alumnos.listar_alumnos'))
