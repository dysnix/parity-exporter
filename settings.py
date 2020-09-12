import os

RPC_ADDRESS = os.environ.get('RPC_ADDRESS', 'http://localhost:8545')
EXPORTER_PORT = int(os.environ.get('EXPORTER_PORT', 8000))
RUN_INTERVAL = int(os.environ.get('RUN_INTERVAL', 5))
