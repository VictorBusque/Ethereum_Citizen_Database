#!/usr/bin/python

import os
import subprocess
import sys
import time


def unlock_account():
	file = open("mainNode_utils/info.db","r")
	text = file.readlines()[0]
	address,password = text.split('~')
	passFile = open("mainNode_utils/pass.pw","w")
	passFile.write(password)
	passFile.close()
	try:
		os.system("x-terminal-emulator -e 'bash ./mainNode_utils/unlockAccount.sh "+address+"'")
		time.sleep(5)
	except:
		print "Error at calling unlockAccount script. Maybe it is oppened already and we can attach"
		sys.exit(1)

def send_ether(_to, _amount):
	unlock_account()
	try:
		file = open("./mainNode_utils/SEScript.js","w")
		file.write('var sender = eth.coinbase\n'
			+ 'var receiver = "'+_to+'";\n'
			+ 'var amount = web3.toWei('+_amount+', "ether");\n'
			+ 'eth.sendTransaction({from:sender, to:receiver, value: amount})\n')
		file.close()
	except:
		print "Could not create Sending script."
		sys.exit(1)
	try:
		so = subprocess.check_output(["bash","./mainNode_utils/executeScript.sh",'./mainNode_utils/SEScript.js'])
		so = so.split('\n')
		if so[0] == "True":
			print ("Everything went right")
	except:
		print "Could not call bash"
		sys.exit(1)


if __name__ == '__main__':
	send_ether(sys.argv[1],sys.argv[2])
	sys.exit(1)
