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
# ...

#  /=================================\
# |============Functions==============|
#  \=================================/

# def no_enchant_getter(market_1:Item, market_2:Item, ressources:list[Item])->int:
# 	'''
# 	@brief: TODO
# 	@param item: Item
# 	@return: int
# 	'''
# 	if (market_1.sell_price_min - market_2.buy_price_max) * TAX > min:
# 		return ((market_1.sell_price_min - market_2.buy_price_max) * TAX)
# 	return (0)

# def enchant_getter(market_1:Item, market_2:Item, min:int, ressources:list[Item])->int:
# 	'''
# 	@brief: TODO
# 	@param item: Item
# 	@return: int
# 	'''
# 	# TODO:
# 	# - comparer (prix d'achat + prix rune * nb rune) et de vente
# 	# - touver un moyen de savoir combien de rune par item (db a moi ?)
# 	pass

# # les donnees qui rentre dans cette fonction doivent contenir les prix des items en .0 a .3 pour toutes 
# # les qualiters dans le market 1 et le market 2
# # donc len(data_m1) == len(data_m2)
# #  - exemple: data_m1[0] == T4_BAG quality 3 et data_m2[0] == T4_BAG quality 3
# def get_opportunity(data_m1:list[Item], data_m2:list[Item], min:int, enchantement:bool, ressources:list[Item])->list[Item]:
# 	'''
# 	@brief Get the best opportunity of the data
# 	@param data: list of items
# 	@return list of items
# 	'''
# 	if (len(data_m1) != len(data_m2)):
# 		return (list())
# 	opportinity: list = []
# 	value: int = 0
# 	for item_m1, item_m2 in zip(data_m1, data_m2):
# 		if enchantement :
# 			value = enchant_getter(item_m1, item_m2, ressources)
# 			if value * TAX > min:
# 				opportinity.append(item_m1)
# 		else:
# 			if (item_m2.sell_price_min * TAX_QUICK_BUY - item_m1.buy_price_max) * TAX > min:
# 				opportinity.append(item_m1)
# 	return (opportinity)

