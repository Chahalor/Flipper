import json

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
					raw[city][item_id][quality]["sell_price_max"] = 0
					raw[city][item_id][quality]["sell_price_avg"] = 0
					raw[city][item_id][quality]["buy_price_min"] = 0
					raw[city][item_id][quality]["buy_price_max"] = 0
					raw[city][item_id][quality]["buy_price_avg"] = 0

	with open(path_json, 'w') as stock :
		stock.write(json.dumps(raw, indent=4))
	return (path_json)

def read_json_DB(path:str) -> dict:
	with open(path, 'r') as stock:
		return (json.load(stock))



if __name__ == '__main__':
	# create_json_DB("Data-Base/stock.json", "Items/equipement.txt")
	print(read_json_DB("Data-Base/stock.json"))