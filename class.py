class Circle:

    def __init__(self, num1, num2):
            self.num1 = num1
            self.num2 = num2
            self.add = self.num1 + self.num2
            self.subtract = self.num1 - self.num2
            self.muxx = self.num1 * self.num2
            self.divide = self.num1 / self.num2

    def Sum(self, *args):
        total = 0
        for n in args:
            total+=n
        return total
        
    def Sub(self, *args):
        total = 0
        for n in args:
            total-=n
        return total
        
    def mux(self, num1, num2):
        return num1 * num2
    
    def divid(self, num1, num2):
        return num1 / num2
    
        


    
Circccle = Circle(3,4)
print(Circccle.add)
print(Circccle.Sum(2,3,4))
print(Circccle.mux(2,3))
print(Circccle.divid(4,2))
print(Circccle.Sub(4,3))

        
    