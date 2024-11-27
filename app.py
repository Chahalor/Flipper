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
import DB

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
	# profit = entrer(0, False, "Caerleon", "Black Market")
	# write_json("profit.json", profit)
	# print(read_item_ids("Items/equipement.txt"))
	# read_item_ids("Items/equipement.txt")
	list_items = ["T4_BAG", "T4_BAG@1", "T4_BAG@2"]
	root = Root(["Caerleon", "Black Market"])
	data:Root = get_items_data(list_items, ["Caerleon", "Black Market"], root)
	prof = get_profits(data, 0, False, "Caerleon", "Black Market", list_items)
	for p in prof:
		print(p)
