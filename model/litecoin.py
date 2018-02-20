# This contains all the information needed for someone who selects bitcoin
import requests
import json
import sys
#from view import core
sys.path.append('../')
import view
import controller


def api_price_retrivel(coin, conversion_currency):
    coin = "ltc"
    url = "https://api.cryptonator.com/api/ticker/{}-{}".format(
        coin, conversion_currency)
    request = requests.get(url)
    data = request.json()
    litecoin_price = float(data['ticker']['price'])
    return litecoin_price
