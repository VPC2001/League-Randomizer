import requests

a = requests.get("https://ddragon.leagueoflegends.com/cdn/12.11.1/data/en_US/champion.json")

data = a.json()

for champ in data["data"]:
        print(data["data"][champ]["name"])