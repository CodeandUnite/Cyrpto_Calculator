# Processor.py acts as the middleman between the view and the models. 
# Its key duties is retriveing the user data and asking the appropriate model for the data 
# It's secondary duty is to validate the data that the user submits and correct them before sending on the data
import sys
sys.path.append('../')
#from model import bitcoin
#from view import core



def verify_cyrptos(user_coin,boolean_verifer):
   #from view import core
   current_coins = ['bitcoin','litecoin','etherium']
   if user_coin in current_coins:
      boolean_is_true = True
      coin_approved = user_coin
      # Sending back the values
      return (coin_approved, boolean_is_true)
   else:
      return (user_coin, boolean_verifer)


def Start_Price_Retrivel(required_data_tuple):
   from model import bitcoin,etherium,litecoin
   current_coins = ["bitcoin", "litecoin", "etherium"]
   coin_id, currency_value = required_data_tuple
   if coin_id == "bitcoin":
   	return bitcoin.api_price_retrivel(coin_id, currency_value)
   elif coin_id == "litecoin":
   	return litecoin.api_price_retrivel(coin_id, currency_value)
   elif coin_id == "etherium":
   	return etherium.api_price_retrivel(coin_id, currency_value)
#Upon a successful true statement def retrive_price(Get_Data):

def Price_retrivel_other_processes(coin):
	from model import bitcoin, etherium, litecoin
	currency_not_needed_void = "void"
	if coin == "bitcoin":
	   return bitcoin.api_price_retrivel(coin, currency_not_needed_void)

def Collect_Calculator_Data(Selected_Coin, the_calculator_module, the_calculator_amount):
	from model import calculator
	Get_Current_Currency = Price_retrivel_other_processes(Selected_Coin)
	if the_calculator_module == "-v":
		return calculator.calculate_v_mode(Get_Current_Currency, the_calculator_amount)
    

