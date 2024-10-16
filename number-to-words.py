numbers = {
    1 :"one",
    2 :"two",
    3 :"three",
    4 :"four",
    5 :"five",
    6 :"six",
    7 :"seven",
    8 :"eight",
    9 :"nine",
    0 :"ten"
}
gg =int(input("Enter the number"))

in_list = []
out_list=[]
while(gg>0):
    temp = gg%10

    in_list.append(temp)
    gg = int(gg / 10)
in_list.reverse()
for item in in_list:
    if item in numbers:
        print(numbers[item], end=" ")
