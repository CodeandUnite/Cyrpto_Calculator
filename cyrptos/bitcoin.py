#Created on December 2nd, 2017 originally by Austin

#GOAL: Get API information for current data on Bitcoin and then this will allow us to send this data to the main.py file.

import requests 


#bitcoin_url = 'https://www.bitstamp.net/api/ticker'
#r = requests.get(bitcoin_url, headers = {'Accept':'application/json'})
#print r.json()['last']
#Last_BitcoinPrice = r.json()['last']

def Bitcoin_PriceCheck():
   print "Oh Hi"
   bitcoin_url = 'https://www.bitstamp.net/api/ticker'
   r = requests.get(bitcoin_url, headers = {'Accept':'application/json'})
   Last_BitcoinPrice = r.json()['last']
   print  "The current price of Bitcoin withihn the last 24 hours is " + Last_BitcoinPrice

#Bitcoin_PriceCheck()
