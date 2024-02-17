from ez import check_force_stop
from bs4 import BeautifulSoup
import requests
import sys

list_url = {
    "https://www.samsung.com/hk/multistore/hkeducation/feature.NP960QFG-KA1HK/",
    "https://www.samsung.com/hk/multistore/hkeducation/feature.NP950QED-KH1HK/",
    "https://www.samsung.com/hk/multistore/hkeducation/feature.NP930QED-KA1HK/",
    "https://www.samsung.com/hk/multistore/hkeducation/feature.NP730QED-KF1HK/",
    "https://www.samsung.com/hk/multistore/hkeducation/feature.NP930QED-KH1HK/"
}

with open('spec.txt', mode='w', encoding="utf-8") as f:
	original_stdout = sys.stdout
	sys.stdout = f

	for url in list_url:
		html_text = requests.get(url).text
		soup = BeautifulSoup(html_text,"lxml")

		title = soup.find(class_="pd-header-navigation__headline-text")
		print (title.text.strip())

		price = soup.find(class_="pd-buying-price__new-price")
		print (price.text.strip())

		content = soup.find_all("div",class_="spec-highlight__detail")
		for i, item in enumerate(content):
				s = item.text.strip()
				s = s.replace('\n\n\n\n\n','\t')
				print (f"{s}")

		print("\n\n\n\n")

	sys.stdout = original_stdout