#!/usr/bin/python

import os
import subprocess
import sys
import time
import signal
import re
#__author__      = "Victor Busque"

def block_print():
    sys.stdout = open(os.devnull, 'w')


def get_contract_info(username,index=0):
	con = 0
	try:
		for line in open("Data/ContractDB.db","r").readlines():
			contract = line.split('~')
			user = contract[0]
			abi = contract[1]
			tH = contract[2].split(':')[1]
			cA = contract[3].split(':')[1].split('\n')[0]
			if (username == user) & (str(con) == str(index)):
				return abi,tH,cA
			elif username == user:
				con += 1
		return None
	except:
		print "Could not get contract's information."
		sys.exit(1)


def getManagerAddress():
	return str(open("Data/Manager.addr","r").read()[:-1])


def get_user_address_pass(username):
	try:
		database = open("Data/UserDB.db","r").readlines()
		address = ""
		password = ""
		for account in database:
			info = account.split('~')
			if info[0] == username:
				address = info[1]
				password = info[2].split('\n')[0]
				return address, password
	except:
		print "Could not retrieve user information."
		sys.exit(1)


def get_user_address_pass_entitat_adm(username):
	try:
		database = open("Data/EntitatsDB.db","r").readlines()
		address = ""
		password = ""
		for account in database:
			info = account.split('~')
			if info[0] == username:
				address = info[1]
				password = info[2].split('\n')[0]
				return address, password
	except:
		print "Could not retrieve user information."
		sys.exit(1)


def get_user_address_pass_entitat_sub(username):
	try:
		database = open("Data/SubvencionsDB.db","r").readlines()
		address = ""
		password = ""
		for account in database:
			info = account.split('~')
			if info[0] == username:
				address = info[1]
				password = info[2].split('\n')[0]
				return address, password
	except:
		print "Could not retrieve user information."
		sys.exit(1)


def unlock_account(address, password):
	try:
		passFile = open("Data/pass.pw","w")
		passFile.write(password)
		passFile.close()
	except:
		print "Error at writting password file."
		sys.exit(1)

	try:
		os.system("x-terminal-emulator -e 'bash ./BashModules/unlockAccount.sh "+address+"'")
		#os.remove('Data/pass.pw')
	except:
		print "Error at calling unlockAccount script. Maybe it is opened already and we can attach"
		#os.remove('Data/pass.pw')
		return
	time.sleep(5)

def connect_and_sync():
	try:
		subprocess.call(['gnome-terminal','-e',"bash ./BashModules/connectGeth.sh"])
		time.sleep(5)
	except:
		print "Error at sync."
		sys.exit(1)


def retrieve_contract_address(tH):
	try:
		file = open("JsContracts/FCAScript.js","w")
		file.write('var tH = "'+tH+'"\n'
			+ 'cAddress = eth.getTransactionReceipt(tH).contractAddress;\n'
			+ 'console.log(cAddress)\n')
		file.close()
		username = abi = ""
		so = subprocess.check_output(["bash","./BashModules/executeScript.sh",'JsContracts/FCAScript.js'])
		so = so.split('\n')
		if str(so[-2]) == "true":
			cA = so[0]
			ln = 0
			for line in open("Data/ContractDB.db","r").readlines():
				contract = line.split('~')
				username = contract[0]
				abi = contract[1]
				tH_a = contract[2].split(':')[1]
				if tH == tH_a:
					break
				else: 
					ln+=1
			aux = []
			with open("Data/ContractDB.db","r") as cDB:
				aux = cDB.readlines()
			aux[ln] = str(username+'~'+abi+'~tH:'+tH+'~cA:'+cA+'\n')
			with open("Data/ContractDB.db","w") as cDB:
				cDB.writelines(aux)
			os.remove('JsContracts/FCAScript.js')
			return cA
		os.remove('JsContracts/FCAScript.js')
	except:
		print 'Could not retrieve and write the address. Maybe contract is not mined.'
		os.remove('JsContracts/FCAScript.js')
		return None	


def execute_function(abi, cA, address, function, parameters, gas = 1000000):
	try:
		file = open("JsContracts/FScript.js","w")
		file.write('var abi = '+abi+';\n'
			+ 'var myContract = eth.contract(abi);\n'
			+ 'var cInstance = myContract.at("'+cA+'")\n'
			+ 'eth.defaultAccount = "'+address+'"\n'
			+ 'console.log(cInstance.'+function+'('+parameters+'{from:"'+address+'", gas: '+str(gas)+'}));\n')	
		file.close()
	except:
		print "Could not create FScript.js ."
		sys.exit(1)
	try:
		so = subprocess.check_output(['bash','./BashModules/executeScript.sh','JsContracts/FScript.js'])
		so = so.split('\n')
		return so[:-2]
	except:
		print "Error at executing script command."
		os.remove('JsContracts/FScript.js')
		sys.exit(1)


def execute_function_on_Person(contractAddressOfPerson, accountOfEntity, function, parameters, gas = 1000000):
	abi  = get_compilation_result("abi", "SolidityContracts/Person.sol")[0]
	return execute_function(abi, contractAddressOfPerson, accountOfEntity, function, parameters, gas)


def execute_function_on_Manager(accountOfEntity, function, parameters, gas = 1000000):
	abi  = get_compilation_result("abi", "SolidityContracts/Manager.sol")[0]
	cA = getManagerAddress()
	return execute_function(abi, cA, accountOfEntity, function, parameters, gas)


def get_compilation_result(type_, contract):
	if type_ == "bin":
		bytecode = subprocess.check_output(['solc','--bin',contract])
		print "Bytecode generated succesfully."
		start = '======= '
		end = ':'
		c_names = re.findall('%s(.*)%s' % (start, end), bytecode)
		print "Compiled the following contracts: %s", str(c_names)
		i = 0
		for contract_ in c_names:
			if contract_ == contract:
				break;
			else:
				i += 1
		bytecode = str(bytecode).split('Binary:')
		bytecodes = bytecode[1:]
		j = 0
		for bytecode in bytecodes:
			if j == i:
				return [('0x'+bytecode[2:].partition('\n')[0])]
			else:
				j += 1
	elif type_ == "abi":
		abi = subprocess.check_output(['solc','--abi',contract])
		print "Abi generated succesfully."
		start = '======= '
		end = ':'
		c_names = re.findall('%s(.*)%s' % (start, end), abi)
		print "Compiled the following contracts: %s", str(c_names)
		i = 0
		for contract_ in c_names:
			if contract_ == contract:
				break;
			else:
				i += 1
		abi = str(abi).split('Contract JSON ABI')
		abis = abi[1:]
		j = 0
		for abi in abis:
			if j == i:
				return [(abi[2:].partition('\n')[0])]
			else:
				j+=1
	else:
		print "Wrong type of compilation"
		sys.exit(1)
	return result


def create_injecting_script(abi, bytecode, address, params, gas = 1000000):
	try:
		inParams = ""
		if len(params) > 0:
			inParams = params[0]+', '
			for parameter in params[1:]:
				inParams += parameter+', '

		file = open("JsContracts/CScript.js","w")
		file.write('var abi = '+abi+';\n'
			+ 'var myContract = eth.contract(abi);\n'
			+ "var bytecode = '"+bytecode+"';\n"
			+ 'var txDeploy = {from:"'+address+'", data: bytecode, gas: '+str(gas)+'};\n'
			+ 'var myContractPartialInstance = myContract.new('+inParams+'txDeploy,'
			+ 'function(err, myContract){\n'
			+ '	if(!err) {\n'
			+ '		if(!myContract.address) console.log("tH:"+myContract.transactionHash)\n'
			+ '		else console.log("cA:"+myContract.address)\n'
			+ '	}\n'
			+ ' else console.log(err);\n'
			+ '});\n')	
		file.close()
	except:
		print "Could not create script"


def try_injection(i):
	sent = False
	j = 0
	print "\n\nStarting attaching process to inject contract..."+str(i)
	while j <= 3 :
		print "Attempt number... "+str(j)
		try:
			so = subprocess.check_output(["bash","./BashModules/injectContract.sh"])
			so = so.split('\n')
			sent = so[0].split(':')[0] == "tH"
			if sent:
				tH = str(so[0].split(':')[1])
				print "---- Contract was injected, now is waiting to be mined. ----\n\n"
				return tH
			else:
				print "Error, log is:"
				print so
				j+=1
				time.sleep(1)
		except:
			print "Injection failed, IPC not yet attached."
			j+=1
			time.sleep(1)
	print "Could not inject."
	return None


def kill_geth():
	so = subprocess.check_output(["ps","-A"])
	so = so.split('\n')
	for proc in so:
		if "geth" in proc:
			pid = int(proc.split(None, 1)[0])
	try:	
		os.kill(pid, signal.SIGKILL)
	except:
		print "Killing unlocked account failed."
		sys.exit(1)
