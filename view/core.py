# This will make it visable
import sys
import time
sys.path.append('../')
#from controller import processor
import model
import controller
'''
MIT License

Copyright (c) 2017 Austin 

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
logo = """
 _____                 _         _____      _            _       _
  / ____|               | |       / ____|    | |          | |     | |
 | |    _   _ _ __ _ __ | |_ ___ | |     __ _| | ___ _   _| | __ _| |_ ___  _ __
 | |   | | | | '__| '_ \| __/ _ \| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |___| |_| | |  | |_) | || (_) | |___| (_| | | (__| |_| | | (_| | || (_) | |
  \_____\__, |_|  | .__/ \__\___/ \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|
         __/ |    | |
        |___/     |_|

"""

default_null_string = "null"
default_boolean = False
STATIC_VERSION = "Version: 0.1-Alpha4"
def currency_list():
	standard_space = "             "
	return """
           Bitcoin:            Type Bitcoin or bitcoin
           Litecoin:           Type Litecoin or litecoin
           Etherium:           Type Etherium or etherium
	       """

def Launch_module():
   print logo
   print """     VERSION: 0.1-Alpha4
                 QUICK START COMMANDS:
    Help module -h | List of cyrptocoins, -l | Pick a cyrptocoin, type -p
   
    

	      """
   capture_input = raw_input("Please type a command to begin")
   if "-h" in capture_input:
      print Help_module()
      capture_input = raw_input("Enter another command please")
   if "-l" in capture_input:
      print currency_list()
      capture_input = raw_input("Enter another command please")
   if "-p" in capture_input:
      Is_coin_in_database(default_null_string, default_boolean)
   else: 
      print "We do apologize, but the input you entered " + capture_input + "could not be recognized and/or is not a valid command. Rerouting you to the Launch_module"
      time.sleep(1)
      Launch_module()
	

def Help_module():
   return """ We value users! We understand that issues can be frustrating! Unfortunately, we cannot help you directly from this program however, you may contact us through our Github page. Please create an account and report an issue! One of our code maintainers will 
             reach you promptly. """

def coin_selection_module(Load_Coin):
   print " Welcome to the menu for " + Load_Coin 
   print """ 
     The default conversion currency is USD, Option to change is not available at this time
     If you would like to check the price for your coin, please type -s
     If you would like to calculate how much your coin could rise, type -f
    """ 
   capture_input = raw_input()
   
   if "-s" in capture_input:
      coin_tuple_of_data = (Load_Coin, "usd")
      Retrive_Price_module(coin_tuple_of_data)
   if "-f" in capture_input:
      Calculator_module(Load_Coin)


def Retrive_Price_module(data_tuple):
   from controller import processor
   current_coin_price = processor.Start_Price_Retrivel(data_tuple)
   print "The current price for your selected coin is " 
   print current_coin_price
   time.sleep(2)
   Launch_module()


def Calculator_module(Selected_Coin):
   from controller import processor
   print "Welcome to the calculator feature. Below are the features we offer:"
   print "        - Calculate how much the price would increase by a user defined amount"
   print "        EXAMPLE: '-v 100'"
   print "        - See a percentage of what the price would do if increased by a user defined amount"
   print "        EXAMPLE  '-inc 100'| the numerical digit signifying a percentage '%' increase of the base value  "
   print "        - See a percentage of what the price would do if decreased by a user defined amount"
   print "        EXAMPLE '-dec 100' | the numerical digit signifying a percentage '%' decrease of the base value  "
   print "Whenever you're ready, please enter your input"
   obtain_command_var, obtain_numerical_command = raw_input().split()
   if obtain_command_var == "-v":
      numerical_make_numeric = float(obtain_numerical_command)
      output =  processor.Collect_Calculator_Data(Selected_Coin, obtain_command_var, obtain_numerical_command)
      # Fix later to beautify. Just need to verify that it works. 
      print "If your coin increased it would be worth this amount", output 
   elif obtain_command_var == "-inc":
      output =  processor.Collect_Calculator_Data(Selected_Coin, obtain_command_var, obtain_numerical_command)
   elif obtain_command_var == "-dec":
      output =  processor.Collect_Calculator_Data(Selected_Coin, obtain_command_var, obtain_numerical_command)
   else:
      print "Your input is garbage. "

def handle_failure_event():
	print "We apologize but that coin is not avaliable yet! If you want it, you can add it! Checkout our Github page"
	print "Heading back to the main menu"
	time.sleep(2)
	Launch_module()


def Is_coin_in_database(users_cyrpto_coin, default_boolean_condition):
   from controller import processor
   print "Please enter a cyrptocurrency"
   default_boolean_condition = False
   users_cyrpto_coin = raw_input().lower()
   record_response = processor.verify_cyrptos(users_cyrpto_coin, default_boolean_condition)
   coin_string, returned_boolean = record_response
   if returned_boolean == True:
      coin_selection_module(coin_string)
   elif returned_boolean == False:
      handle_failure_event()
 
	
	#Sending for vertification and procressing 
# Test
Launch_module()