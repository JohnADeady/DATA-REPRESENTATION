# Import libraries
import requests
import json

# Import database from third party api
apiKey = 'f59b1cdb743ce0ab9b21a94ac246b02f06ee2d85'
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'
filename = "deezer.json"

# pull apikey and url rename to json
response = requests.get(url, auth=('token',apiKey))
data = response.json()

#print (response.json())
file = open(filename, 'w')

# Import data
json.dump(data, file, indent=4)