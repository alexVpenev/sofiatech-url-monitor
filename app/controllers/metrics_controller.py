from flask import Blueprint, Response
from app.services.metrics_service import generate_prometheus_metrics, logging


#Blueprint to expose metrics in Prometheus format
metrics_blueprint = Blueprint('metrics', __name__)


@metrics_blueprint.route('/', methods=['GET'])
def metrics():
    try:
        return Response(generate_prometheus_metrics())
    except Exception as e:
        logging.error(f"Error generating Prometheus metrics: {e}")
        return Response("Error generating metrics", status=500)