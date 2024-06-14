class Employee:
    def __init__(self,name,project,salary):
        self.name = name 
        self._project = project
        self.__salary = salary

    def show(self):
        print("Name :", self.name)

emp = Employee("Bishal", "Niwas" , 99999)
emp.show()
print(emp.name)
print(emp._project)
print(emp._Employee__salary)

class Person:
    def __init__(self,name , age):
        self.name = name
        self.age = age

    def person_info(self):
        print("Name is ", self.name , "age:", self.age)

class Company:
    def __init__(self):
        self._company_name = "Mero Niwas"
        self._location = "Ktm"

    def company_info(self):
        print("Inside Company class")
        print("Company name is: ", self._company_name , "Location is " , self._location)

class Employee(Person , Company):
    def __init__(self, salary , skill):   
        self.__salary = salary
        self.__skill = skill
        Company.__init__(self)
        Person.__init__(self)

    def employee_info(self):
        print("Salary: ", self.__salary , "skill: " , self.__skill, "Location " , self._location , "Name :" , self.name)