import requests
import json

url = "https://icanhazdadjoke.com/?Accept=application/json&User-Agent=APIHomework (https://github.com/AlexLeeGRC/PythonforCybersecurity)"

payload={}
headers = {
  'Accept': 'application/json',
  'User-Agent': 'APIHomework (https://github.com/AlexLeeGRC/PythonforCybersecurity)'
}

response = requests.request("GET", url, headers=headers, data=payload)

joke = response.json()

# print(response.text)
# prettify
# print(json.dumps(joke, indent=2))
print("{0}".format(joke["joke"]))