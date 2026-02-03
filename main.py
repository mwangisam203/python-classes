#super(): =>function used in a child class to call methods from the parent class (superclass)

class Circle:
    def __init__(self, color, filled, radius):
        self.color = color
        self.filled = filled
        self.radius = radius

        

class Square:
    def __init__(self, color, filled, radius):
        self.color = color
        self.filled = filled
        self.radius = radius
    
class Triangle:
    def __init__(self, color, filled, radius):
        self.color = color
        self.filled = filled
        self.radius = radius