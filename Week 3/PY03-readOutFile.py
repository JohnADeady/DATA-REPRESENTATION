#Import requests
import requests
from bs4 import BeautifulSoup


# page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")	
# print(page)
# print("------------")
# print(page.content)
#soup1 = BeautifulSoup(page.content, 'html.parser')
# print("------------")

# Open file with beautiful soup
with open("../Week 2/carviewer2.html") as fp:
	soup = BeautifulSoup(fp, 'html.parser')
	#print(soup.prettify())

# print(soup.tr)

rows = soup.findAll("tr")
for row in rows:
	# print("--------")
	# print(row)
	dataList = []
	cols = row.findAll("td")
	for col in cols:
		# print(col.text)
		dataList.append(col.text)
	print(dataList)