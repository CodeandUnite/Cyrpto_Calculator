# Initial version created December 1st, 2017 by Austin
from cyrptos import *
import time
result = "void"

'''
MIT License

Copyright (c) 2017 CodeandUnite

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

space = "\n"
logo = """   _____                 _         _____      _            _       _
  / ____|               | |       / ____|    | |          | |     | |
 | |    _   _ _ __ _ __ | |_ ___ | |     __ _| | ___ _   _| | __ _| |_ ___  _ __
 | |   | | | | '__| '_ \| __/ _ \| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |___| |_| | |  | |_) | || (_) | |___| (_| | | (__| |_| | | (_| | || (_) | |
  \_____\__, |_|  | .__/ \__\___/ \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|
         __/ |    | |
        |___/     |_|

                   """
def Welcome_Screen():
    print logo
    print "Welcome to Cyrpto-Calculator!"
    space
    print "What we do: We are a simple tool that allows you to check the prices for cyrpto currencies and do simple analysis to predict prices for you"

    Home_Screen()


def Home_Screen():
    space
    print "Quick Commands: -h for help and/or to report a bug"
    print "Currently avalible currencies are Bitcoin, Etherium, and Litecoin. Please enter any of the three mentioned below"

    print space

    Search_Query()


def Help():
    print """Hello! Thank you for visiting our Help function.
             This program is still in ALPHA development therefore we
             still have bugs. Developers please check our issues page
             on Github to submit bugs and work on bugs. Mahalo """
    Yes_or_No = raw_input("Would you like to return?")
    if Yes_Or_No == "Yes":
       Welcome_Screen()
    elif Yes_Or_No == "No":
       Help()
    else:
       Help()


def Search_Query():
    search = raw_input()
    print space
    if search == "-h":
       Help()
    else:
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


def Display_Logo(which_coin):
   if which_coin == "bitcoin":
      return """ ,.=ctE55ttt553tzs.,
             ,,c5;z==!!::::  .::7:==it3>.,
          ,xC;z!::::::    ::::::::::::!=c33x,
        ,czz!:::::  ::;;..===:..:::   ::::!ct3.
      ,C;/.:: :  ;=c!:::::::::::::::..      !tt3.
     /z/.:   :;z!:::::J  :E3.  E:::::::..     !ct3.
   ,E;F   ::;t::::::::J  :E3.  E::.     ::.     \ttL
  ;E7.    :c::::F******   **.  *==c;..    ::     Jttk
 .EJ.    ;::::::L                   "\:.   ::.    Jttl
 [:.    :::::::::773.    JE773zs.     I:. ::::.    It3L
;:[     L:::::::::::L    |t::!::J     |::::::::    :Et3
[:L    !::::::::::::L    |t::;z2F    .Et:::.:::.  ::[13
E:.    !::::::::::::L               =Et::::::::!  ::|13
E:.    (::::::::::::L    .......       \:::::::!  ::|i3
[:L    !::::      ::L    |3t::::!3.     ]::::::.  ::[13
!:(     .:::::    ::L    |t::::::3L     |:::::; ::::EE3
 E3.    :::::::::;z5.    Jz;;;z=F.     :E:::::.::::II3[
 Jt1.    :::::::[                    ;z5::::;.::::;3t3
  \z1.::::::::::l......   ..   ;.=ct5::::::/.::::;Et3L
   \t3.:::::::::::::::J  :E3.  Et::::::::;!:::::;5E3L
    "cz\.:::::::::::::J   E3.  E:::::::z!     ;Zz37`
      \z3.       ::;:::::::::::::::;='      ./355F
        \z3x.         ::~======='         ,c253F
          "tz3=.                      ..c5t32^
             "=zz3==...         ...=t3z13P^
                 `*=zjzczIIII3zzztE3>*^` """



def Cyrpto_Calculator(current_coin):
    print  Display_Logo(current_coin)
    print "Welcome to the calculator for the "+current_coin+" currency!"
    print space
    print "The features that we offer are the following: Check the current price(-c), See what your price would be if it incresed by x amount(-p)"
    print space
    print "Enter those whenever you wish"
    collect_data = raw_input()
    if collect_data == "-c":
       print price_check(current_coin)
       # Should probably change the name
       Coin_Fail_Event()

    elif collect_data == "-p":
       print amount_compare(current_coin)
       Coin_Fail_Event()

def price_check(specific_coin):
    return coin_apis.Coin_PriceCheck(specific_coin)


def amount_compare(specific_coin):
    print "Do you want to see how much your bitcoin would be worth if it increased by a certain amount? Just enter that number directly below and we will do the rest"
    print "NOTE: Enter a dollar amount. Example if a bitcoin cost 1 dollar say you imagine it incrasing to 1000, enter that"
    collect_coin_data = raw_input()
    print calculator.Get_Recent_Price(specific_coin, collect_coin_data)

if __name__ == "__main__":
   Welcome_Screen()
