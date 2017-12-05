# Initial version created December 1st, 2017 by Austin 
from cyrptos import *
result = "void"
space = "\n"
logo = """   _____                 _         _____      _            _       _             
  / ____|               | |       / ____|    | |          | |     | |            
 | |    _   _ _ __ _ __ | |_ ___ | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 | |   | | | | '__| '_ \| __/ _ \| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |___| |_| | |  | |_) | || (_) | |___| (_| | | (__| |_| | | (_| | || (_) | |   
  \_____\__, |_|  | .__/ \__\___/ \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
         __/ |    | |                                                            
        |___/     |_|            """
def Welcome_Screen():
    print logo
    print "Welcome to Cyrpto-Calculator Version 0.1-Alpha"
    print space
    print "This simple tool allows you to check the prices for popular cyrpto currencies."
    print space
    print "In addition, we can do simple analysis to predict prices for you"
    print  space
    Home_Screen()

def Home_Screen():
    print "Please type the name of your cypto you want to check the price for"
    print space
    print "NOTICE: Internet connection is required. Prices are based on coinbase statistics"
    print space
    print "We do not have the price for every cyrpto currency. However, our talented developers are adding new ones every day"
    print space
    Search_Query()

def Search_Query():
    search = raw_input()
    print space
    # Now send to the information to the query search	        
    coinsearch.Searchdatabase(search)

def Pending_Results(coin):
    print space
    Cyrpto_Calculator(coin)

def Coin_Fail_Event():
   print "Would you like to enter a new coin?" 
   Yes_Or_No = raw_input()
   if Yes_Or_No == "Yes" or Yes_Or_No == "Y":
      print "Starting Over"
      Welcome_Screen()
   if Yes_Or_No == "No" or Yes_Or_No == "N":
      print "Thank you for using the product. Terminating the program"
   else:
      print "Can not understand that. Please enter 'Yes' or 'No' exactly as that"
      Coin_Fail_Event()

def Cyrpto_Calculator(current_coin):
    #Replace bitcoin with each different coin
    print "Welcome to the calculator for the "+current_coin+" currency!"
    print space
    print "The features that we offer are the following: Check the current price(-c), See what your price would be if it incresed by x amount(-p)"
    print space
    print "Enter those whenever you wish"
    collect_data = raw_input()
    if collect_data == "-c":
       price_check(current_coin)
    elif collect_data == "-p":
       amount_compare(current_coin)

def price_check(specific_coin):
    #Testing Purposes
    coin_apis.Coin_PriceCheck(specific_coin)
    Cyrpto_Calculator(specific_coin)

def amount_compare(specific_coin):
    print "Do you want to see how much your bitcoin would be worth if it increased by a certain amount? Just enter that number directly below and we will do the rest"
    print "NOTE: Enter a dollar amount. Example if a bitcoin cost 1 dollar say you imagine it incrasing to 1000, enter that"
    collect_coin_data = raw_input()
#Causing potential bug in the code 
#Welcome_Screen()
if __name__ == "__main__":
   Welcome_Screen()

