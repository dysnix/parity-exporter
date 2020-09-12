import logging
import requests
import datetime


class RPCError(Exception):
    pass


class Parity:
    JSONRPC_VER = "2.0"

    def __init__(self, rpc_url):
        self.rpc_url = rpc_url

    def make_request(self, method, params=None):
        if params is None:
            params = []
        timestamp = int(datetime.datetime.now().timestamp())

        data = {
            'id': timestamp,
            'method': method,
            'params': params,
            'jsonrpc': self.JSONRPC_VER
        }
        try:
            result = requests.post(self.rpc_url, json=data).json()
        except Exception as e:
            logging.error('Error make request {}: {}'.format(method, e))
            raise RPCError('Error call {}'.format(method))

        try:
            return result['result']
        except:
            logging.error('Error get result for call {}'.format(method))
            raise RPCError('Error call {}'.format(method))

    def eth_blockNumber(self):
        result = self.make_request('eth_blockNumber')
        return int(result, 0)

    def parity_net_peers(self):
        result = self.make_request('parity_netPeers')
        return len(result['peers']), int(result['active']), int(result['connected'])