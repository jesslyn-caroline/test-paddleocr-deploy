from flask import request, jsonify
from api.services.blur import predict

def init_blur_route(app):
    @app.route("/predict/blur", methods=["POST"])
    def blur():
        data = request.files['file']

        result = predict(data)

        return jsonify({
            "result": result
        })