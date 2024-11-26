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

# City.Item.qlty.<attr>
# BW.T4_BAG.3.price_min

class Quality:
	def __init__(self, qlty:int, item_id:str, quality:int, sell_price_min:int, sell_price_min_date:str, sell_price_max:int, 
			  sell_price_max_date:str, buy_price_min:int, buy_price_min_date:str, buy_price_max:int, 
			  buy_price_max_date:str):
		self.qlty = qlty
		self.item_id = item_id
		self.quality = quality
		self.sell_price_min = sell_price_min
		self.sell_price_min_date = sell_price_min_date
		self.sell_price_max = sell_price_max
		self.sell_price_max_date = sell_price_max_date
		self.buy_price_min = buy_price_min
		self.buy_price_min_date = buy_price_min_date
		self.buy_price_max = buy_price_max
		self.buy_price_max_date = buy_price_max_date
	
	def __str__(self):
		return f"Item: {self.item_id}, Quality: {self.quality}, Sell Price Min: {self.sell_price_min}, Sell Price Max: {self.sell_price_max}, Buy Price Min: {self.buy_price_min}, Buy Price Max: {self.buy_price_max}"

class Item:
	def __init__(self):
		self.item_id = None
		self.q0 = None
		self.q1 = None
		self.q2 = None
		self.q3 = None
		self.q4 = None
		self.q5 = None

	def __str__(self):
		return (f"Item_id: {self.item_id}, Q0: {self.q0}, Q1: {self.q1}, Q2: {self.q2}, Q3: {self.q3}, Q4: {self.q4}, Q5: {self.q5}")

	def add_quality(self, quality:Quality):
		setattr(self, quality.quality, quality)

class City:
	def __init__(self, name:str):
		self.name:str = name

	def __str__(self):
		return (f"City: {self.name}")

	def add_item(self, item:Item):
		setattr(self, item.item_id, item)

class Root:
	def __init__(self, citys:list[str]) -> None:
		for city in citys:
			setattr(self, city.replace(' ', '_'), City(city))

	def __str__(self) -> str:
		result = str()
		for city in dir(self):
			if not city.startswith('__'):
				result += f"{city}: {getattr(self, city, "attr not found")}\n"
		return (result)
	
	def reset_city(self, city:str) -> None:
		setattr(self, city, City(city))

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


def get_items_data(list_items: list[str], citys:list[str], root:Root)->Root:
	url = URL_BASE_PRICES_EU
	url += ",".join(list_items)
	if citys:
		url += f"?locations={','.join(citys)}"
	
	data = request_url(url)

	for item in data:
		city:City = getattr(root, item['city'].replace(' ', '_'))	# root.LY
		item_class = setattr(city, item['item_id'], Item())						# root.LY.T4_BAG
		qlty = setattr(item_class, 'q' + str(item["quality"]), Quality(item['city'], 
																 item['item_id'], 
																 item["quality"], 
																 item["sell_price_min"], 
																 item["sell_price_min_date"], 
																 item["sell_price_max"], 
																 item["sell_price_max_date"], 
																 item["buy_price_min"], 
																 item["buy_price_min_date"], 
																 item["buy_price_max"], 
																 item["buy_price_max_date"]))
	return (root)


