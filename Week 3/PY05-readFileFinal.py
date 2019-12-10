# Import libraries
from bs4 import BeautifulSoup
import csv

# Open data in html file
with open("../Lab2.html") as fp:
	soup = BeautifulSoup(fp, 'html.parser')

# Write this to a SCV file	
employee_file = open('employee_file.csv', mode='w')
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# Find rows
rows = soup.findAll("tr")
for row in rows:
	cols = row.findAll("td")
	dataList = []
	
	# store to text file
	for col in cols:
		# print(col.text)
		dataList.append(col.text)
	employee_writer.writerow(dataList)
employee_file.close()