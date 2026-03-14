import requests
import random


def get_name():
        all_champs = []

        get_champs = requests.get("https://ddragon.leagueoflegends.com/cdn/12.11.1/data/en_US/champion.json")

        data_names = get_champs.json()

        for champ in data_names["data"]:
                all_champs.append(data_names["data"][champ]["name"])

        print("Champion:", all_champs[random.randrange(0,len(all_champs))])

def get_items():
        all_items = []

        get_items = requests.get("https://ddragon.leagueoflegends.com/cdn/16.5.1/data/en_US/item.json")

        data_items = get_items.json()

        for item in data_items["data"]:
                if data_items["data"][item]["gold"]["purchasable"] and data_items["data"][item]["maps"]["11"] and "into" not in data_items["data"][item] and "from" in data_items["data"][item]:
                        all_items.append(data_items["data"][item]["name"])

        rand_item = random.sample(all_items, 5)

        for x in range(0, 5):
                suffix = "st" if x == 1 else "nd"
                print(f"{x+1}{suffix} item: {rand_item[x]}")


def get_spells():
        all_spells = []

        get_spells = requests.get("https://ddragon.leagueoflegends.com/cdn/16.5.1/data/en_US/summoner.json")
        
        data_spells = get_spells.json()

        for spell in data_spells["data"]:
                for x in data_spells["data"][spell]["modes"]:
                        if x == "CLASSIC":
                                all_spells.append(data_spells["data"][spell]["name"])

        rand_spell = random.sample(all_spells, 2)

        for x in range(0, len(rand_spell)):
                suffix = "st" if x == 1 else "nd"
                print(f"{x+1}{suffix} spell: {rand_spell[x]}")
                
def get_roles():
        # No API for this
        all_roles = ["Top", "Jungle", "Mid", "Adc", "Support"]

        rand_role = random.choice(all_roles)

        print(f"Role: {rand_role}")

def get_runes():
        get_runes = requests.get("https://ddragon.leagueoflegends.com/cdn/16.5.1/data/en_US/runesReforged.json")

        data_runes = get_runes.json()

        rune_head = random.randrange(0,4)

        # Used this to understand how to pick things from the list 
        # for x in range(len(data_runes)):
        #         print(data_runes[x]["name"])
        #         for y in range(len(data_runes[x]["slots"])):
        #                 for z in range(len(data_runes[x]["slots"][y]["runes"])):
        #                         print(data_runes[x]["slots"][y]["runes"][z]["name"])
                                

        print(data_runes[rune_head]["name"])
        for i in range(0, 4):
                print(data_runes[rune_head]["slots"][i]["runes"][random.randrange(0,3)]["name"])

# get_name()
# print()
# get_roles()
# print()
# get_spells()
# print()
# get_items()
get_runes()