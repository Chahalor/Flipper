'''
Big Header
'''

# Description: TODO...

#  /=================================\
# |===========Importations============|
#  \=================================/

import requests
from json import load

#  /=================================\
# |=========Global Variables==========|
#  \=================================/

MAX_REQUESTS_PER_MINUTE = 180
MAX_REQUESTS_PER_5_MINUTES = 300
URL_BASE_PRICES_EU = "https://www.albion-online-data.com/api/v2/stats/prices/"
LIST_RUNE = [
	"T4_RUNE", "T4_SOUL", "T4_RELIC", "T4_SHARD_AVALONIAN", "T4_SHARD_CRYSTAL",
	"T5_ESSENCE_POTION", "T5_ESSENCE", "T5_RUNE", "T5_SOUL", "T5_RELIC", "T5_SHARD_AVALONIAN", "T5_SHARD_CRYSTAL",
	"T6_ESSENCE_POTION", "T6_ESSENCE", "T6_RUNE", "T6_SOUL", "T6_RELIC", "T6_SHARD_AVALONIAN", "T6_SHARD_CRYSTAL",
	"T7_ESSENCE_POTION", "T7_ESSENCE", "T7_RUNE", "T7_SOUL", "T7_RELIC", "T7_SHARD_AVALONIAN", "T7_SHARD_CRYSTAL",
	"T8_ESSENCE_POTION", "T8_ESSENCE", "T8_RUNE", "T8_SOUL", "T8_RELIC", "T8_SHARD_AVALONIAN", "T8_SHARD_CRYSTAL"
]


#  /=================================\
# |============Classes================|
#  \=================================/

# ...

#  /=================================\
# |============Functions==============|
#  \=================================/


def request_url(url:str)->list[dict]:
	try:
		response = requests.get(url)

		if response.status_code != 200:
			print(f"Error: {response.status_code}")
		return response.json()
	except requests.exceptions.RequestException as e:
		print(f"Error: {e}")
	return {}


def get_items_data(list_items: list[str], citys:list[str], stock:dict)->dict:
	url = URL_BASE_PRICES_EU
	url += ",".join(list_items)
	stock = {
			# "Black Market": {}, 
			# "Briddgewatch": {}, 
			# "Caerleon": {}, 
			# "Fort Sterling": {}, 
			# "Lymhurst": {}, 
			# "Martlock": {}, 
			# "Thetford": {}
			}
	if len(citys) != 0:
		url += "?locations=" + ",".join(citys)
	all_data = request_url(url)
	# print(url)
	for data in all_data:
		stock.setdefault(data['city'], {})
		stock[data['city']].setdefault(data['item_id'], {})
		stock[data['city']][data['item_id']].setdefault(data['quality'], {})
		
		stock[data['city']][data['item_id']][data['quality']] = {
			'sell_price_min': data['sell_price_min'],
			'sell_price_min_date': data['sell_price_min_date'],
			'sell_price_max': data['sell_price_max'],
			'sell_price_max_date': data['sell_price_max_date'],
			'buy_price_min': data['buy_price_min'],
			'buy_price_min_date': data['buy_price_min_date'],
			'buy_price_max': data['buy_price_max'],
			'buy_price_max_date': data['buy_price_max_date']
		}
	return (stock)


