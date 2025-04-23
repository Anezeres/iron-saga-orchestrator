from flask import Flask, request, jsonify

app = Flask(__name__)

armor_status = {
    "status": "not_assembled",
    "parts_attached": [],
    "mobility": "0%",
    "structural_integrity": "none"
}

@app.route('/assemble', methods=['POST'])
def assemble_armor():
    if not request.is_json:
        return jsonify({
            "error": "Solicitud inválida",
            "message": "Se espera contenido JSON en la solicitud"
        }), 400

    armor_status.update({
        "status": "armor_ready",
        "parts_attached": ["torso", "left_arm", "right_arm", "legs", "boots"],
        "mobility": "100%",
        "structural_integrity": "optimal"
    })
    return jsonify({
        "message": "Armadura ensamblada con éxito",
        "armor_status": armor_status
    }), 200

@app.route('/disassemble', methods=['POST'])
def disassemble_armor():
    if not request.is_json:
        return jsonify({
            "error": "Solicitud inválida",
            "message": "Se espera contenido JSON en la solicitud"
        }), 400

    armor_status.update({
        "status": "not_assembled",
        "parts_attached": [],
        "mobility": "0%",
        "structural_integrity": "none"
    })
    return jsonify({
        "message": "Armadura desmontada con éxito",
        "armor_status": armor_status
    }), 200

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({
        "message": "Estado actual de la armadura",
        "armor_status": armor_status
    }), 200

# Ruta para cuando alguien use un método incorrecto
@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({
        "error": "Método no permitido",
        "message": "Verifica que estás usando el método HTTP correcto para esta ruta"
    }), 405

# Ruta para cuando se accede a una ruta no existente
@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "error": "Ruta no encontrada",
        "message": "La ruta solicitada no existe en el microservicio armor_service"
    }), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)
