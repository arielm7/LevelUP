import requests
import json

#String to send
str2Send='Hola'

#Get request
payload = {'request': str2Send}
r = requests.get('http://192.168.0.7/watson.php', params=payload)

print json.dumps(r.text)#Response
print r.status_code     #Status Code


