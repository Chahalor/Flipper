'''
Big Header
'''


# Frontend :
# service << min_profit, rune,  ville achat, ville vente
# service >> liste de items [cost, profit, % renta]
#  - dans un tableaux par ordre croissant de renta
# loop sur 5 minutes (reccuperes les data de tout les items) -> 5 minutes entre chaque actualisation d'items


# Backend(min:int, run:bool, ville_achat:str, ville_vente:str) :
# - fleatcher les data de l'api pour chaque item
# - calculer la diff entre les prix d'achat et de vente
# - calculer le profit
# - calculer le % de renta
# - retourner la liste des items rentable

# Description: TODO...
#  /=================================\
# |===========Importations============|
#  \=================================/
from api_utils import *
from data_processing import *
import json

#  /=================================\
# |=========Global Variables==========|
#  \=================================/
MAX_REQUESTS_PER_MINUTE = int(180)
MAX_REQUESTS_PER_5_MINUTES = int(300)
URL_BASE_PRICES_EU = str("https://www.albion-online-data.com/api/v2/stats/prices/")

#  /=================================\
# |============Classes================|
#  \=================================/

# ...

#  /=================================\
# |============Functions==============|
#  \=================================/

def write_json(path: str, data: dict) -> None:
	with open(path, 'w') as json_file:
		json.dump(data, json_file, indent=4)
		json_file.close()

def read_item_ids(file: str) -> list[str]:
	with open(file, 'r') as f:
		data = f.read().splitlines()
		result = []
		for line in data:
			result.append(line.split(':')[1].strip())
	return (result)

def get_profits(stock:dict[dict[dict[dict[int, str]]]], min:int, rune:bool, buy_city:str, sell_city:str)->dict:
	Profit_dict = {}
	print(f"buy_city: {buy_city}, sell_city: {sell_city}")
	for item in stock[buy_city]:
		for quality in stock[buy_city][item]:
			price_buy = stock[buy_city][item][quality]['buy_price_min']
			price_sell = stock[sell_city][item][quality]['sell_price_min']
			if (price_sell - price_buy) * TAX > min and price_buy != 0:
				profit = (price_sell - price_buy) * TAX
				percent = (profit / price_buy) * 100
				Profit_dict.setdefault(item, {
					"quality": quality,
					"buy_price": price_buy,
					"sell_price": price_sell,
					"profit": profit,
					"percent": percent
				})
	return (Profit_dict)


# input : benef min, rune use, ville achat, ville vente
# output : Profit[nom item achat, nom item revente, prix achat, rune cost, prix vente, benef, % renta]
def entrer(min:int=0, rune:bool=False, buy_city:str="Caerleon", sell_city:str="Black Market")->dict:
	all_item_IDs = read_item_ids("Items/equipement.txt")
	# print(all_item_IDs)
	
	stock = dict()
	i = 0
	# for i in range(0, len(all_item_IDs), 40):
	stock = get_items_data(all_item_IDs[i:i+40], [buy_city, sell_city], stock)
	write_json("stock.json", stock)
	Profit_dict = get_profits(stock, min, rune, buy_city, sell_city)
	return (Profit_dict)

#  /=================================\
# |==============Main================|
#  \=================================/
if __name__ == '__main__':
	profit = entrer(0, False, "Caerleon", "Black Market")
	write_json("profit.json", profit)
	# print(read_item_ids("Items/equipement.txt"))
	# read_item_ids("Items/equipement.txt")
