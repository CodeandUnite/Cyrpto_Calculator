
"""
This Module gives quick and easy access to current
cryptocurrency prices for any coin
"""

import requests




def get_price(coin, base_currency):
    """Returns current price of given coin in the respective currency"""
    url = "https://api.cryptonator.com/api/ticker/{}-{}".format(
            coin, base_currency)
    request = requests.get(url)
    data = request.json()

    return data['ticker']['price']

print "Hi"
print get_price("ltc","usd")
