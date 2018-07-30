import requests

url = 'http://192.168.0.7/json.txt'

#Get the JSON decoded file
r = requests.get(url, allow_redirects=True)
open('json.txt', 'wb').write(r.content)

#Print the response code
print r 
