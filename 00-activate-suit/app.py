from flask import Flask, request, jsonify
import requests
import sys

sys.stdout.reconfigure(line_buffering=True)
app = Flask(__name__)

# Endpoints internos (nombres de servicios de Kubernetes)
CORE_URL = "http://core-service:5001"
ARMOR_URL = "http://armor-service:5002"
AI_URL = "http://ai-service:5003"
DIAGNOSTIC_URL = "http://diagnostic-service:5004"

@app.route('/activate-suit', methods=['POST'])
def activate_suit():
    user = request.json.get('user')
    successful_steps = []

    try:
        print(f"🦾 Activando traje para {user}", flush=True)

        # 1. Core
        print("🔋 Iniciando núcleo...", flush=True)
        res = requests.post(f"{CORE_URL}/activate", json={"user": user})
        print(f"🔌 Respuesta núcleo: {res.status_code} - {res.text}", flush=True)
        if res.status_code != 200:
            raise Exception("Falló núcleo")
        successful_steps.append("core")

        # 2. Armor
        print("🛡️ Ensamblando armadura...", flush=True)
        res = requests.post(f"{ARMOR_URL}/assemble", json={"user": user})
        print(f"⚙️ Respuesta armadura: {res.status_code} - {res.text}", flush=True)
        if res.status_code != 200:
            raise Exception("Falló armadura")
        successful_steps.append("armor")

        # 3. Diagnóstico
        print("🧠 Ejecutando diagnóstico...", flush=True)
        res = requests.post(f"{DIAGNOSTIC_URL}/run-checks", json={"user": user})
        print(f"📈 Respuesta diagnóstico: {res.status_code} - {res.text}", flush=True)
        if res.status_code != 200:
            raise Exception("Falló diagnóstico")
        successful_steps.append("diagnostic")

        # 4. AI
        print("🤖 Boot de IA (Jarvis/Friday)...", flush=True)
        res = requests.post(f"{AI_URL}/boot", json={"user": user})
        print(f"🧠 Respuesta IA: {res.status_code} - {res.text}", flush=True)
        if res.status_code != 200:
            raise Exception("Falló AI")
        successful_steps.append("ai")

        print(f"✅ Traje ACTIVADO para {user}", flush=True)
        return jsonify({"message": f"Traje activado para {user}"}), 200

    except Exception as e:
        print(f"🔥 ERROR detectado: {e}", flush=True)
        if "ai" in successful_steps:
            print("⏪ Apagando IA...", flush=True)
            requests.post(f"{AI_URL}/shutdown", json={"user": user})
        if "diagnostic" in successful_steps:
            print("⏪ Revirtiendo diagnóstico...", flush=True)
            requests.post(f"{DIAGNOSTIC_URL}/cancel", json={"user": user})
        if "armor" in successful_steps:
            print("⏪ Desensamblando armadura...", flush=True)
            requests.post(f"{ARMOR_URL}/cancel", json={"user": user})
        if "core" in successful_steps:
            print("⏪ Apagando núcleo...", flush=True)
            requests.post(f"{CORE_URL}/shutdown", json={"user": user})

        return jsonify({"message": f"Error al activar el traje de {user}. Se ejecutaron compensaciones."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
