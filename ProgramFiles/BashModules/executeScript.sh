geth --datadir eth_nodes --networkid 22 --exec "loadScript('$1')" --fast attach "eth_nodes/geth.ipc"
