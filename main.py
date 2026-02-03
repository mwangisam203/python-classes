#super(): =>function used in a child class to call methods from the parent class (superclass)

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
        

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

        

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width
    
class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height


circle = Circle("grey", True , 7)
square = Square("Violet", False, 15)
triangle = Triangle("brown", True, 13, 20)

print(circle.color)
print(circle.radius)
print(circle.filled)

print(triangle.height)
print(f"{triangle.height} cm")