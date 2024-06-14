class Vechile:

    def __init__(self,name,number,price):
        self.name = name
        self.number = number
        self.price = price
    def Display(self):
        print("Car nakme is" , self.name, " number is ", self.number, " and price is" , self.price)
    def max_speed():
        print("Max speed is 100km/hr")
    def change_gear():
        print("Max speed is 6gear")

class Car(Vechile):

    def max_speed(self):
        print("Max speed is 220km/hr")
    def change_gear(self):
        print("Max speed is 6gear")


car = Car("Car", 2234 , 2035999)
car.max_speed()
car.change_gear()
Vechile.max_speed()