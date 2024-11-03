from flask import Blueprint, request, jsonify
from modelo.ruta import Ruta, db

ruta_blueprint = Blueprint('ruta', __name__)

@ruta_blueprint.route('/guardar_ruta', methods=['POST'])
def guardar_ruta():
    data = request.get_json()
    
    # Validar que se reciban los datos necesarios
    if not data or 'origen' not in data or 'destino' not in data or 'puntos' not in data or 'cupos_disponibles' not in data:
        return jsonify({'message': 'Faltan datos de origen, destino, puntos o cupos disponibles'}), 400

    origen = data['origen']
    destino = data['destino']
    puntos = data['puntos']  # Obtener los puntos
    cupos_disponibles = data['cupos_disponibles']  # Obtener el número de cupos disponibles

    # Crear una nueva ruta con los datos proporcionados
    nueva_ruta = Ruta(origen=origen, destino=destino, puntos=puntos, cupos_disponibles=cupos_disponibles)

    try:
        db.session.add(nueva_ruta)
        db.session.commit()
        return jsonify({'message': 'Ruta guardada exitosamente'}), 201
    except Exception as e:
        db.session.rollback()
        print(f"Error al guardar la ruta: {e}")  # Agregar registro del error
        return jsonify({'message': 'Error al guardar la ruta', 'error': str(e)}), 500
