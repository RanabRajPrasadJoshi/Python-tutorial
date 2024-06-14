x = int(input("Enter the number"))

if x % 3 == 0 and x % 5 ==0:
    print("it is fizzbuzz")

elif x % 3 == 0:
    print("it is Fizz")

elif x % 5 ==0:
    print("it is Buzz")