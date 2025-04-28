import threading
import time
from app.services.metrics_service import collect_metrics

def start_background_task():
    def run():
        while True:
            collect_metrics()
            time.sleep(10)

    background_thread = threading.Thread(target=run, daemon=True)
    background_thread.start()
