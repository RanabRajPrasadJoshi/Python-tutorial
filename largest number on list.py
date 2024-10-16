numbers = [11,22 ,3123, 43, 5]
temp = numbers[0]
temp1= numbers[0]
for number in numbers:
    if number>temp:
        temp =number
    if number<temp1:
        temp1 =number
print(temp)
print(temp1)
