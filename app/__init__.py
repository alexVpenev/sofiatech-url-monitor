from flask import Flask
from app.controllers import crud_blueprint
from app.controllers import metrics_blueprint
from app.tasks.background_task import start_background_task

def create_app():
    app = Flask(__name__)

    app.register_blueprint(crud_blueprint, url_prefix="/")
    app.register_blueprint(metrics_blueprint, url_prefix="/metrics")
    # Start background metrics collection
    start_background_task()

    return app
