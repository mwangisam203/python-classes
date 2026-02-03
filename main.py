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


circle = Circle(color="grey", filled = True , radius=7)

print(circle.color)