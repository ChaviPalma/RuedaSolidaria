from flask import Blueprint, jsonify
from modelo.ruta import Ruta  # Asegúrate de que la ruta de importación sea correcta

gestionar_ruta_blueprint = Blueprint('gestionar_rutas', __name__)

@gestionar_ruta_blueprint.route('/gestionar_rutas', methods=['GET'])
def gestionar_rutas():
    try:
        # Obtener las rutas desde la base de datos
        rutas = Ruta.query.all()  # Suponiendo que tienes el modelo Ruta
        rutas_data = []

        for ruta in rutas:
            rutas_data.append({
                'origen': ruta.origen,
                'destino': ruta.destino,
                'cupos_disponibles': ruta.cupos_disponibles,
            })
        
        return jsonify(rutas_data)  # Enviar las rutas como respuesta en formato JSON
    except Exception as e:
        return jsonify({'message': 'Error al cargar las rutas', 'error': str(e)}), 500
