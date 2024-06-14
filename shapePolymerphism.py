import math
class Shape:
    def area(self):
        raise NotImplementedError("Sub classes must be implement this method")
    
class Rectangle(Shape):
    def __init__(self, width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
class Triangle (Shape):
    def __init__(self,base, height):
        self.base = base
        self.heigth = height

    def area(self):
        return 0.5 * self.base * self.heigth
    

l = int(input("Enter the length of Rectangle"))
w = int(input("Enter the width of Rectangle"))
rectangle = Rectangle(l,w)
print("area of Rectangle is", rectangle.area())

r = float(input("Enter the radius of Circle"))
circle = Circle(r)
print("area of Circle is", circle.area())
    
b= int(input("Enter the base of Triangle"))
h = int(input("Enter the height of Triangle"))
triangle = Triangle(b,h)

print("area of Triangle is", triangle.area())
        

    
