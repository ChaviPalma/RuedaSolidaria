from flask import Flask, jsonify
from modelo.tipo_usuario import TipoUsuarioModel  

app = Flask(__name__)


tipo_usuario_model = TipoUsuarioModel()

@app.route('/tipo_usuario', methods=['GET'])
def listar_tipo_usuarios():
    try:
        tipo_usuarios = tipo_usuario_model.listar_tipo_usuarios()
        if tipo_usuarios:
            # Si hay tipo de usuarios, devolverlos en formato JSON
            return jsonify([t._asdict() for t in tipo_usuarios]), 200
        else:
            # Si no se encuentran tipo de usuarios, devolver un mensaje adecuado
            return jsonify({"mensaje": "No se encontraron tipos de usuarios."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/tipo_usuario/<int:id_tipo_usuario>', methods=['DELETE'])
def eliminar_tipo_usuario(id_tipo_usuario):
    try:
        filas_afectadas = tipo_usuario_model.eliminar_tipo_usuario(id_tipo_usuario)
        if filas_afectadas > 0:
            return jsonify({"mensaje": "Tipo de usuario eliminado exitosamente."}), 200
        else:
            return jsonify({"mensaje": "No se encontró el tipo de usuario para eliminar."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
