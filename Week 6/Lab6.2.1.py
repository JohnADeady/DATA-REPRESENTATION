import requests
import json

apiKey = 'f59b1cdb743ce0ab9b21a94ac246b02f06ee2d85'
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'
filename = "deezer.json"


response = requests.get(url, auth=('token',apiKey))
data = response.json()

#print (response.json())
file = open(filename, 'w')
json.dump(data, file, indent=4)