import requests
import random


def get_name():
        all_champs = []

        get_champs = requests.get("https://ddragon.leagueoflegends.com/cdn/12.11.1/data/en_US/champion.json")

        data_names = get_champs.json()

        for champ in data_names["data"]:
                all_champs.append(data_names["data"][champ]["name"])

        champ_name = all_champs[random.randrange(0,len(all_champs))]

        url_champs_stats = requests.get(f"https://ddragon.leagueoflegends.com/cdn/16.5.1/data/en_US/champion/{champ_name}.json")

        champ_stats_data = url_champs_stats.json()

        print(f"Champion: {champ_name}")
        
        index = random.randrange(0, 3)

        random_ability = champ_stats_data["data"][champ_name]["spells"][index]["name"]

        abilities = ["Q", "W", "E"]

        print(f"\nAbility to max: {abilities[index]} ({random_ability})")


def get_items():
        all_items = []

        all_boots = []

        get_items = requests.get("https://ddragon.leagueoflegends.com/cdn/16.5.1/data/en_US/item.json")

        data_items = get_items.json()


        for item in data_items["data"]:
                if data_items["data"][item]["gold"]["purchasable"] and data_items["data"][item]["maps"]["11"] and "into" not in data_items["data"][item] and "from" in data_items["data"][item]:
                        all_items.append(data_items["data"][item]["name"])
                if data_items["data"][item]["gold"]["purchasable"] and data_items["data"][item]["maps"]["11"] and "from" in data_items["data"][item]:
                        for boot in data_items["data"][item]["from"]:
                                if boot == "1001":
                                        all_boots.append(data_items["data"][item]["name"])

        rand_item = random.sample(all_items, 5)

        print(f"Boots: {random.choice(all_boots)}")

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

        rune_path = random.sample(list(range(0, len(data_runes))), 2)
 
        # Used this to understand how to pick things from the list 
        # for x in range(len(data_runes)):
        #         print(data_runes[x]["name"])
        #         for y in range(len(data_runes[x]["slots"])):
        #                 for z in range(len(data_runes[x]["slots"][y]["runes"])):
        #                         print(data_runes[x]["slots"][y]["runes"][z]["name"])

        # Primary Rune Path
        print("Runes 1st part: ")
        print(data_runes[rune_path[0]]["name"])
        for i in range(0, 4):
                print(data_runes[rune_path[0]]["slots"][i]["runes"][random.randrange(0,3)]["name"])

        # Secondary Rune Path
        minor_runes = random.sample(range(1,4), 2)
        print("\nRunes 2nd part: ")
        print(data_runes[rune_path[1]]["name"])
        for x in minor_runes:
                print(data_runes[rune_path[1]]["slots"][x]["runes"][random.randrange(0,3)]["name"])

        # Stats Shards
        stat_shards = [
                ["Adaptive Force", "Attack Speed", "Ability Haste"],
                ["Adaptive Force", "Move Speed", "Health Scaling"],
                ["Scaling Health", "Tenacity and Slow Resist", "Health Scaling"]
        ]

        print("\nStats Shards: ")
        for y in range(len(stat_shards)):
                print(stat_shards[y][random.randrange(0, 3)])




for _ in range(1):
        get_name()
        print()
        get_roles()
        print()
        get_spells()
        print()
        get_items()
        print()
        get_runes()