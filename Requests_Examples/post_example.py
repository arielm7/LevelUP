import requests
import json

url = 'http://192.168.1.73/post.php'
payload = {'some': 'Data'}

#Send the JSON file
r = requests.post(url, data=json.dumps(payload))

#Print the response code
print r
