from flask import Blueprint, jsonify

crud_blueprint = Blueprint('/', __name__)

@crud_blueprint.route('/', methods=['GET'])
def get_endpoint():
    try:
        return jsonify(message="Other endpoints go here! Hit /metrics for Prometheus data"), 200
    except Exception as e:
        return jsonify(error="Internal Server Error", message=str(e)), 500