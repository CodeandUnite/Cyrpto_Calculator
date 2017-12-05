approved_cyrptos = ["bitcoin","etherium","litecoin"]
counter = len(approved_cyrptos)
input_test = raw_input()

if input_test in approved_cyrptos:
   print "Word is in yo"
else:
   print "Sorry, word no in"
