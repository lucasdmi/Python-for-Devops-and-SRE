
import requests

resp = requests.get ('https://www.google.com/')
print('STATUS',resp.status_code)
json = resp.json ()
print(json[0])

