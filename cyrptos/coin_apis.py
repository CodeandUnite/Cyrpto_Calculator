# Created on December 2nd, 2017 originally by Austin

# GOAL: Get API information for current data on Bitcoin and then this will allow us to send this data to the main.py file.

import requests
import json


def Coin_PriceCheck(specific_coin):

    if specific_coin == "bitcoin":
        coin = "btc"
        base_currency = "usd"
        url = "https://api.cryptonator.com/api/ticker/{}-{}".format(
            coin, base_currency)
        request = requests.get(url)
        data = request.json()
        print "The current price for Bitcoin is " + data['ticker']['price']
        bitcoin_price = float(data['ticker']['price'])
        print bitcoin_price

    elif specific_coin == "etherium":
        coin = "eth"
        base_currency = "usd"
        url = "https://api.cryptonator.com/api/ticker/{}-{}".format(
            coin, base_currency)
        request = requests.get(url)
        data = request.json()
        print "The current price for Etherium is " + data['ticker']['price']
    elif specific_coin == "litecoin":
        coin = "ltc"
        base_currency = "usd"
        url = "https://api.cryptonator.com/api/ticker/{}-{}".format(
            coin, base_currency)
        request = requests.get(url)
        data = request.json()
        print "The current price for Litecoin is " + data['ticker']['price']


# Bitcoin_PriceCheck()
