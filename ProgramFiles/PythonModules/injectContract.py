#!/usr/bin/python

import os
import subprocess
import sys
import time
import signal
import ethereumUtils


#__author__      = "Victor Busque"


def run(contract, username, params, gas = 1000000, printing = True, unlocking = False, tipus = "0"):
	if not printing:
		ethereumUtils.blockPrint()

	bytecodes = []
	abis =  []
	tHs = []
	cAs = []	
	address = ""
	password = ""
	if (tipus == '0'):
		address, password = ethereumUtils.get_user_address_pass(username)
	elif (tipus == '1'):
		address, password = ethereumUtils.get_user_address_pass_entitat_adm(username)
	else:
		address, password = ethereumUtils.get_user_address_pass_entitat_sub(username)

	if unlocking:
		ethereumUtils.unlock_account(address, password) # Not necessary, login already unlocked account.

	try:
		bytecodes = ethereumUtils.get_compilation_result("bin", contract)
		abis = ethereumUtils.get_compilation_result("abi", contract)
	except:
		print "Error at generating or getting contract bytecode or abi."
		return 0


	print "number of contracts compiled = " + str(len(bytecodes))

	try:
		for i in range(0, len(abis)):
			ethereumUtils.create_injecting_script(abis[i], bytecodes[i], address, params, gas) #CScript.js created
			tH = ethereumUtils.try_injection(i)
			os.remove("JsContracts/CScript.js")
			if tH == None:
				print "Returning 0, maybe no sufficient ether."
				return 0
			else:
				tHs.append(tH) #We still don't have the address
				cAs.append(None)

	except:
		print "Error at injecting contracts"
		return 0


	i = 0
	any_not_mined = False
	while (i < len(tHs)): #tHs[i] + abis[i] -> cAs[i]
		print "Checking for contract " + str(i) + " mining."
		with open("Data/ContractDB.db","a") as cDB:
			contract_ = str(username+'~'+abis[i]+'~'+'tH:'+tHs[i]+'~'+'cA:\n')
			cDB.write(contract_)
		
		for j in range(0,10):
			cA = ethereumUtils.retrieve_contract_address(tHs[i])
			if cA != None:
				print "----- Contract was mined! -----"
				cAs[0] = cA
				i+=1
				break
			else:
				print "Contract not mined, check number " + str(j)
				time.sleep(1)
				if j == 9:
					any_not_mined = True
					i+=1

	if any_not_mined:
		print "Not every contract was mined, returning 1"
		return 1
	else:
		print "Every contract was mined, returning 2"
		return 2
		

if __name__ == '__main__':	
	try:
		contract = sys.argv[1]
		username = sys.argv[2]
		gas = sys.argv[3]
		tipus = sys.argv[4]
		params = []
		if (len(sys.argv) > 5):
			params = sys.argv[5:]
		run(contract, username, params, gas, tipus = tipus, unlocking = True)
	except:
		print "Parameters: 1. the '.sol', 2.username, 3. gas, +4. parameters"
		sys.exit(1)
