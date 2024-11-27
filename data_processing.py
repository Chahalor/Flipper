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
		for item in list_items :
			for qlty in range(0, 6) :
				buy_price = data.__getattribute__(buy_city).__getattribute__(item).__getattribute__(f"q{qlty}").sell_price_min
				sell_price = data.__getattribute__(sell_city).__getattribute__(item).__getattribute__(f"q{qlty}").buy_price_max
			if (sell_price - buy_price) * TAX > min:
				result.append(Profits(item, item, buy_price, 
									  data.__getattribute__(buy_city).__getattribute__(item).sell_price_min_date, 
									  sell_price, data.__getattribute__(sell_city).__getattribute__(item).buy_price_max_date))
	else:
		return (None) # TODO: implement the rune calculation
	return (result)
