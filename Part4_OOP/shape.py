from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
import math
'''
1
'''


class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    def calculate_area(self):
        pass


'''
2
'''
@dataclass
class Rectangle(Shape):
    height: float
    width: float
    def calculate_perimeter(self):
        return (self.height + self.width)*2
    def calculate_area(self):
        return self.height * self.width

'''
3
'''
@dataclass
class Square(Shape):
    side: float
    def calculate_perimeter(self):
        return self.side * 4
    def calculate_area(self):
        return self.side * self.side

'''
4
'''
@dataclass 
class Triangle(Shape):
    sides: list[float]
    def calculate_perimeter(self):
        return sum(self.sides)
    def calculate_area(self):
        p = self.calculate_perimeter()/2
        return math.sqrt(p*(p-self.sides[0])*(p-self.sides[1])*(p-self.sides[2]))
    
# temp = Triangle((3,4,5))
# print(temp.calculate_area())
# print(temp.calculate_perimeter()


