import requests

resp = requests.get ('https://api.github.com/events')
print('STATUS',resp.status_code)
json = resp.json ()

print(json)


for var_email in json:
    if var_email == 'email':
        valor = json[var_email]
    print(valor)