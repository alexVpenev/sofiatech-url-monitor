import requests
import logging
from prometheus_client import Gauge, CollectorRegistry, generate_latest

URLS_TO_MONITOR = [
    "https://httpstat.us/503",
    "https://httpstat.us/200"
]
# Configure basic logging format and level
# For Prod, should be configurable via an env variable
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

# Create Prometheus registry and define metrics for monitoring URLs
registry = CollectorRegistry()
url_status = Gauge('external_url_up', 'URL status:', ['url'], registry=registry)
url_response_ms = Gauge('external_url_response_ms', 'URL response time in ms:', ['url'], registry=registry)

def collect_metrics():
    for url in URLS_TO_MONITOR:
        try:
            logging.info(f"Checking URL: {url}")
            response = requests.get(url, timeout=10)
            status = 1 if response.status_code == 200 else 0
            response_time = response.elapsed.total_seconds() * 1000
        except requests.RequestException as e:
            logging.error(f"Error while fetching {url}: {e}")
            status = 0
            response_time = 0

        url_status.labels(url=url).set(status)
        url_response_ms.labels(url=url).set(response_time)

def generate_prometheus_metrics():
    return generate_latest(registry)