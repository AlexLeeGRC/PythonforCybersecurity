import requests
import json

url = "http://api.open-notify.org/astros.json"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

astronauts = response.json()

# prettify
# print(json.dumps(astronauts, indent=2))

# specific data
print("There are {0} people in space now".format(astronauts["number"]))

print("The first astronaut listed is {0}, aboard the {1}".format(astronauts["people"][0]["name"], astronauts["people"][0]["craft"]))
