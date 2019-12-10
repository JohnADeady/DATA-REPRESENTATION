# import libraries
import requests
import json

apiKey = '6b9d216ab27d6fac8fbee4457758e4ded43a916e'
url = 'https://api.github.com/repos/JohnADeady/dataRepresentation'
filename = "repomine.json"

# create json file
response = requests.get(url, auth=('token',apiKey))
repoJSON = response.json()

# dump to json file
#print (response.json())
file = open(filename, 'w')
json.dump(repoJSON, file, indent=4)