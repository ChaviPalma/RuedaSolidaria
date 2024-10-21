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