# Import libraries
import requests
import json

data={'id':219516100}

apiKey = 'f59b1cdb743ce0ab9b21a94ac246b02f06ee2d85'
url = 'https://api.github.com/repos/datarepresentationstudent/aPrivateOne'

# dump to json
response = requests.put(url, json=data, auth=('token',apiKey))

# print status code and text
print (response.status_code)
print (response.text)