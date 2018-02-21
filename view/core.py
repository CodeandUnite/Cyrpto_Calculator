<<<<<<< HEAD

# -*- coding: utf-8 -*-

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

def program_router(Reroute_tuple):
# Send a tuple to this program for Processing
# Tuple needs to contain code, coin_name, gdp_currency
# Tuple can be NULL for coin_name and gdp_currency when not neccessary

    """ The rerouter serves as the directory method for the program. It will
    collect an specific code (1-2) for going to views and 3,4 for -help,
    -license. This will allow it to minimize code in each module"""

    """ This will reroute the program to its selected destination  """

    access_code,cyrpto, gdp = Reroute_tuple




#def Router_features():
#    print "To go back to the home screen, type 1"
#    print "To go back to the calculator choice, type 2"

def currency_list():
    """
    All current currencies our calculator offers will be avialable here.
    This allows for us to add new entries simply.
    """
    standard_space = "             "
    return """
    --------------------------------------------------------------
                         Cyrptocurrencies
           Bitcoin:            Type Bitcoin or bitcoin
           Litecoin:           Type Litecoin or litecoin
           Etherium:           Type Etherium or etherium

           MORE TO COME
    --------------------------------------------------------------

    --------------------------------------------------------------
                        Fiat currencies
        United States Dollar -----> Type usd
        British Stirling  --------> Type gbp
        Europen Euro -------------> Type eur
        Indian Rubee --------------> Type rur

        MORE TO COME

    --------------------------------------------------------------
	       """


def launch_view():
    """
    This is the main view that people will see when entering the program.
    Its duties are to collect data from the user, interpret the data, and
    send it on its way to its selected destination.
    """
    print logo
    print """
    Welcome to Cyrpto Calcculator!

    COMMANDS:

    ['-h' ] Use this command for a comprehensive help module

    ['-l' ] Use this command for a complete list of cyrpto-currencies and standard GDP currencies that we offer

    ['-p'] [coin_name] [Standard currency e.g usd, ]

         """


    captured_input = raw_input("Please enter your command")

    try:
       obtain_specific_command, obtain_cyrpto_coin, obtain_gdp_currency = captured_input.split(" ")
       Is_coin_in_database(obtain_cyrpto_coin, obtain_gdp_currency,default_boolean)
    except ValueError:
       captured_input = captured_input
       if "-h" in captured_input:
          make_tuple = 4, "null", "null"
          print program_router(make_tuple)
          # Needs to redirect back after command entered
          captured_input = raw_input("Please enter another command please")
       if "-l" in captured_input:
          make_tuple = 5, "null", "null"
          print program_router(make_tuple)
          # Needs to redirect back after command entered
          captured_input = raw_input("Please enter another command please")
       #else:
        #  print "We do apologize, but the input you entered " + captured_input + "could not be recognized and/or is not a valid command. Please re-enter your command"
        #  time.sleep(1)
        #  launch_view()



# This is a standard help menu that features a FAQ for common problems and
# resoruces for how to connect to someone to report a bug, enhancement
def help_view():
    return """

    FAQ
    --------------
    1. The application is not returning any data?

    There could be several reasons for this. The frist is perhaps our API is down.
    All request go through the API. So, if you are not receiving anything at All
    you might have to wait till the API is back in operation. However, if your
    are a developer, perhaps you could add the functionality for an back-up
    API? If this problem persist, please contact us!

    2. I get an error when I try and submit an cyrpto to calculate

    When you enter your command please make sure

          """

def cyrptocoin_user_choice_view(cyrptocoin, gdpcurrency):
   """
   This part of the view serves as the key view for retriveing user data for
   the calculator module
   """
   print 'Calculator initilized for %s' % (cyrptocoin)
   print 'Fiat currency initilized for %s' % (gdpcurrency)
   print """
                Calculator Commands
 -------------------------------------------------------------
 '-check' If you would like to check the price for your cyrptocurrency
 '-rise percentage  ex. -rise 10'  If you would like to see how much your cyrpto would increase by a percentage
 '-fall percentage ex. -fall 10'  If you would like to see how much your cyrpto would decrease by a percentage

 -------------------------------------------------------------
        """
   user_calculator_decision = raw_input("Enter your input now")
   try:
      command, percentage = user_calculator_decision.split(" ")
      good_int = int(percentage)
      Datatuple = (cyrptocoin, gdpcurrency, command, good_int)
      retrive_price_helper(Datatuple)

   except ValueError:
      if "-check" in user_calculator_decision:
         print "Processing"
         tuple_coin_data = (cyrptocoin, gdpcurrency,user_calculator_decision, 0)
         retrive_price_helper(tuple_coin_data)
        #print gdpcurrency

def retrive_price_helper(data_tuple):
    """
    This acts as a helper for the processor. It will send the data that was retrieved
    in the view data collection module(cyrptocoin_user_choice_view) and send it
    to the processor. The data will be interpreted and then regurgetated here
    """

    from controller import processor
    cyrpto_name, gdp_name, command, command_number = data_tuple
    if command == "-check":
       current_coin_price = processor.Start_Price_Retrivel(data_tuple)
       print '%s is currently worth %d in %s fiat currency' % (cyrpto_name, current_coin_price, gdp_name)
    if command == "-rise":
       risen_price = processor.Price_retrivel_other_processes(data_tuple)
       """ Example text
       print 'Your cyrptocurrency %s if raised by %d would be worth about %d % (name, name2, name3) '"""
       # Might want to add the original price aswell
       print 'If your %s was raised by %d percent it would be worth approximately %d in %s fiat currency' % (cyrpto_name, command_number, risen_price, gdp_name)
    if command == "-fall":
        # Again, add original price
        fallen_price = processor.Price_retrivel_other_processes(data_tuple)
        print 'If your %s fell by %d percent it would be worth approximately %d in %s fiat currency' % (cyrpto_name, command_number, fallen_price, gdp_name)




    print ""
    time.sleep(5)
    print """
        -------------------------------------
         You can type a new or another command |-check, -raise [percentage], -fall [percentage] |
         OR do the following:
         To go back to the main menu, type -menu
         To terminate the program, type -terminate or simply exit the program
        -------------------------------------
         """
    collect_info = raw_input("Please enter your response.")
    if collect_info == "-check":
       retrive_price_helper(data_tuple)
    if collect_info == "-raise":
       retrive_price_helper(data_tuple)
    if collect_info == "-fall":
       retrive_price_helper(data_tuple)
    if collect_info == "-menu":
       launch_view()
    if collect_info == "-terminate":
       print "Thank you for using the program. Goodbye"
       exit()





# Must check with the processor to ensure that everything the user sent is in place and accurate
def Is_coin_in_database(UsersCyrpto_Precheck,UsersGDP_Precheck, default_boolean_condition):
    from controller import processor
    true_or_false_verifyer = False
    record_response = processor.verify_cyrptos(UsersCyrpto_Precheck, UsersGDP_Precheck, default_boolean_condition)
    user_cyrptocoin, user_gdpcurrency, boolean_decision = record_response
    # Upon successful vertification we need to proceed
    if boolean_decision == True:
       cyrptocoin_user_choice_view(user_cyrptocoin, user_gdpcurrency)
    if boolean_decision == False:
       #print "Sorry but either " + UsersCyrpto_Precheck + " or " + UsersGDP_Precheck + " could not validated "
       print "Sorry but %s is not a valid or not in our list of available currencies" % UsersGDP_Precheck
       print "Sorry! It seems that %s was not a valid gdp currency" % UsersCyrpto_Precheck

       print """
        -------------------------------------------------
           To enter new text, please type 1
         Other wise the program will terminate in 2 minutes
        -------------------------------------------------
            """
       collect_input = raw_input("Enter your input now")

#For the event where the coin is not in the database


launch_view()
=======
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
        print "We do apologize, but the input you entered " + capture_input + "could not be recognized and/or is not a valid command. Please re-enter your command"

        time.sleep(1)
        Launch_module()


def Help_module():
    return """ We value users! We understand that issues can be frustrating! Unfortunately, we cannot help you directly from this program however, you may contact us through our Github page. Please create an account and report an issue! One of our code maintainers will
             reach you promptly. """


def coin_selection_module(Load_Coin):
    print " Welcome to the menu for " + Load_Coin
    print """
     The default conversion currency is USD, Option to change is not available at this time
     If you would like to check the price for your coin, please type -check
     If you would like to calculate how much your coin could rise, type -cal
    """
    capture_input = raw_input()

    if "-check" in capture_input:
        coin_tuple_of_data = (Load_Coin, "usd")
        Retrive_Price_module(coin_tuple_of_data)
    if "-cal" in capture_input:
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
    print "        EXAMPLE  '-inc 0.3'| the numerical digit signifying a percentage '%' increase of the base value  "
    print "        - See a percentage of what the price would do if decreased by a user defined amount"
    print "        EXAMPLE '-dec 0.3' | the numerical digit signifying a percentage '%' decrease of the base value  "
    print "Whenever you're ready, please enter your input"
    obtain_command_var, obtain_numerical_command = raw_input().split()
    if obtain_command_var == "-v":
        numerical_make_numeric = float(obtain_numerical_command)
        output = processor.Collect_Calculator_Data(
            Selected_Coin, obtain_command_var, obtain_numerical_command)
        # Fix later to beautify. Just need to verify that it works.
        print "If your coin increased it would be worth this amount", output
        time.sleep(2)
        Launch_module()
    elif obtain_command_var == "-inc":
        output = processor.Collect_Calculator_Data(
            Selected_Coin, obtain_command_var, obtain_numerical_command)
        print "If your coin were to increase by", obtain_numerical_command, "''%' it would be worth", output
        time.sleep(2)
        Launch_module()
    elif obtain_command_var == "-dec":
        output = processor.Collect_Calculator_Data(
            Selected_Coin, obtain_command_var, obtain_numerical_command)

        print "If your coin was to decrease by", obtain_numerical_command, "it would be worth approximately", output
        time.sleep(2)
        Launch_module()

    else:
        print "Sorry, but your input of",obtain_command_var, "could not be recognized! If you believe this was an error please report this on our Github. Restarting module"
        time.sleep(1)
        Calculator_module(Selected_Coin)


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


Launch_module()
>>>>>>> c6dd36c66de50d7d3e5dddf19b4f5bd03f6a1dbd
