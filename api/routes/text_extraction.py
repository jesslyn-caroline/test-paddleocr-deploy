from flask import request, jsonify
from api.services.text_extraction import predict

def init_text_extraction_route(app):
    @app.route("/predict/text-extraction", methods=["POST"])
    def text_extraction():
        data = request.files['file']

        result = predict(data)

        return jsonify({
            "result": result
        })