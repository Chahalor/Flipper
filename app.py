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
MAX_URL_SIZE = int(4096)
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


def tkt(path_db:str, list_items:list[str], list_citys:list[str], list_qualitys:list[str], base_url:str=URL_BASE_PRICES_EU) -> str:
	if not list_items or not base_url :
		return (None)

	# db = DB.read_json_DB(path_db)

	url = base_url
	url_addon = ""
	if list_citys or list_qualitys:
		url_addon += "?"
		if list_citys:
			url_addon += "locations=" + ",".join(list_citys)
		if list_qualitys:
			url_addon += "&qualities=" + ",".join(list_qualitys)
	for item in list_items:
		if (len(url_addon) + len(url) + len(item) + 1 > MAX_URL_SIZE):
			url += url_addon
			data = request_url(url)
			print(json.dumps(data, indent=4))
			if not data:
				return (None)
			DB.write_all_requests(path_db, data)
			url = base_url
		else :
			if not url.endswith('/') :
				url += ',' + item
			else :
				url += item
	url += url_addon
	data = request_url(url)
	print(json.dumps(data, indent=4))
	if not data:
		return (None)
	DB.write_all_requests(path_db, data)
	return (path_db)
	





# input : benef min, rune use, ville achat, ville vente
# output : Profit[nom item achat, nom item revente, prix achat, rune cost, prix vente, benef, % renta]
def entrer(min:int=0, rune:bool=False, buy_city:str="Caerleon", sell_city:str="Black Market")->dict:
	all_item_IDs = DB.read_item_ids("Items/equipement.txt")
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
	DB.create_json_DB("Data-Base/stock.json", "Items/equipement.txt")
	# tkt("Data-Base/stock.json", ["T4_BAG", "T4_BAG@1", "T4_BAG@2"], ["Black Market", "Caerleon"], ["1", "2", "3", "4", "5"], URL_BASE_PRICES_EU)

