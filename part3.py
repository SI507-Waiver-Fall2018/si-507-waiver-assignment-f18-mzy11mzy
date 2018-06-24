#name: Zhiyi Ma
#unique name: zhiyima
#umid: 48014433

import requests
from bs4 import BeautifulSoup

# write your code here
# usage should be python3 part3.py
print("Michigan Daily -- MOST READ") 

response1 = requests.get("https://www.michigandaily.com")
soup1 = BeautifulSoup(response1.text, "html.parser")

most_read = soup1.find_all("div",class_="view-most-read")
for ol in most_read:
	li = ol.find_all("li")
	for content in li:
		name = content.string
		href = content.a["href"]

		response2 = requests.get("https://www.michigandaily.com" + href)
		soup2 = BeautifulSoup(response2.text, "html.parser")

		author_name = soup2.find_all("div",class_="byline")	
		for div in author_name:
			div2 = 	div.find_all("div",class_="link")
			for content in div2:
				author = content.contents[0].string

		print(name,"\n","by",author)


