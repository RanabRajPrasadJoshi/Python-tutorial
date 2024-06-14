# x = lambda a, b: a+b
# # num1 = int(input("enter an even number"))
# # num2 = int(input("enter an even number"))
# # print(num1+num2)
# add = x(10,10)
# print(add)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
print (factorial(5))