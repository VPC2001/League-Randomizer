import requests
import random


def get_name():
        all_champs = []

        get_champs = requests.get("https://ddragon.leagueoflegends.com/cdn/12.11.1/data/en_US/champion.json")

        data_names = get_champs.json()

        for champ in data_names["data"]:
                all_champs.append(data_names["data"][champ]["name"])

        print("Champion: ", all_champs[random.randrange(0,len(all_champs))])

def get_items():
        all_items = []

        get_items = requests.get("https://ddragon.leagueoflegends.com/cdn/16.5.1/data/en_US/item.json")

        data_items = get_items.json()

        #print(data_items)


        for item in data_items["data"]:
                if data_items["data"][item]["gold"]["purchasable"] and data_items["data"][item]["maps"]["11"] and "into" not in data_items["data"][item] and "from" in data_items["data"][item]:
                        all_items.append(data_items["data"][item]["name"])

        for x in range(1, 6):
                print(f"{x} item: ", all_items[random.randrange(0,len(all_items))])

get_name()
get_items()