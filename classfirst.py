class Person:
    def __init__(self , name, country , age , number):
        self.name = name
        self.country = country
        self.age = age
        self.number = number


    def talk(self):
        print(f"Hey! I am {name} form {Country} and my age is {age}")
    #
    def display(self):
        print(f"hey! {self.number}"  )



name = input("Enter the name")
Country = input("Where are you from")
age = input("whats your age")

person = Person(name, Country , age , 5)
# print(person.number)
person.talk()
person.display()

print(" "
      " "
      " "
      " ")
name = "bOb"
Country = "China"
age = 22

person1 = Person(name, Country , age , 50)
# print(person.number)
person1.talk()
person1.display()