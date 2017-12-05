#not  Coinsearch file is what will get the coin query and perform the search for that specific cypto-currency

# First step: Get the query string 

 

def Searchdatabase(Inputedsearch):
   #Send to Cyrptodatabase for anylasis   
   Cyrptodatabase(Inputedsearch)

def Search_Failure(Userdefined_Coin):
   import main
   print "User defined coin" + Userdefined_Coin
   Failure_Message = "Sorry, the cyrpto that you just entered "+Userdefined_Coin+ " Is not available"
   main.Coin_Fail_Event()

def Search_Success(Userdefined_Coin):
   import main
   result = "void"  
   main.Pending_Results(Userdefined_Coin)

def Cyrptodatabase(Input_Checker):
   approved_cyrptos = ["bitcoin","etherium","litecoin"]
   counter = len(approved_cyrptos)
   if Input_Checker in approved_cyrptos:
      Search_Success(Input_Checker)
   else:
      Search_Failure(Input_Checker)
        

