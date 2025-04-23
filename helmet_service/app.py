from flask import Flask, request, jsonify

app = Flask(__name__)

helmet_status = {
    "active": False,
    "hud_online": False,
    "ai_assistant": "J.A.R.V.I.S.",
    "vision_mode": "normal",
    "last_command": None
}

@app.route('/activate', methods=['POST'])
def activar_helmet():
    data = request.json
    command = data.get("command", "").lower()

    if command == "deploy":
        helmet_status["active"] = True
        helmet_status["hud_online"] = True
        helmet_status["last_command"] = command
        return jsonify({
            "message": "Casco desplegado y HUD activado",
            "status": "helmet ready",
            "ai_assistant": helmet_status["ai_assistant"],
            "vision_mode": helmet_status["vision_mode"]
        }), 200

    elif command == "shutdown":
        helmet_status["active"] = False
        helmet_status["hud_online"] = False
        helmet_status["last_command"] = command
        return jsonify({
            "message": "Sistema de casco desactivado",
            "status": "helmet offline"
        }), 200

    else:
        return jsonify({
            "error": "Comando no reconocido",
            "available_commands": ["deploy", "shutdown"]
        }), 400

@app.route('/config', methods=['POST'])
def configurar_helmet():
    data = request.json
    if "ai_assistant" in data:
        helmet_status["ai_assistant"] = data["ai_assistant"]
    if "vision_mode" in data:
        helmet_status["vision_mode"] = data["vision_mode"]
    return jsonify({
        "message": "Configuración actualizada",
        "new_config": {
            "ai_assistant": helmet_status["ai_assistant"],
            "vision_mode": helmet_status["vision_mode"]
        }
    }), 200

@app.route('/status', methods=['GET'])
def estado_helmet():
    return jsonify({
        "system": "helmet",
        "status": "active" if helmet_status["active"] else "inactive",
        "hud": "online" if helmet_status["hud_online"] else "offline",
        "ai_assistant": helmet_status["ai_assistant"],
        "vision_mode": helmet_status["vision_mode"],
        "last_command": helmet_status["last_command"]
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
