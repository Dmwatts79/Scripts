import requests

request = requests.get("http://api.open-notify.org/astros.json")
request = request.json()
print(request)


print("Number of people in space:", request['number'])
for name in request['people']:
    print(name['name'])
