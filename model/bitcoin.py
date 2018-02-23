import requests
import json
import sys
#from view import core
sys.path.append('../')
import view
import controller


def api_price_retrivel(dataTuple):
    cyrpto, fiat = dataTuple
    coin = "btc"
    #Will need to change base_currency to custom price
    #base_currency = "usd"
    url = "https://api.cryptonator.com/api/ticker/{}-{}".format(
        cyrpto, fiat)
    request = requests.get(url)
    data = request.json()
    bitcoin_price = float(data['ticker']['price'])
    return bitcoin_price
