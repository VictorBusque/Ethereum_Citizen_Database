geth --datadir ./mainNode --networkid 22 --exec "loadScript('$1')" --fast attach "./mainNode/geth.ipc"
