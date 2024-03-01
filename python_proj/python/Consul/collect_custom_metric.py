from prometheus_client import start_http_server, Gauge
import random
import time

# Define custom metric
custom_metric = Gauge('custom_metric', 'Custom metric for DevOps performance analysis')

def collect_custom_metric():
    # Simulate some custom metric values
    value = random.uniform(0, 100)
    custom_metric.set(value)

if __name__ == '__main__':
    # Start Prometheus metrics server
    start_http_server(8000)

    # Collect custom metric every 10 seconds
    while True:
        collect_custom_metric()
        time.sleep(10)
