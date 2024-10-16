numbers = [2,2,2,2,5]

for number in numbers:
    out = ""
    for x in range(number):
        out += "x"
    print(out)

#or
print("\n \n")

for number in numbers:
    print("x"*number)
