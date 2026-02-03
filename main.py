#super(): =>function used in a child class to call methods from the parent class (superclass)

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
        

class Circle:
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

        

class Square:
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.radius = width
    
class Triangle:
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.radius = width
        self.height = height