# Import libraries
import requests
import json
from xlwt import *

# webapplication created
url = "http://127.0.0.1:5000/cars"

response = requests.get(url)
data = response.json()

# output to console
print(data)

# output cars individually
for car in data["cars"]:
	print(car)
	

# other code
# save this to a file
filename = 'cars.json'
if filename:
	# Writing JSON data
	with open(filename,'w') as f:
		json.dump(data, f, indent=4)
		

# write to excel file
w = Workbook()
ws = w.add_sheet('cars')
row = 0;

# Create headings
ws.write(row,0,"reg")
ws.write(row,1,"make")
ws.write(row,2,"model")
ws.write(row,3,"price")
row += 1
# Import data
for car in data["cars"]:
	ws.write(row,0,car["reg"])
	ws.write(row,1,car["make"])
	ws.write(row,2,car["model"])
	ws.write(row,3,car["price"])
	row +=1

#save to excel	
w.save('cars.xls')
