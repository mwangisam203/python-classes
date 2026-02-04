#super(): =>function used in a child class to call methods from the parent class (superclass)
import math

class Shape:
    def __init__(self, color, filled, unit="cm"):
        self.color = color
        self.filled = filled
        self.unit = unit

    def area(self):
        raise NotImplementedError("Subclasses must implement area()")


class Circle(Shape):
    def __init__(self, color, filled, radius, unit="cm"):
        super().__init__(color, filled, unit)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Square(Shape):
    def __init__(self, color, filled, width, unit="cm"):
        super().__init__(color, filled, unit)
        self.width = width

    def area(self):
        return self.width ** 2


class Triangle(Shape):
    def __init__(self, color, filled, width, height, unit="cm"):
        super().__init__(color, filled, unit)
        self.width = width
        self.height = height

    def area(self):
        return 0.5 * self.width * self.height

circle = Circle("grey", True , 7) 
square = Square("Violet", False, 15) 
triangle = Triangle("brown", True, 13, 20)

print(circle.color) 
print(circle.radius) 
print(circle.filled)

print(triangle.height) 
print(f"{triangle.height}cm") 
print(triangle.area())
print(square.area())

#Polymorphism => have many forms or faces
class Shapes:
    pass

class Circles(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
        

class Square(Shapes):
    def __init__(self, length):
        self.length = length


    def area(self):
        return self.length ** 2
    
        

class Triangle(Shapes):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        
        