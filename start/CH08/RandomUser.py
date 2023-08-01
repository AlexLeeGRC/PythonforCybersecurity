import requests
import json

url = "https://randomuser.me/api/"

payload={}
headers = {}

#gender = input("Would you like gendered results? m/f")
#if gender.casefold == 'm':
#    headers.update({"gender": "male"})
#elif gender.casefold == 'f':
#    headers.update({"gender": "female"})
#else:
#    headers.update({""})

response = requests.request("GET", url, headers=headers, data=payload)

rando = response.json()

# print(response.text)

#print(json.dumps(rando, indent=2))
# prettified
#print("Test, the location is: {0}, {1}, {2}".format(rando["results"][0]["location"]["city"],rando["results"][0]["location"]["state"],rando["results"][0]["location"]["country"]))
print("The new user is: {0} {7} {8}\n Gender: {1} \n Age: {2} \n From: {3}, {4}, {5} \n Email: {6}".format(
    rando["results"][0]["name"]["title"],rando["results"][0]["gender"],rando["results"][0]["dob"]["age"],rando["results"][0]["location"]["city"],rando["results"][0]["location"]["state"],rando["results"][0]["location"]["country"],rando["results"][0]["email"],rando["results"][0]["name"]["first"],rando["results"][0]["name"]["last"]))