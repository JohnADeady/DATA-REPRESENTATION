import requests, json
from xlwt import *

#url = "https://api.github.com/users?since=100"
url = "https://api.github.com/users/andrewbeattycourseware/followers"

response = requests.get(url)
data = response.json()
print(data)

# output cars individually
for followers in data:
	print(followers)
	
#Get the file name for the new file to write
filename = 'githubusers.json'
with open(filename, 'w') as f:
 json.dump(data, f, indent=4)
 

# write to excel file
w = Workbook()
ws = w.add_sheet('followers')
row = 0;

ws.write(row,0,"login")
ws.write(row,1,"id")
ws.write(row,2,"node_id")
ws.write(row,3,"avatar_url")
ws.write(row,4,"gravatar_id")
ws.write(row,5,"url")
ws.write(row,6,"html_url")
ws.write(row,7,"followers_url")
ws.write(row,8,"following_url")
ws.write(row,9,"gists_url")
ws.write(row,10,"starred_url")
ws.write(row,11,"subscriptions_url")
ws.write(row,12,"organizations_url")
ws.write(row,13,"repos_url")
ws.write(row,14,"events_url")
ws.write(row,15,"received_events_url")
ws.write(row,16,"type")
ws.write(row,17,"site_admin")
row += 1

for followers in data:
	ws.write(row,0,followers["login"])
	ws.write(row,1,followers["id"])
	ws.write(row,2,followers["node_id"])
	ws.write(row,3,followers["avatar_url"])
	ws.write(row,4,followers["gravatar_id"])
	ws.write(row,5,followers["url"])
	ws.write(row,6,followers["html_url"])
	ws.write(row,7,followers["followers_url"])
	ws.write(row,8,followers["following_url"])
	ws.write(row,9,followers["gists_url"])
	ws.write(row,10,followers["starred_url"])
	ws.write(row,11,followers["subscriptions_url"])
	ws.write(row,12,followers["organizations_url"])
	ws.write(row,13,followers["repos_url"])
	ws.write(row,14,followers["events_url"])
	ws.write(row,15,followers["received_events_url"])
	ws.write(row,16,followers["type"])
	ws.write(row,17,followers["site_admin"])
	row +=1
	
w.save('followers.xls')

