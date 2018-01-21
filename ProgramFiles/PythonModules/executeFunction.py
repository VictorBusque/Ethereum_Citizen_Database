#!/usr/bin/python

import os
import subprocess
import sys
import time
import signal
import ethereumUtils

def computeOutput(username, contract, function, params, gas = 1000000, printing = True, unlocking = False, tipus = '0'):
	if not printing:
		ethereumUtils.blockPrint()
	
	try:
		abi,tH,cA = ethereumUtils.get_contract_info(username,contract)
		address = ""
		password = ""
		if (tipus == '0'):
			print ("tipus == 0") 
			address, password = ethereumUtils.get_user_address_pass(username)
		elif (tipus == '1'):
			print ("tipus == 1") 
			address, password = ethereumUtils.get_user_address_pass_entitat_adm(username)
		else:
			print ("tipus == 2") 
			address, password = ethereumUtils.get_user_address_pass_entitat_sub(username)

		if unlocking:
			ethereumUtils.unlock_account(address, password) # Not necessary, login already unlocked account.
	except:
		print "username or contract parameters do not exist."
		sys.exit(1)
	try:
		if cA == "":
			cA = ethereumUtils.retrieve_contract_address(tH)
	except:
		print "Contract is not mined, so cA is not retrieved."
		sys.exit(1)
	
	inParams = ""
	if len(params) > 0:
		for parameter in params:
			inParams += parameter+', '		

	try:
		output = ethereumUtils.execute_function(abi, cA, address, function, inParams)
	except:
		print "Could not call method."
		sys.exit(1)

	return output


if __name__ == '__main__':	
	try:
		username = sys.argv[1]
		contract = sys.argv[2]
		function = sys.argv[3]
		gas = sys.argv[4]
		tipus = sys.argv[5]
		params = []
		if (len(sys.argv) > 6):
			params = sys.argv[6:]
		print computeOutput(username, contract, function, params, gas, tipus = tipus, unlocking = True)
	except:
		print "Parameters: 1. username, 2. contract reference, 3.function's name, 4. gas, +5. parameters"
		sys.exit(1)
