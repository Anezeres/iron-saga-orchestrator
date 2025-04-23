from flask import Flask, request, jsonify

app = Flask(__name__)

core_status = {
    "active": False,
    "current_command": None,
    "power_level": 0
}

@app.route('/activate', methods=['POST'])
def activar_core():
    data = request.json
    
    if not data or 'command' not in data:
        return jsonify({
            "error": "Formato inválido",
            "message": "Debes proporcionar un comando en formato JSON: {'command': 'valor'}"
        }), 400
    
    command = data['command'].lower()
    response = {"command_received": command}

    if command == "start":
        core_status["active"] = True
        core_status["current_command"] = command
        core_status["power_level"] = 100
        response.update({
            "message": "Secuencia de inicio completada",
            "status": "Core en funcionamiento",
            "power_level": 100
        })
    elif command == "shutdown":
        core_status["active"] = False
        core_status["current_command"] = None
        core_status["power_level"] = 0
        response.update({
            "message": "Core apagado con éxito",
            "status": "inactivo",
            "power_level": 0
        })
    else:
        return jsonify({
            "error": "Comando no reconocido",
            "message": f"El comando '{command}' no es válido",
            "available_commands": ["start", "shutdown"]
        }), 400
    
    return jsonify(response), 200

@app.route('/status', methods=['GET'])
def obtener_estado():
    return jsonify({
        "system": "core",
        "status": "active" if core_status["active"] else "inactive",
        "current_command": core_status["current_command"],
        "power_level": core_status["power_level"]
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)