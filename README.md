# parity-exporter
Very simple prometheus exporter for Parity.

The main motivation is not to use ready-made solutions, since their build methods (with the indication of dependencies from GIT) are not safe.
The current mini-exporter is as simple as possible and only uses `requests` as JsonRPC clients, which minimizes security risks.
This code can be forked, reviewed and added to build containers from your repository, which will give the necessary level of peace of mind in order to give it access to your private RPCs.

Provided metrics for:

* `eth_block_number`: The number of most recent block.
* `net_peers`: The number of peers currently connected to the client
* `parity_net_active_peers`: The number of active peers
* `parity_net_connected_peers`: The number of peers currently connected to the client

## Env config variables

* `RPC_ADDRESS` - JsonRPC Parity address
* `EXPORTER_PORT` - Prometheus exporter port
* `RUN_INTERVAL` - JsonRPC call interval