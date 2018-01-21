#geth --datadir eth_nodes --networkid 22 --exec "personal.unlockAccount(eth.coinbase, '$2', 0)" #attach "eth_nodes/geth.ipc"
geth --datadir eth_nodes --unlock $1 --password "Data/pass.pw" --networkid 22 --verbosity 1 #attach "eth_nodes/geth.ipc"

