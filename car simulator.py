
flag = True
st = 0
stt=0
while(flag == True):
    msg = input(">").upper()
    if msg == "HELP":
        msg = input('''Enter Start to start the car
Enter Stop to stop the car
Enter Quit for quit \n''').upper()

    if msg == "START":
        if not abs(st) >=1:
            print("Car started succcessfully")
            st +=1  #
            stt = 0
        else:
            print("Car already started")
    elif msg == "STOP":
        if not abs(stt) >=1:
            print("Car stoped succcessfully")
            stt +=1
            st = 0
        else:
            print("Car already stopped")
    elif msg == "QUIT":
        print("Thanks for joining")
        flag = False
    else:
       print("I cannot understand you:")
