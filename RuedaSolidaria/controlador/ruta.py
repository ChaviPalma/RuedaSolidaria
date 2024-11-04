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

@ruta_blueprint.route('/buscar_rutas', methods=['POST'])
def buscar_rutas():
    data = request.get_json()
    direccion = data.get('direccion')

    # Validar que se reciba la dirección
    if not direccion:
        return jsonify({'message': 'La dirección es requerida'}), 400

    try:
        # Aquí puedes implementar la lógica para calcular las rutas más cercanas
        # Supongamos que tienes una lógica de filtrado que puedes usar para encontrar las rutas cercanas
        rutas_cercanas = Ruta.query.filter(Ruta.origen.like(f'{direccion}%')).all()  # Filtrar rutas por origen que comience con la dirección ingresada

        # Preparar la respuesta con las rutas encontradas
        rutas_respuesta = [
            {
                'origen': ruta.origen,
                'destino': ruta.destino,
                'cupos_disponibles': ruta.cupos_disponibles
            }
            for ruta in rutas_cercanas
        ]

        return jsonify(rutas_respuesta)

    except Exception as e:
        print(f"Error al buscar rutas: {e}")  # Agregar registro del error
        return jsonify({'message': 'Error al buscar rutas', 'error': str(e)}), 500
