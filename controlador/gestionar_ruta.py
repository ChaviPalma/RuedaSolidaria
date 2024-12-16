from flask import Blueprint, jsonify
from modelo.ruta import Ruta, db

# Define el blueprint para gestionar rutas
gestionar_ruta_blueprint = Blueprint('gestionar_ruta', __name__)

# Ruta para obtener las rutas
@gestionar_ruta_blueprint.route('/gestionar_rutas', methods=['GET'])
def gestionar_rutas():
    try:
        # Obtener todas las rutas desde la base de datos
        rutas = Ruta.query.all()
        rutas_list = [{
             # Asegúrate de que 'id' corresponde al nombre real de tu columna
            'origen': ruta.origen,
            'destino': ruta.destino,
            'cupos_disponibles': ruta.cupos_disponibles
        } for ruta in rutas]
        return jsonify(rutas_list)  # Devuelve las rutas en formato JSON
    except Exception as e:
        return jsonify({'message': 'Error al obtener rutas', 'error': str(e)}), 500
