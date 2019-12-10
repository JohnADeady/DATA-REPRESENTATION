# Import requests
import requests

# Import reg
url = 'http://127.0.0.1:5000/cars/08%20C%201234'

# delete reg
response = requests.delete(url)

# Print status code
print (response.status_code)

# Print text
print (response.text)