from flask import request, jsonify
from api.services.bundling import get_bundling

def init_bundling_route(app):
    @app.route("/bundling", methods=["POST"])
    def product_bundling():
        req = request.get_json()
        data = req.get("data")

        result = get_bundling(data)

        return jsonify({
            "result": result
        })