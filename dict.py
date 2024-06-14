capital={
   "Nepal":"Kathmandu",
    "USA":"Washington D.C.",
    "Canada":"Ottawa"
}
print(capital)
print(len(capital))
print(type(capital))

print(capital.keys())
print(capital.values())

print(capital['Nepal'])
capital['Japan']="Tokyo"
print(capital)

capital['Bhutan']="Thimppu"
print(capital)

pop_element=capital.pop("Bhutan")
print(pop_element)
print(capital)

a={1,2,3,4}
b={1,2,3,4}

marks={
    "Maths": 80,
    "Science": 80,
    "Nepal": 80
}
print(marks)
capital.update(marks)
print(capital)
copy_capital=capital.copy()
print("This is a copy capital :", copy_capital)

copy_capital.clear()
print(copy_capital)

print(marks.items())

test={'key1':{'nestkey':{'subnestkey':'hello'}}}
print(test['key1']['nestkey']['subnestkey'])
print(test['key1']['nestkey'])
print(test['key1'])
print(test.values())

student={}
print(type(student))
student["Name"]="Ranab Josi"
print(student)

student['age']=17
student['address']='kathmandu'
student['education']='SEE'
print(student)