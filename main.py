# coding=utf-8
import time
import logging
from prometheus_client import start_http_server, Summary
from settings import EXPORTER_PORT, RPC_ADDRESS, RUN_INTERVAL
from exporter import update_metrics
from parity import Parity

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    p = Parity(RPC_ADDRESS)
    start_http_server(EXPORTER_PORT)
    while True:
        update_metrics(p)
        time.sleep(RUN_INTERVAL)