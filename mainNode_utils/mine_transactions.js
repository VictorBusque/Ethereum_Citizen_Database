var mining_threads = 2;

function checkWork() {
    if (eth.getBlock("pending").transactions.length > 0) {
        if (eth.mining) return;
        console.log("== Pending transactions! Mining...");
        miner.start(mining_threads);
    } else {
        miner.stop();
        console.log("== No transactions! Mining stopped.");
    }
}
function sleep(delay) {
	var start = new Date().getTime();
	while (new Date().getTime() < start + delay);
}
eth.filter("latest", function(err, block) { checkWork(); });
eth.filter("pending", function(err, block) { checkWork(); });
while (eth.getBlock("pending").transactions.length == 0) {
	console.log('No transactions pending. Waiting 3 seconds.');
 	sleep(3000);
	if (!eth.mining) miner.start(mining_threads);
}
console.log('Set checkWork, now only mine when there are transactions pending.');
checkWork();
