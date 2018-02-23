from decimal import *

#Workaround for bug
def price_retrivel(dataTuple):
    cyrpto, fiat = dataTuple

    #Will need to change base_currency to custom price
    #base_currency = "usd"
    url = "https://api.cryptonator.com/api/ticker/{}-{}".format(
        cyrpto, fiat)
    request = requests.get(url)
    data = request.json()
    bitcoin_price = float(data['ticker']['price'])
    return bitcoin_price


def calculate_inc_mode(dataTuple):
    from model import bitcoin
    cyrpto, fiat, percentage_increase, price = dataTuple
    cyrpto_price = float(price)
    current_price = float(percentage_increase)
    projectedIncrease = cyrpto_price * current_price
    AddToTotal = current_price + projectedIncrease
    return AddToTotal


def calculate_dec_mode(dataTuple):
    from model import bitcoin
    cyrpto, fiat, percentage_increase, price = dataTuple
    cyrpto_price = float(price)
    current_price = float(percentage_increase)

    Projected_decrease = cyrpto_price * current_price
    Decrease_From_Total = current_price - Projected_decrease
    return Decrease_From_Total
