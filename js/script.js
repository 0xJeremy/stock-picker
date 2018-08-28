var stock = ["aapl", "goog", "msft", "mu", "tsla", "mtn", "ba", 
			 "baba", "cat", "unh", "mcd", "jpm", "hd", "axp", "wmt", 
			 "mmm", "gs", "v", "dwdp", "nke", "intc", "csco", "trv", 
			 "pfe", "jnj", "utx", "cvx", "spy", "qqq", "dis", "vz", 
			 "ko", "pg", "ibm", "xom", "mrk", "nflx", "stx", "isrg",];
var stock_names = "";
for(i in stock) {
	stock_names += stock[i] + ", "; 
}
stock_names = stock_names.substring(0, stock_names.length - 2);
document.getElementById('stock-list').innerHTML = stock_names;