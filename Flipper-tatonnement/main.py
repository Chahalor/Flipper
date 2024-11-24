''' Big Header '''
# Description: TODO...
#  /=================================\
# |===========Importations============|
#  \=================================/
import requests
import time

#  /=================================\
# |===========Constantes=============|
#  \=================================/
# constantes
MAX_REQUESTS_PER_MINUTE: int = 180
MAX_REQUESTS_PER_5_MINUTE: int = 300
MAX_URL_LENGTH: int = 4096
# file path
PATH_ARTIFACT_TXT: str = "items/artifact.txt"
PATH_CONSUMABLE_TXT:str = "items/consumable.txt"
PATH_EQUIPEMENT_TXT: str = "items/equipement.txt"
PATH_ITEM_LIST_TXT: str = "items/items.txt"
PATH_ITEM_LIST_JSON: str = "items/items.json"
PATH_RESSOURCES_TXT: str = "items/ressources.txt"
# url
URL_BASE_PRICES_EU: str = "https://www.albion-online-data.com/api/v2/stats/prices/"
EXEMPLE_URL: dict = {
	# src: https://old.west.albion-online-data.com/api/swagger/index.html
	"Charts": {
		"url_charts": "https://europe.albion-online-data.com//api/v2/stats//api/v2/stats/Charts/{itemList}.{format}",
		"url_history": "https://europe.albion-online-data.com//api/v2/stats//api/v2/stats/History/{itemList}.{format}"
	},
	"Gold": {
		"url_gold": "https://europe.albion-online-data.com//api/v2/stats/Gold"	# .{format}
	},
	"Prices": {
		"url_prices": "https://europe.albion-online-data.com//api/v2/stats/prices/SUS.json"	# {itemList}.{format}
	},
	"View": {
		"url_view": "https://europe.albion-online-data.com//api/v2/stats/View/{itemList}"
	}
}

#  /=================================\
# |===========Classes================|
#  \=================================/
class Item:
	def __init__(self, id:int, name:str, display:str=None)->None:
		self.id = id
		self.name = name
		self.display = display
	def __str__(self)->str:
		return f"{self.id}: {self.name}: {self.display}"

#  /=================================\
# |===========Fonctions==============|
#  \=================================/
def	get_url(url:str)->list[dict]:
	try:
		response = requests.get(url)

		# Vérifier si la requête a réussi
		if response.status_code != 200:
			print(f"Erreur lors de la requête : {response.status_code} - {response.text}")
			return ([])
		data = response.json()  # Convertir la réponse JSON en dictionnaire Python
		return (data)
	except requests.exceptions.RequestException as e:
		print(f"Erreur réseau : {e}")
		return ([])
	
def read_item_list(path: str) -> list[Item]:
	items = []
	with open(path, "r") as file:
		for line in file:
			parts = line.strip().replace(' ', '').split(':', 3)
			if len(parts) == 3:
				item_id, item_name, display_name = parts
				item = Item(int(item_id), item_name, display_name)
				items.append(item)
	return items

def build_list_item(all_item: list[Item], base_length:int=len(URL_BASE_PRICES_EU), start: int=0) -> tuple[list[str], int]:
	length = base_length
	i = start
	result = []
	while i < len(all_item):
		item = all_item[i].name
		if (length + len(item) + 1) >= 1000:
			break
		result.append(item)
		length += len(item) + 1
		i += 1
	return (result, i)

def url_builder(base_url:str, items:list[str], locations:list[str], qualities:list[str])->str:
	url = base_url
	url += ",".join(items)
	if items:
		url += ".json"
	if locations:
		url += "?locations=" + ",".join(locations)
	if qualities:
		url += "&qualities=" + ",".join(qualities)
	return (url)

#  /=================================\
# |===========Main===================|
#  \=================================/
if __name__ == "__main__":
	all_item = read_item_list(PATH_EQUIPEMENT_TXT)
	length = len(URL_BASE_PRICES_EU) + len(".json") + len("Caerleon,Black Market")
	listed, i = build_list_item(all_item, length, 736)
	url = url_builder(URL_BASE_PRICES_EU, listed, ["Caerleon", "Black Market"], [])
	requested = get_url(url)
	for data in requested:
		# print(data)
		print(f"{data["item_id"]}: {data["sell_price_min"]} at {data["city"]} date {data["sell_price_min_date"]}")

	# i = 0
	# while i < len(all_item):
	# 	items, i = build_list_item(all_item, i)
	# 	url = url_builder(URL_BASE_PRICES_EU, items, ["Caerleon", "Black Market"], [])
	# 	print(url)
	# 	print(len(url))
		# data = get_url(url)
		# if not data:
		# 	break
		# time.sleep(5)


# nb char per name mean = 24
# nb items = 7492
# 7492 / 24 = 312.1666666666667 --> toute les 5 minutes je peut fletch tout les items du jeu (en moyenne)

'''
TODO:
File :
 - un fichier avec que les ressources
 - un fichier avec que les items (equipable/BM)
 - un fichier avec que les items (non equipable/non BM)
Functions :
 - patch build_list_item qui renvoie une list trop grande (les ',' mal géré)
 - 

'''
# https://west.albion-online-data.com/api/v2/stats/prices/T2_SHOES_CLOTH_SET1,T3_SHOES_CLOTH_SET1,T4_SHOES_CLOTH_SET1,T4_SHOES_CLOTH_SET1@1,T4_SHOES_CLOTH_SET1@2,T4_SHOES_CLOTH_SET1@3,T4_SHOES_CLOTH_SET1@4,T5_SHOES_CLOTH_SET1,T5_SHOES_CLOTH_SET1@1,T5_SHOES_CLOTH_SET1@2,T5_SHOES_CLOTH_SET1@3,T5_SHOES_CLOTH_SET1@4,T6_SHOES_CLOTH_SET1,T6_SHOES_CLOTH_SET1@1,T6_SHOES_CLOTH_SET1@2,T6_SHOES_CLOTH_SET1@3,T6_SHOES_CLOTH_SET1@4,T7_SHOES_CLOTH_SET1,T7_SHOES_CLOTH_SET1@1,T7_SHOES_CLOTH_SET1@2,T7_SHOES_CLOTH_SET1@3,T7_SHOES_CLOTH_SET1@4,T8_SHOES_CLOTH_SET1,T8_SHOES_CLOTH_SET1@1,T8_SHOES_CLOTH_SET1@2,T8_SHOES_CLOTH_SET1@3,T8_SHOES_CLOTH_SET1@4,T4_SHOES_CLOTH_SET2,T4_SHOES_CLOTH_SET2@1,T4_SHOES_CLOTH_SET2@2,T4_SHOES_CLOTH_SET2@3,T4_SHOES_CLOTH_SET2@4,T5_SHOES_CLOTH_SET2,T5_SHOES_CLOTH_SET2@1,T5_SHOES_CLOTH_SET2@2,T5_SHOES_CLOTH_SET2@3,T5_SHOES_CLOTH_SET2@4,T6_SHOES_CLOTH_SET2,T6_SHOES_CLOTH_SET2@1,T6_SHOES_CLOTH_SET2@2,T6_SHOES_CLOTH_SET2@3,T6_SHOES_CLOTH_SET2@4,T7_SHOES_CLOTH_SET2,T7_SHOES_CLOTH_SET2@1,T7_SHOES_CLOTH_SET2@2,T7_SHOES_CLOTH_SET2@3,T7_SHOES_CLOTH_SET2@4,T8_SHOES_CLOTH_SET2,T8_SHOES_CLOTH_SET2@1,T8_SHOES_CLOTH_SET2@2,T8_SHOES_CLOTH_SET2@3,T8_SHOES_CLOTH_SET2@4,T4_SHOES_CLOTH_SET3,T4_SHOES_CLOTH_SET3@1,T4_SHOES_CLOTH_SET3@2,T4_SHOES_CLOTH_SET3@3,T4_SHOES_CLOTH_SET3@4,T5_SHOES_CLOTH_SET3,T5_SHOES_CLOTH_SET3@1,T5_SHOES_CLOTH_SET3@2,T5_SHOES_CLOTH_SET3@3,T5_SHOES_CLOTH_SET3@4,T6_SHOES_CLOTH_SET3,T6_SHOES_CLOTH_SET3@1,T6_SHOES_CLOTH_SET3@2,T6_SHOES_CLOTH_SET3@3,T6_SHOES_CLOTH_SET3@4,T7_SHOES_CLOTH_SET3,T7_SHOES_CLOTH_SET3@1,T7_SHOES_CLOTH_SET3@2,T7_SHOES_CLOTH_SET3@3,T7_SHOES_CLOTH_SET3@4,T8_SHOES_CLOTH_SET3,T8_SHOES_CLOTH_SET3@1,T8_SHOES_CLOTH_SET3@2,T8_SHOES_CLOTH_SET3@3,T8_SHOES_CLOTH_SET3@4,T4_SHOES_CLOTH_KEEPER,T4_SHOES_CLOTH_KEEPER@1,T4_SHOES_CLOTH_KEEPER@2,T4_SHOES_CLOTH_KEEPER@3,T4_SHOES_CLOTH_KEEPER@4,T5_SHOES_CLOTH_KEEPER,T5_SHOES_CLOTH_KEEPER@1,T5_SHOES_CLOTH_KEEPER@2,T5_SHOES_CLOTH_KEEPER@3,T5_SHOES_CLOTH_KEEPER@4,T6_SHOES_CLOTH_KEEPER,T6_SHOES_CLOTH_KEEPER@1,T6_SHOES_CLOTH_KEEPER@2,T6_SHOES_CLOTH_KEEPER@3,T6_SHOES_CLOTH_KEEPER@4,T7_SHOES_CLOTH_KEEPER,T7_SHOES_CLOTH_KEEPER@1,T7_SHOES_CLOTH_KEEPER@2,T7_SHOES_CLOTH_KEEPER@3,T7_SHOES_CLOTH_KEEPER@4,T8_SHOES_CLOTH_KEEPER,T8_SHOES_CLOTH_KEEPER@1,T8_SHOES_CLOTH_KEEPER@2,T8_SHOES_CLOTH_KEEPER@3,T8_SHOES_CLOTH_KEEPER@4,T4_SHOES_CLOTH_HELL,T4_SHOES_CLOTH_HELL@1,T4_SHOES_CLOTH_HELL@2,T4_SHOES_CLOTH_HELL@3,T4_SHOES_CLOTH_HELL@4,T5_SHOES_CLOTH_HELL,T5_SHOES_CLOTH_HELL@1,T5_SHOES_CLOTH_HELL@2,T5_SHOES_CLOTH_HELL@3,T5_SHOES_CLOTH_HELL@4,T6_SHOES_CLOTH_HELL,T6_SHOES_CLOTH_HELL@1,T6_SHOES_CLOTH_HELL@2,T6_SHOES_CLOTH_HELL@3,T6_SHOES_CLOTH_HELL@4,T7_SHOES_CLOTH_HELL,T7_SHOES_CLOTH_HELL@1,T7_SHOES_CLOTH_HELL@2?locations=4,7,8,301,1002,1006,1012,1301,2002,2004,2301,3002,3003,3005,3008,3301,4002,4006,4300,4301,5003&qualities=1,2,3,4,5