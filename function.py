# print
def Display():
    print('Hlo')

Display()

print("-------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------")

# add
def AddNum(x ,y):
    print(x+y)

AddNum(3,4)

print("-------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------")
# add
def AddNum(x,y):
    print(x+y)

AddNum(y=1,x=5)
print("-------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------")

# string concinate
def StringConcatinate(FirstName, LastName):
    print(FirstName + LastName)
    print("Your first Name",  FirstName)
    print("Your last Name", LastName)
    print("Your Full Name",  FirstName + " " + LastName)


StringConcatinate( "Adarsh" , "Tamang" )
print("-------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------")

# string concinate
def StringConcatinate(FirstName, LastName):
    print(FirstName + LastName)
    print("Your first Name",  FirstName)
    print("Your last Name", LastName)
    print("Your Full Name",  FirstName + " " + LastName)


StringConcatinate(LastName= "Tamang", FirstName="Adarsh"  )
print("-------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------")

# radius  
a = int(input("Enter the radius"))


def CirculeArea(radius):
    print(3.14 * (radius*radius))

CirculeArea(a)

print("-------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------")

# add

def Sum(*args):
    total = 0
    for n in args:
        total+=n

    return total

num = Sum(2,5,67,8,1)
print(num)


print("-------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------")







