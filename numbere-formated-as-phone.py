number = input("Enter a number")
if len(number)==10:
    print("(" , end="")
    for i in range(0,3):
        print(number[i], end="")
    print(") " , end="")
    for i in range(3,len(number)):
        print(number[i], end="")