import json
from datetime import datetime

def read_item_ids(file: str) -> list[str]:
	with open(file, 'r') as f:
		data = f.read().splitlines()
		result = []
		for line in data:
			result.append(line.split(':')[1].strip())
	return (result)

def	create_json_DB(path_json:str, path_items:str) -> str:
	items_ids = read_item_ids(path_items)
	list_city = ["Black Market", "Caerleon"]
	list_quality = ["1", "2", "3", "4", "5"]
	raw = dict()
	for city in list_city:
		raw[city] = dict()
		for item_id in items_ids:
				raw[city][item_id] = dict()
				for quality in list_quality:
					raw[city][item_id][quality] = dict()
					raw[city][item_id][quality]["quality"] = quality
					raw[city][item_id][quality]["item_id"] = item_id
					raw[city][item_id][quality]["city"] = city
					raw[city][item_id][quality]["sell_price_min"] = 0
					raw[city][item_id][quality]["sell_price_min_date"] = ""
					raw[city][item_id][quality]["sell_price_max"] = 0
					raw[city][item_id][quality]["sell_price_max_date"] = ""
					raw[city][item_id][quality]["buy_price_min"] = 0
					raw[city][item_id][quality]["buy_price_min_date"] = ""
					raw[city][item_id][quality]["buy_price_max"] = 0
					raw[city][item_id][quality]["buy_price_max_date"] = ""

	with open(path_json, 'w') as stock :
		stock.write(json.dumps(raw, indent=4))
	return (path_json)

def read_json_DB(path:str) -> dict:
	with open(path, 'r') as stock:
		return (json.load(stock))

# CITY.ITEM.QUALITY.{INFO}
def	update_item_in_DB(path:str, item:dict, db:dict=None) -> str:
	if not db:
		db = read_json_DB(path)

	item_time_sell_min = datetime.fromisoformat(item["sell_price_min_date"])
	item_time_sell_max = datetime.fromisoformat(item["sell_price_max_date"])
	item_time_buy_min = datetime.fromisoformat(item["buy_price_min_date"])
	item_time_buy_max = datetime.fromisoformat(item["buy_price_max_date"])
	if (item_time_sell_min < datetime.fromisoformat(db[item["city"]][item["item_id"]][str(item["quality"])]["sell_price_min_date"])): 
		db[item["city"]][item["item_id"]][str(item["quality"])]["sell_price_min"] = item["sell_price_min"]
		db[item["city"]][item["item_id"]][str(item["quality"])]["sell_price_min_date"] = item["sell_price_min_date"]
	if (item_time_sell_max < datetime.fromisoformat(db[item["city"]][item["item_id"]][str(item["quality"])]["sell_price_max_date"])):
		db[item["city"]][item["item_id"]][str(item["quality"])]["sell_price_max"] = item["sell_price_max"]
		db[item["city"]][item["item_id"]][str(item["quality"])]["sell_price_max_date"] = item["sell_price_max_date"]
	if (item_time_buy_min < datetime.fromisoformat(db[item["city"]][item["item_id"]][str(item["quality"])]["buy_price_min_date"])):
		db[item["city"]][item["item_id"]][str(item["quality"])]["buy_price_min"] = item["buy_price_min"]
		db[item["city"]][item["item_id"]][str(item["quality"])]["buy_price_min_date"] = item["buy_price_min_date"]
	if (item_time_buy_max < datetime.fromisoformat(db[item["city"]][item["item_id"]][str(item["quality"])]["buy_price_max_date"])):
		db[item["city"]][item["item_id"]][str(item["quality"])]["buy_price_max"] = item["buy_price_max"]
		db[item["city"]][item["item_id"]][str(item["quality"])]["buy_price_max_date"] = item["buy_price_max_date"]

	with open(path, 'w') as stock:
		stock.write(json.dumps(db, indent=4))
	
	return (db[item["city"]][item["item_id"]][str(item["quality"])])

def write_all_requests(path:str, data:list[dict]) -> str:
	db = read_json_DB(path)

	for item in data:
		update_item_in_DB(path, item, db)


	return (path)

if __name__ == '__main__':
	# create_json_DB("Data-Base/stock.json", "Items/equipement.txt")
	# print(read_json_DB("Data-Base/stock.json"))
	data = {'item_id': 'T4_BAG@1', 
		 'city': 'Black Market', 
		 'quality': 1, 
		 'sell_price_min': 5424, 
		 'sell_price_min_date': '2024-11-28T06:50:00', 
		 'sell_price_max': 5479, 
		 'sell_price_max_date': '2024-11-28T06:50:00', 
		 'buy_price_min': 4745, 
		 'buy_price_min_date': '2024-11-28T06:40:00', 
		 'buy_price_max': 5110, 
		 'buy_price_max_date': '2024-11-28T06:40:00'}
	update_item_in_DB("Data-Base/stock.json", data)
