# Processor.py acts as the middleman between the view and the models.
# Its key duties is retriveing the user data and asking the appropriate model for the data
# It's secondary duty is to validate the data that the user submits and correct them before sending on the data
import sys
sys.path.append('../')
#from model import bitcoin
#from view import core




def verify_cyrptos(cyrpto_currency, GDP_currency, boolean_trueORfalse):
    """ Retrives the data from the view. beautifys it and sends it to the helper
    for proper vertification. """
    Acceptable_current_coins = ['bitcoin', 'litecoin', 'etherium']
    acceptable_fiat_currencies = ['usd', 'eur', 'rur','gbp']

    if cyrpto_currency in Acceptable_current_coins:
       if GDP_currency in acceptable_fiat_currencies:
          Passedverification = True
          return (cyrpto_currency, GDP_currency, Passedverification)
    else:
       cyrpto_fail = "Null"
       gdp_fail = "Null"
       Failedvertification = False
       return (cyrpto_fail, gdp_fail, Failedvertification)

def verify_cyrptos_helper():
    """This acts as the helper function for the main verify_cyrptos. It will
    check the database for the correct cyrptocoins and gdp currencies.
    upon satisfactory or unsatisfactory work it will return it to
    verify_cyrptos for processing  """




def Start_Price_Retrivel(required_data_tuple):
    from model import bitcoin, etherium, litecoin
    cyrpto_name, gdp_name, command, command_number = required_data_tuple
    current_coins = ['bitcoin','etherium','litecoin']
    if cyrpto_name == "bitcoin":
       return bitcoin.api_price_retrivel(cyrpto_name, gdp_name)
    if cyrpto_name == "litecoin":
       return litecoin.api_price_retrivel(cyrpto_name, gdp_name)
    if cyrpto_name == "etherium":
        return etherium.api_price_retrivel(cyrpto_name, gdp_name)


# Need to get the currency here too
def Price_retrivel_other_processes(standard_data_tuple):
    from model import bitcoin, etherium, litecoin
    coin, fiat_currency, command, command_number = standard_data_tuple
    if coin == "bitcoin":
        return bitcoin.api_price_retrivel(coin, fiat_currency)
    if coin == "etherium":
        return etherium.api_price_retrivel(coin, fiat_currency)
    if coin == "litecoin":
        return litecoin.api_price_retrivel(coin, fiat_currency)

def price_calculator_functions(data_tuple):
    from model import calculator
    coin, fiat_currency, command, command_number = data_tuple
    # Determine which command to user
    if command == "-check":
       return "do something important"
    if command == "-rise":
       return calculator.calculate_inc_mode(data_tuple)
    if command == "-fall":
       return calculator.calculate_dec_mode(data_tuple)
    else:
       error_message = "Something went wrong"
       return error_message




def Collect_Calculator_Data(data_tuple):
    from model import calculator
    Get_Current_Currency = Price_retrivel_other_processes(Selected_Coin)
    if the_calculator_module == "-v":
        return calculator.calculate_v_mode
    if the_calculator_module == "-inc":
        return calculator.calculate_inc_mode(data_tuple, Get_Current_Currency)
    if the_calculator_module == "-dec":
        return calculator.calculate_dec_mode(Get_Current_Currency, the_calculator_amount)
