from flask import Flask, request, jsonify
from sources.engine import ChatEngine

app = Flask(__name__)

# Engine start
try:
    print("--- Loading ChatEngine (Flask) ---")
    bot = ChatEngine()
    print("--- ChatEngine READY ---")
except Exception as e:
    print(f"CRITICAL ERROR: {e}")
    bot = None

@app.route("/chat", methods=["POST"])
def chat_endpoint():
    if bot is None:
        return jsonify({"error": "Engine not initialized", "status": "error"}), 500
    
    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()
    if not message:
        return jsonify({"error": "Message cannot be empty", "status": "error"}), 400
    
    try:
        response = bot.get_response(message)
        return jsonify({
            "reply": str(response),
            "status": "success"
        })
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e), "status": "error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
