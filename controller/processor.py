'''
The processor will essentially get the data from the view. It will then use
this data to send to the designated model to get its data. Once this data is
retrived it will send it back to the view
'''


def handle_cyrpto_and_fiat_database_check(dataTuple):
    '''As the name suggest this will check that the cyrpto currency along with the
    user defined fiat currency will be checked that it is in the database.
    If the fiat currency along with the cyrpto currency are in the database then
     '''
    usrdefinedCyrpto, userdefinedFiat = dataTuple

    complete_list_of_cyrptos = ["btc","ltc","eth"]
    complete_list_of_fiats = ["usd", "rur", "gbp"]
    if usrdefinedCyrpto in complete_list_of_cyrptos:
        if userdefinedFiat in complete_list_of_fiats:
            AcceptedVaribles = True
            return AcceptedVaribles
    if usrdefinedCyrpto not in complete_list_of_cyrptos:
        if userdefinedFiat not in complete_list_of_fiats:
            AcceptedVaribles = False
            return AcceptedVaribles




def handle_cyrpto_price_check(dataTuple):
    from model import bitcoin,litecoin,etherium,calculator
    '''Call the model according to the cyrptoCurrency
       Let the model retrive the price from the api
       Send that data back to the view

       Needs two things:
       Cyrptocurrency
       fiat currency  '''
    cyrpto_coin, fiat_currency = dataTuple
    if cyrpto_coin == "btc":
        print "Retriving your price....."
        collected_price = bitcoin.api_price_retrivel(dataTuple)
        return collected_price
    if cyrpto_coin == "ltc":
        print "Retriving your price....."
        collected_price = litecoin.api_price_retrivel(dataTuple)
        return collected_price
    if cyrpto_coin == "eth":
        print "Retriving your price....."
        collected_price = etherium.api_price_retrivel(dataTuple)
        return collected_price

def handle_cyrpto_rise_calc(dataTuple):
    from model import calculator
    '''Call the model according to the cyrptocurrency '''

    cyrpto, fiat, percentage_to_increase, price = dataTuple

    CalcFunctionsTuple = (cyrpto, fiat,percentage_to_increase,price)
    return calculator.calculate_inc_mode(CalcFunctionsTuple)



def handle_cyrpto_fall_calc(dataTuple):
    from model import calculator
    cyrpto, fiat, percentage_to_increase, price = dataTuple
    CalcFunctionsTuple = (cyrpto, fiat,percentage_to_increase,price)

    return calculator.calculate_dec_mode(CalcFunctionsTuple)
