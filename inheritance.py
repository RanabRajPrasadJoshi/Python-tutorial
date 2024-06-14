class Person:
    def person_info(self, fname, lname):
      print("Indside Person")
      self.firstname = fname
      self.lastname = lname
      print("your name is ", self.firstname + self.lastname)

class Company:
    def companyInfo(self, cname, location):
        print("Inside company")
        self.companuyname = cname
        self.location = location
        print("your Company is ", self.companuyname , "located in " , self.lastname)

class Employee(Person , Company):
    def employe_info(self, salary, skill):
        super().person_info("dhiraj","Thapa")
        super().companyInfo("Shivapuri","Maharajjung")
        print("inside employee")
        print("Salary", salary , "Skil" , skill )


emp = Employee()
emp.employe_info(2000,"Compueter")

    