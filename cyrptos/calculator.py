# THis file will work as a calculator for the program
import requests
import time
test_coin = "bitcoin"

#Get_Recent_Price(test_coin)

def Get_Recent_Price(specific_coin,user_math):
   if specific_coin == "bitcoin":
      bitcoin_url = 'https://www.bitstamp.net/api/ticker'
      r = requests.get(bitcoin_url, headers = {'Accept':'application/json'})
      Last_BitcoinPrice = r.json()['last']
      print "Calculating..."
      print time.sleep(2)
      print "If the price was to raise by your estimation it would be approximately" 
      print Calculate_Future(Last_BitcoinPrice, user_math)
     # print "If " + specific_coin +" s price were to raise by "+user_math+" it would be approximately " + Calculate_Future(Last_BitcoinPrice,user_math)

def Calculate_Future(Last_BitcoinPrice,user_math):
   recent_price =  float(Last_BitcoinPrice)
   new_price = recent_price * 10
   return new_price


