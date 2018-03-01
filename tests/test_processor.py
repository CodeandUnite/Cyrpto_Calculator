''' This test will attempt to validate that the code that was entered is accurate  '''
def handle_cyrpto_price_check(cyrpto_coin, fiat_currency):
    from model import bitcoin,litecoin,etherium calculator
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

def test_handle_cyrpto_price_check():
    
