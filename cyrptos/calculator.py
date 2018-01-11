# THis file will work as a calculator for the program
import requests
import time


def Get_Recent_Price(specific_coin, user_math):
    if specific_coin == "bitcoin":
        coin = "btc"
        base_currency = "usd"
        url = "https://api.cryptonator.com/api/ticker/{}-{}".format(
            coin, base_currency)
        request = requests.get(url)
        data = request.json()
        Latest_Bitcoinprice = float(data['ticker']['price'])
        # Send to the real calculator to calculate the price
        return Calculate_Future(Latest_Bitcoinprice, user_math)
    elif specific_coin == "etherium":
        coin = "eth"
        base_currency = "usd"
        url = "https://api.cryptonator.com/api/ticker/{}-{}".format(
            coin, base_currency)
        request = requests.get(url)
        data = request.json()
        Latest_EtheriumPrice = float(data['ticker']['price'])
        return Calculate_Future(Latest_EtheriumPrice, user_math)
    elif specific_coin == "litecoin":
        coin = "ltc"
        base_currency = "usd"
        url = "https://api.cryptonator.com/api/ticker/{}-{}".format(
            coin, base_currency)
        request = requests.get(url)
        data = request.json()
        Latest_LitecoinPrice = float(data['ticker']['price'])
        return Calculate_Future(Latest_LitecoinPrice, user_math)


def Calculate_Future(Last_Price, user_math):
    new_price = Last_Price * user_math
    return new_price
