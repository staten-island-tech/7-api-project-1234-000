import requests


asker = input("What??")

rep  = requests.get(f"https://pokeapi.co/api/v2/pokemon/{asker}")
data = rep.json()

for i in data["abilities"]:
    print(i["ability"]["name"])
print(data["name"])
print(data["weight"])
print(data["height"])
print(data["base_experience"])
