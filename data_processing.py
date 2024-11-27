'''
Big Header
'''

# Description: TODO...

#  /=================================\
# |===========Importations============|
#  \=================================/

#  /=================================\
# |=========Global Variables==========|
#  \=================================/
# TODO: verify the taxes values
TAX = 0.06
SELL_ORDER_TAX = 0.025
TAX_BUY_ORDER = 1 # TODO: find the real value
TAX_QUICK_BUY = 1 # TODO: find the real value

#  /=================================\
# |============Classes================|
#  \=================================/

class Profits:
	def __init__(self, item_id:str, item_name:str, buy_price:int, buy_date:str, sell_price:int, sell_date:str):
		self.item_id = item_id
		self.item_name = item_name
		self.buy_price = buy_price
		self.buy_date = buy_date
		self.sell_price = sell_price
		self.sell_date = sell_date
		self.profits = (self.sell_price - self.buy_price) * TAX
		self.percent_rent = (self.profits / self.buy_price) * 100	# a mon avis c'est faux car pas de tax

	def __str__(self):
		return (f"Item: {self.item_name}, Buy Price: {self.buy_price}, Sell Price: {self.sell_price}, Profit: {self.profit}, Rentability: {self.rentability}, % Rentability: {self.percent_rent}")

#  /=================================\
# |============Functions==============|
#  \=================================/

def get_profits(data, min:int, rune:bool, buy_city:str, sell_city:str, list_items:list[str])->list[Profits]:
	result = list()
	if not rune :
		for item_id in dir(data.__getattribute__(buy_city.replace(' ', '_'))) :
			if (item_id.startswith("__")):
				continue
			for i in range(1, 6) :
				qlty = data.__getattribute__(buy_city.replace(' ', '_')).__getattribute__(item_id).__getattribute__(f"q{i}")
				if
	else:
		return (None) # TODO: implement the rune calculation
	return (result)
