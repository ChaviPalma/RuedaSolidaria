from flask import Blueprint, request, jsonify, session
from sqlalchemy.exc import IntegrityError, OperationalError
from modelo.ruta import Ruta, db
from modelo.usuario import UsuarioModel  # Import UsuarioModel

ruta_blueprint = Blueprint('ruta', __name__)

@ruta_blueprint.route('/guardar_ruta', methods=['POST'])
def guardar_ruta():
    try:
        data = request.get_json()

        # Validar que se reciban los datos necesarios
        if not data or 'origen' not in data or 'destino' not in data or 'puntos' not in data or 'cupos_disponibles' not in data:
            return jsonify({'message': 'Faltan datos de origen, destino, puntos o cupos disponibles'}), 400

        origen = data['origen']
        destino = data['destino']
        puntos = data['puntos']
        cupos_disponibles = data['cupos_disponibles']

        # Validar el tipo de dato de las variables
        if not isinstance(origen, str) or not isinstance(destino, str) or not isinstance(puntos, list) or not isinstance(cupos_disponibles, int):
            return jsonify({'message': 'Tipo de dato inválido para origen, destino, puntos o cupos disponibles'}), 400

        # Validar que la lista de puntos no esté vacía
        if not puntos:
            return jsonify({'message': 'La lista de puntos no puede estar vacía'}), 400

        # Validar que cupos_disponibles sea un número positivo
        if cupos_disponibles <= 0:
            return jsonify({'message': 'El número de cupos disponibles debe ser un número positivo'}), 400

        # Obtener el ID del conductor de la sesión actual
        usuario_model = UsuarioModel()
        conductor_id = usuario_model.obtener_id_conductor_por_email(session.get('usuario_id'))  

        if not conductor_id:
            return jsonify({'message': 'No se pudo encontrar el ID del conductor'}), 400

        # Crear una nueva ruta con los datos proporcionados
        nueva_ruta = Ruta(origen=origen, destino=destino, puntos=puntos, cupos_disponibles=cupos_disponibles, conductor_id=conductor_id)

        db.session.add(nueva_ruta)
        db.session.commit()
        return jsonify({'message': 'Ruta guardada exitosamente'}), 201

    except IntegrityError as e:
        db.session.rollback()
        print(f"Error de integridad al guardar la ruta: {e}")
        return jsonify({'message': 'Error de integridad al guardar la ruta'}), 400
    except OperationalError as e:
        db.session.rollback()
        print(f"Error de conexión a la base de datos: {e}")
        return jsonify({'message': 'Error de conexión a la base de datos'}), 500
    except Exception as e:
        db.session.rollback()
        print(f"Error al guardar la ruta: {e}")
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
