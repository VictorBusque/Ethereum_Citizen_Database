var sender = eth.coinbase
var receiver = "0xc0b9bf8d91ee207586abe7d1fc33648e7ee99e74";
var amount = web3.toWei(22, "ether");
eth.sendTransaction({from:sender, to:receiver, value: amount})
