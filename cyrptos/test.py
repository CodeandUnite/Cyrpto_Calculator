
import requests
#import urllib.request
import ast
import json
import yaml
specific_coin = "litecoin"


if specific_coin == "litecoin":
   litecoin_url = 'https://api.coinmarketcap.com/v1/ticker/litecoin'
   r = requests.get(litecoin_url, headers = {'Accept':'application/json'})
   Last_LitecoinPrice = r.json()
   json_data = yaml.load(json.dumps(Last_LitecoinPrice))
   print json_data['price_usd']

  
# print Last_LitecoinPrice


#Bitcoin_PriceCheck()
#https://api.coinbase.com/v2/prices/BTC-USD/spot.



