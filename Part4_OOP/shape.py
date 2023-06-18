from abc import ABC, abstractmethod
import math

# 1. Create abstract class Shape with methods:
class Shape:
    @abstractmethod
    def calculate_perimeter(self): pass
    
    @abstractmethod
    def calculate_area(self): pass

# 2. Create child class Rectangle, inherited from class Shape:
class Rectangle(Shape):

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        return (self.height + self.width)*2
    
    def calculate_area(self):
        return self.height * self.width

# 3. Create child class Square, inherited from class Shape:
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side*4

    def calculate_area(self):
        return self.side ** 2

# 4. Create child class Triangle, inherited from class Shape:
class Triangle(Shape):
    def __init__(self, sides):
        self.sides = sides

    def calculate_perimeter(self):
        return self.sides[0] + self.sides[1] + self.sides[2]

    def calculate_area(self):
        halfPeri = self.calculate_perimeter() / 2
        temp = halfPeri*(halfPeri - self.sides[0])*(halfPeri - self.sides[1])*(halfPeri - self.sides[2])
        return math.sqrt(temp) # Heron
