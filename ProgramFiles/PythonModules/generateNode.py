#!/usr/bin/python

import os
from subprocess import call
import getpass

username = getpass.getuser()
eth_dir = "eth_nodes"
networkid = 22


try :
	os.makedirs(eth_dir)
	print("Folder succesfully created.")
except:
	print("Folder already created, installing geth...")


try:
	call(["bash","BashModules/install_Geth.sh"])
	print("geth succesfully installed.")

except:
	print("geth could not be installed")


try:
	call(["geth","--datadir",eth_dir,"--networkid",str(networkid),"init","JSonFiles/genesis.json"])
	print("Node successfully generated.")
except:
	print("Unknown error happened.")


try:
	call(["cp","JSonFiles/static-nodes.json",eth_dir+"/geth/"])
	print("Peering file succesfully copied.")
except:
	print("Could not copy peering file.")
