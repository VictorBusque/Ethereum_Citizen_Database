Daniel Alcocer, Anass Benali, Víctor Busqué, Roger Mas
# Ethereum_Citizen_Database
Ethereum-based Citizen database, provides a framework and tools to create a private Ethereum network in which to run a database of citizens.
# First time usage
Execute the setup.py script. That will generate a new node for you to work with. Once this is done, you will see an "eth_nodes" folder being created. This is your brand new node.
# Interacting with the node
Running the run.py script will execute the GUI which can be used to interact with every functionality of the prototype. You can either create new users and submit their information to the blockchain (once the account validating process has been done successfully), modify your information so it will be sent to the administration to be validated, etc.
Please, note that in order to run properly, there are two roles necessary, client (the node set up at the beggining), and a mining central node, but this requieres more setup that could not be automatized on the prototype. 
The idea is that you can generate your "mainNode" using geth itself by running
```
    geth --datadir mainNode init ProgramFiles/JSonFiles/genesis.json
```
Then, you can create your unique mainNode account by running:
```
    geth --datadir mainNode account new
```
And then by introducing a password you will be able to generate your new account.
Now, to use the mainNode utilities provided in this repository, you should substitute the content on the mainNode_utils on file info.db by something like:
```
    <your_account_address>~<your_account_password>
```
Then you will be able to use the MN_Send_ether.py script that given an account (usually from the eth_nodes datadir) and an amount of ether, is able to send this ether (requiring a transaction, and therefore, mining). With all of this you will be able to start using the Ethereum network successfully.

Since the main function of mainNode is to mine, in mainNode_utils the mine_trans_auto.sh file is also available, which allows you to automatically mine when there are pending transactions.
# Previous before being able to create the other nodes:
Once the mainNode is created, you have to create a Manager of your network. For this purpose, the following steps must be carried out:

1.- Create an Administrative Entity:

To do so, it will be enough to create a new account.

2.- Give ether to the new account:

Using MN_Send_ether.py script, described in the previous section, we will be able to transfer ether to the new account. We can get the account of the new account in the file: "ProgramFiles/Data/UserDB.db"

3.- Create the Manager:

Once we have given ether to the account, we can create the manager in the following way, from ProgramFiles:
```
python PythonModules/injectContract.py SolidityContracts/Manager.sol <name> '4712388' '"<account>"'
```
This step also needs mining.

4.- Create the file Manager.addr:

For the program to work properly it is necessary to have the address of the contract Manager in the file Manager.addr inside the Data folder of ProgramFiles. To obtain the address you have to look in the file "ProgramFiles/Data/ContractDB.db".

# Establishing your own private network
Now you need to make sure your central network and your client network can discover themselves. This can be done by either re-defining the contents on the static-nodes.json inside your eth_nodes/geth folder, or by checking https://github.com/ethereum/go-ethereum/wiki/Connecting-to-the-network information about how to do so.
