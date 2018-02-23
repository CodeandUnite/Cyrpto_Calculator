# -*- coding: utf-8 -*-

# This will make it visable
import sys
import time
sys.path.append('../')

#from controller import processor
#import model
#import controller
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
version = "V0.1 Alpha5"

def reroute_automatic():
    ''' This will reroute the user whenever --help or --list are entered at
    anytime for the duration of the program'''

def input_sanitize_and_check_helper(tupleCheck):
    from controller import processor
    ''' This function will check the input that is entered. This is good to
    ensure that no unexpected errors happen when the program is in opeeration.
    This function will receive different variables under different conditions.
    '''

    ''' This is a central method of checking input that is inputted throughout
    the program. Each command_code number signifies a different area of the program
    that will be checked.

    COMMAND NUMBER LIST:
    1 --> This will check the input for --help and --list within the calculator function
    2 --> This will check the input for --check within the calculator function
    3 --> This will check for --rise and --fall within the calculator function '''

    command, cyrpto, fiat, command_code = tupleCheck



    if command_code == 0:
        processorCheckVariables = (cyrpto, fiat)

        Allowed_Verifcation = processor.handle_cyrpto_and_fiat_database_check(processorCheckVariables)
        if Allowed_Verifcation == True:
            PassFailBoolean = True
            return PassFailBoolean
        if Allowed_Verifcation == False:
            PassFailBoolean = False
            return PassFailBoolean

    if command_code == 1:
        if command == "--help":
            PassFailBoolean = True
            return PassFailBoolean

        if command == "--list":
            PassFailBoolean = True
            return PassFailBoolean

    if command_code == 2:
        if command == "--price":
            PassFailBoolean = True
            return PassFailBoolean
        else:
            PassFailBoolean = False
            return PassFailBoolean
    if command_code == 3:
       if command == "--rise":
           PassFailBoolean = True
           return PassFailBoolean






def help_view():
    print "Welcome to the help view"

def currency_list_view():
    print """
    cyrpto currencies available:
    Bitcoin  ---> btc
    Litecoin ---> ltc
    Etherium ---> eth

    Fiat conversion currencies available:
    United States Dollar ---> USD
    British Pound        ---> GBP

          """
def home_screen_view():
    print logo
    print version
    print "Welcome to Cyrptocalculator!"
    print """
    QUICK START COMMANDS:
    |--help| This command will launch a help screen for the user
    |--list| This command will show all currencies avialble aswell as the fiat currencies available for conversion
    |--version| This command will show you the most recent version that is available for download

    |-p| |coin_name| |fiat currency| - This is the go to command to start the applications calculator function
          """
    collect_initial_input = raw_input("Please enter your input")
    # This try and except will eliminate the value error when user enters only one command
    try:
        command, cyrpto, fiat = collect_initial_input.split(" ")
        check_code = 0
    except ValueError:
        collect_initial_input == collect_initial_input
        check_code = 1


    default_check_boolean = False


    if check_code == 1:
        null_null = "null"
        verifyInfo = (collect_initial_input, default_check_boolean,null_null, check_code)
        # This should return a TRUE or FALSE boolean
        booleanJuryDecision = input_sanitize_and_check_helper(verifyInfo)
        if booleanJuryDecision == True:
        # Now that we know that the input is verified we can proceed with operations
            while collect_initial_input == "--help":
                print help_view()
                time.sleep(2)
                home_screen_view()
            while collect_initial_input == "--list":
                print currency_list_view()
                time.sleep(2)
                home_screen_view()
        if booleanJuryDecision == False:
            '''TO DO
            1. Need to define what the error it
            2. Must create a way to mitigate the error for the user '''
            print "An error occured!"
    if check_code == 0:
        verifyInfo = (command, cyrpto, fiat, check_code)
        booleanJuryDecision = input_sanitize_and_check_helper(verifyInfo)
        if booleanJuryDecision == True:
            ''' The data is now safe to send to the calculator view.
            The view should first go to a helper view to handle this exiting
            home screen view '''
            prepareCalcData = (command, cyrpto, fiat)
            calculator_view(prepareCalcData)


def calculator_view(calculatorData):
    from controller import processor
    from model import bitcoin
    command, cyrptoCurrency, fiatCurrency = calculatorData
    print "Calculator has been initilized for %s cyrptocurrency and %s fiat currency" % (cyrptoCurrency, fiatCurrency)
    print """
 Welcome to the main feature of this program, namely, the calculator!
 Here are the commands that you can use to begin the program

 |--price| This will retrive the current price of the cyrptoCurrency
 |--rise percentage | Use this command to see the price of your selected currency inflated by a user defined amount. P.S. Please enter the number 10-100. CASE SENSITIVE
 |--fall percentage | Use this command to see the price of your selected currency deflated by a user defined amount. P.S. Please enter the number 10-100. CASE SENSITIVE

          """
    collect_input = raw_input("Please enter your response now")
    try:
        command_variable, percentage_variable = collect_input.split(" ")
        dataTuple = (command_variable, percentage_variable,cyrptoCurrency, fiatCurrency)
        calculator_helper_one(dataTuple)
    except ValueError:
        collect_input == collect_input
        dataTuple = (cyrptoCurrency, fiatCurrency)
        calculator_helper_two(dataTuple)

def calculator_helper_one(lovely_data):
    from model import bitcoin
    from controller import processor
    command, percentage, cyrpto, fiat = lovely_data
    obtain_price = (cyrpto, fiat)
    price = bitcoin.api_price_retrivel(obtain_price)
    verification_code = 3
    default_boolean = False
    PackageDataVerify = (command, percentage, default_boolean, verification_code)
    CleanDataBooleanDecision = input_sanitize_and_check_helper(PackageDataVerify)

    if CleanDataBooleanDecision == True:


        if command == "--rise":
            equationNeededVariables = (cyrpto, fiat, percentage, price)
            equationReturn = processor.handle_cyrpto_rise_calc(equationNeededVariables)
            print equationReturn
            print "If %s were to increase by %s it would roughly worth %d in %s fiat currency" % (cyrpto, percentage, equationReturn, fiat)
        elif command == "--fall":
            equationNeededVariables = (cyrpto, fiat, percentage, price)
            equationReturn = processor.handle_cyrpto_rise_calc(equationNeededVariables)
            print equationReturn

def calculator_helper_two(lovely_data):
    from controller import processor
    user_cyrpto, user_fiat = lovely_data
    current_price_for_user = processor.handle_cyrpto_price_check(lovely_data)
    print "The current price for %s is %d" % (user_cyrpto, current_price_for_user)
    










home_screen_view()
