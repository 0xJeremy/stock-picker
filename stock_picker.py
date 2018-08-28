import requests, smtplib
import sys, time
import json

def email_data(data):
	#server = smtplib.SMTP("smtp.gmail.com", 587)
	#server.starttls()
	#server.login([sending email], [password])
	print("\nEmailing information...")
	#server.sendmail([sending email], [target email], data)
	#server.quit()
	print(data)
	
def get_news(stock):
	newsURL = "https://api.iextrading.com/1.0/stock/" + stock + "/news/last/5"
	data = requests.get(url = newsURL)
	news = data.json()
	formatted_data = ""
	for i in news:
		formatted_data = formatted_data + i['headline'] + ":\n" + i['summary'] + "\n\t" + i['url'] + "\n\n"
	print(formatted_data)
	return formatted_data

def check_move(stock, pos):
	URL = "https://api.iextrading.com/1.0/stock/" + stock + "/quote/changePercent"
	r = requests.get(url = URL)
	
	data = r.json()
	data = data*100
	if(data <= -5 and pos == 1):
		return stock + ": " + get_news(stock)
	elif(data >= 5 and pos == -1):
		return stock + ": " + get_news(stock)
	else:
		return ""

def main():
	email_msg = ""
	file = open("info.txt", "w")
	stock = {"aapl", "goog", "msft", "mu", "tsla", "mtn", "ba", 
			 "baba", "cat", "unh", "mcd", "jpm", "hd", "axp", "wmt", 
			 "mmm", "gs", "v", "dwdp", "nke", "intc", "csco", "trv", 
			 "pfe", "jnj", "utx", "cvx", "spy", "qqq", "dis", "vz", 
			 "ko", "pg", "ibm", "xom", "mrk", "nflx", "stx", "isrg",}

	get_news("goog")

	for i in stock:
		URL = "https://api.iextrading.com/1.0/stock/" + i + "/stats/year1ChangePercent"
		print("Retrieving information: " + i + "...")
		r = requests.get(url = URL)
	
		data = r.json()
		percent = data*100

		if percent >= 25:
			file.write("Positive: " + i + "\n")
			info = check_move(i, 1)
			if(info != ""):
				email_msg = email_msg + info + "\n"
		elif percent <= -25:
			file.write("Negative: " + i + "\n")
			info = check_move(i, -1)
			if(info != ""):
				email_msg = email_msg + info + "\n"
		
	file.close()
	if(email_msg != ""):
		email_data(email_msg)
	sys.exit("Finished Compiling Information. Exiting.\n")
		
if __name__=='__main__':
	main()