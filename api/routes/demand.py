from flask import request, jsonify
from api.services.demand import predict

def init_demand_route(app):
    @app.route("/predict/demand", methods=["POST"])
    def predict_demand():
        req = request.get_json()
        data = req.get("data")

        result = predict(data)

        return jsonify({
            "result": result
        })