from pprint import PrettyPrinter

numbers = [11237,122121,9,1,2,7,11]
#1,2,3,5,7,11,13,17,19

primary_number = []
count = 0
val = False
for number in numbers:
    if number in primary_number:
        continue    #remove the number if it is a repeated number or the number already exists
    if number == 1:
        primary_number.append(number)  # 1 is a prime number so its always printed
    for i in range(1,number):
        if number % i ==0:
            count+=1
        if count >= 2:
            count = 0
            val= False
            break
        else:
            val = True
    if val==True:
        primary_number.append(number)

    val = False
    count = 0
print("Primary numbers;")
for num in primary_number:

    print(num)

print("Orginal numbers:")
print(numbers)
print("Primary numbers:")
print(primary_number)



