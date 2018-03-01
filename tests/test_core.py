# This will test the core view of the program
import pytest


def home_screen_view():
    default_check_boolean = False
    ''' The home_screen_view is the first view that the user will encounter.
    Here it collects crucial input that the program needs and sends it to the
    destination that the user defines '''
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




    if check_code == 0:
        ''' The 0 check code will ensure that the -p command is accurate'''
        verifyInfo = (command, cyrpto, fiat, check_code)
        booleanJuryDecision = input_sanitize_and_check_helper(verifyInfo)
        if booleanJuryDecision == True:
            ''' The data is now safe to send to the calculator view.
            The view should first go to a helper view to handle this exiting
            home screen view '''
            prepareCalcData = (command, cyrpto, fiat)
            calculator_view(prepareCalcData)
        if booleanJuryDecision == False or None:
            print "We apologize but the data that was sent could not be verified."
            print "Please make sure that you type your command exactly. If the problem persist please check the --help module"
            print "Redirecting you to home_screen...."
            time.sleep(2)
            print "Loading your data....."
            time.sleep(2)
            home_screen_view()

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
