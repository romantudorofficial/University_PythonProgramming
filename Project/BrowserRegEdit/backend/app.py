from flask import Flask, request, jsonify, render_template
from registry_handler import create_key, delete_key, get_registry

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # Serve the HTML page for the frontend

# API: Create a registry key
@app.route("/api/create_key", methods=["POST"])
def create_registry_key():
    path = request.json.get("path")
    if create_key(path):
        return jsonify({"message": "Key created successfully!"}), 200
    return jsonify({"error": "Failed to create key"}), 400

# API: Delete a registry key
@app.route("/api/delete_key", methods=["DELETE"])
def delete_registry_key():
    path = request.json.get("path")
    if delete_key(path):
        return jsonify({"message": "Key deleted successfully!"}), 200
    return jsonify({"error": "Key not found"}), 404

# API: Get the current state of the registry
@app.route("/api/get_registry", methods=["GET"])
def fetch_registry():
    return jsonify(get_registry()), 200

if __name__ == "__main__":
    app.run(debug=True)
