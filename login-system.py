#input email
#check email if email exist ask for password else go home,
#input password
#if email and password are correct then successfully logged in else go home


user= {
    "qw":"12",
    "ranabjoshi@gmail.com" : "Home1234",
    "ranabjoshi11@gmail.com" : "Home123411",
}
flag = True
while(flag):
    print("Welcome to facebook \n \n")
    email = input("Enter your email: ")
    try:
        if (user[email]):
            password = input("Enter your password: ")
            if(password == user[email]):
                print("Logged in successfully")
                print("Click me :  https://github.com/RanabRajPrasadJoshi/C-Sharp--basics")
            else:
                print("go home your pass is incorrect")

    except KeyError:
        print("go home email doesnot exit")
    select = int(input("Enter 1 to continue "
                   "Enter 2 or more to exit: "))
    if select  > 1:
        print("Thanks for joining")
        flag = False
