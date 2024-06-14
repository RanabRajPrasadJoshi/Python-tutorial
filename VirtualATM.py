AtmNumber = input("Enter the ATM card number using `-` after each 4 digit: ")
AtmNumber = AtmNumber.replace(" ","")    #remove spaces
if AtmNumber != "":    #not to make the empty input bar
    if AtmNumber == "1111-2222-3333-4444":    #check the data exixt in db or not
        print("Succes using ATM Number")
        Amount = input("Enter the amount you want to withdraw")
        Amount = Amount.replace(" ","")     #remove spaces
        if Amount != "":     #not to make the empty input bar
            Amount = int(Amount)       #type casting
            Code = input("Enter the code of atm number")
            Code = Code.replace(" ","")      #remove spaces
            OldAmount = 50000
            if Code != "":      #not to make the empty input bar
                Code = int(Code)      #type casting
                if Code == 3435:   #check the data exixt in db or not
                    if Amount <= OldAmount:     #Check the amount in the bank
                          print("Successfully Withdraw Amount ",+ Amount)
                          print("Your now balance after WithDraw is: ", +  OldAmount - Amount )
                    
                    else:
                        print("Insufficient Balance")
                #from here all are the errors
                else:
                    print("Please try Again! your code is incorrect")
            else:
                print("Please try Again! Your Code is empty")
        else:
            print("Please try Again! Your amount is Empty")
    else:
        print("Please try Again! You entered Incorrect AtmNumber ")
else:
    print("Please try Again ! Your AtmNumber is Empty")

