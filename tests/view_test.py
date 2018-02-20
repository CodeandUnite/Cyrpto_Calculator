# This will test that the view is working properly

def p_processor():
    command = raw_input("Please enter your command")
    try:

       test_one, test_two, test_three = command.split(" ")
       print test_one
       print test_two
       print test_three
    except ValueError:
       test_one = command
       print test_one


# Incorporate a try and except to catch ValueError

p_processor()
