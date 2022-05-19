from ez import check_force_stop
from bs4 import BeautifulSoup
import requests
import lxml # for hadling XML and HTML file

def	florence_price():
	html_text = requests.get("https://store.steampowered.com/app/1102130/Florence/").text
	soup = BeautifulSoup(html_text,"lxml")

	# if only need to find the first only, then use soup.find
	item_price = soup.find_all("div",class_="game_purchase_price price")
	for i, item in enumerate(item_price):
		print (f"Price #{i}: {item.text.strip()}")
		if (i==0): break

if __name__ == "__main__":
	florence_price()