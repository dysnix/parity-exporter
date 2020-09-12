import logging
from prometheus_client import Gauge

eth_block_number = Gauge('eth_block_number', 'The number of most recent block.')
net_peers = Gauge('net_peers', 'The number of peers currently connected to the client.')
parity_net_active_peers = Gauge('parity_net_active_peers', 'The number of active peers.')
parity_net_connected_peers = Gauge('parity_net_connected_peers',
                                   'The number of peers currently connected to the client. Available only for Parity')


def update_metrics(parity):
    total_peers, active_peers, connected_peers = parity.parity_net_peers()
    net_peers.set(total_peers)
    parity_net_active_peers.set(active_peers)
    parity_net_connected_peers.set(connected_peers)

    eth_block_number.set(parity.eth_blockNumber())

    logging.info('Metric updated')
