#!/usr/bin/python

import sys
import os
from subprocess import call

def createEntitatAdm(username, password):
	try:
		database = open("Data/EntitatsDB.db","r")
	except:
		print "Database is empty, will create a new Database."
		database = open("Data/EntitatsDB.db","w+")
		
	try:
		if username in database.read():
			print "Username already in the database."
			raise Exception("Username already in the database.")
	except Exception, e:
		raise Exception(e)

	try:
		passFile = open("Data/pass.pw","w")
		passFile.write(password)
		passFile.close()
	except:
		print "Could not save the password."
		os.remove('Data/pass.pw')
		raise Exception("Could not save the password.")

	try:
		call(["bash","./BashModules/createUser.sh"])
	except:
		print "Error at calling generateUser script"
		os.remove('Data/pass.pw')
		raise Exception("Error at calling generateUser script")

	try:
		addressFile = open("Data/address.add","r")
		addressFile = addressFile.readline()
		address = addressFile.partition('{')[-1].rpartition('}')[0]
	except:
		print "Could not read the Ethereum address correctly."
		raise Exception("Could not read the Ethereum address correctly.")

	try:
		with open("Data/EntitatsDB.db", "a") as database:
			database.write(username+'~0x'+address+'~'+password+'\n')
	except:
		print "Could not store the DataBase."
		os.remove('Data/pass.pw')
		os.remove('Data/address.add')
		raise Exception("Could not store the DataBase.")

	try:
		os.remove('Data/pass.pw')
		os.remove('Data/address.add')
	except:
		print "Could not delete temp files."
		raise Exception("Could not delete temp files.")


def createEntitatSub(username, password):
	try:
		database = open("Data/SubvencionsDB.db","r")
	except:
		print "Database is empty, will create a new Database."
		database = open("Data/SubvencionsDB.db","w+")
		
	try:
		if username in database.read():
			print "Username already in the database."
			raise Exception("Username already in the database.")
	except Exception, e:
		raise Exception(e)

	try:
		passFile = open("Data/pass.pw","w")
		passFile.write(password)
		passFile.close()
	except:
		print "Could not save the password."
		os.remove('Data/pass.pw')
		raise Exception("Could not save the password.")

	try:
		call(["bash","./BashModules/createUser.sh"])
	except:
		print "Error at calling generateUser script"
		os.remove('Data/pass.pw')
		raise Exception("Error at calling generateUser script")

	try:
		addressFile = open("Data/address.add","r")
		addressFile = addressFile.readline()
		address = addressFile.partition('{')[-1].rpartition('}')[0]
	except:
		print "Could not read the Ethereum address correctly."
		raise Exception("Could not read the Ethereum address correctly.")

	try:
		with open("Data/SubvencionsDB.db", "a") as database:
			database.write(username+'~0x'+address+'~'+password+'\n')
	except:
		print "Could not store the DataBase."
		os.remove('Data/pass.pw')
		os.remove('Data/address.add')
		raise Exception("Could not store the DataBase.")

	try:
		os.remove('Data/pass.pw')
		os.remove('Data/address.add')
	except:
		print "Could not delete temp files."
		raise Exception("Could not delete temp files.")


def createUser(username, password):
	try:
		database = open("Data/UserDB.db","r")
	except:
		print "Database is empty, will create a new Database."
		database = open("Data/UserDB.db","w+")

	try:
		if username in database.read():
			print "Username already in the database."
			raise Exception("Username already in the database.")
	except Exception, e:
		raise Exception(e)

	try:
		passFile = open("Data/pass.pw","w")
		passFile.write(password)
		passFile.close()
	except:
		print "Could not save the password."
		os.remove('Data/pass.pw')
		raise Exception("Could not save the password.")

	try:
		call(["bash","./BashModules/createUser.sh"])
	except:
		print "Error at calling generateUser script"
		os.remove('Data/pass.pw')
		raise Exception("Error at calling generateUser script")

	try:
		addressFile = open("Data/address.add","r")
		addressFile = addressFile.readline()
		address = addressFile.partition('{')[-1].rpartition('}')[0]
	except:
		print "Could not read the Ethereum address correctly."
		raise Exception("Could not read the Ethereum address correctly.")

	try:
		with open("Data/UserDB.db", "a") as database:
			database.write(username+'~0x'+address+'~'+password+'\n')
	except:
		print "Could not store the DataBase."
		os.remove('Data/pass.pw')
		os.remove('Data/address.add')
		raise Exception("Could not store the DataBase.")

	try:
		os.remove('Data/pass.pw')
		os.remove('Data/address.add')
	except:
		print "Could not delete temp files."
		raise Exception("Could not delete temp files.")

if __name__ == '__main__':
	createUser(sys.argv[1],sys.argv[2])
