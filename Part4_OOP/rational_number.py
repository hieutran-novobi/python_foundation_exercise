import math

# 5. Create class RationalNumber with attributes
# 7. Create method simplify() to simplify the retional number:
# 8. Override __str__() method to display the RationalNumber object when it is represented as a string
# 9. Override __add__(), __sub__(), __mul__() and __div__() methods to perform arithmetic with rational numbers
# 10. Override __lt__(), __gt__() and __eq__() methods to perform comparison with rational numbers
class RationalNumber:
    def __init__(self, numerator, denominator=1):
        if type(numerator) is not int or type(denominator) is not int:
            raise NotIntegerError()
        if denominator == 0:
            raise ZeroDenominatorError()
        self.numerator = numerator
        self.denominator = denominator        

    def simplify(self):
        gcdDiv = math.gcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator / gcdDiv)
        self.denominator = int(self.denominator / gcdDiv)

    def __str__(self):
        self.simplify()
        if self.denominator == 1:
            return f"{self.numerator}"
        else:
            return f"{self.numerator}/{self.denominator}"
    
    def __add__(self, obj):
        numerator = self.numerator * obj.denominator + obj.numerator * self.denominator
        denominator = self.denominator * obj.denominator
        return RationalNumber(numerator, denominator)

    def __sub__(self, obj):
        numerator = self.numerator * obj.denominator - obj.numerator * self.denominator
        denominator = self.denominator * obj.denominator
        return RationalNumber(numerator, denominator)

    def __mul__(self, obj):
        numerator = self.numerator * obj.numerator
        denominator = self.denominator * obj.denominator
        return RationalNumber(numerator, denominator)

    def __truediv__(self, obj):
        numerator = self.numerator * obj.denominator
        denominator = self.denominator * obj.numerator
        return RationalNumber(numerator, denominator)  
    
    def __lt__(self, obj):
        return True if (self.numerator / self.denominator) < (obj.numerator / obj.denominator) else False
    
    def __gt__(self, obj):
        return True if (self.numerator / self.denominator) > (obj.numerator / obj.denominator) else False

    def __eq__(self, obj):
        return True if (self.numerator / self.denominator) == (obj.numerator / obj.denominator) else False

# 6. Write exception hierarchy which defines a different exception for each of these error conditions (when creating RationalNumber objects):
class NotIntegerError(Exception):
    """Numerator or Denominator is not an integer"""
    def __init__(self):
        super().__init__("Numerator or Denominator is not an integer")

class ZeroDenominatorError(Exception):
    """Denominator must different 0"""
    def __init__(self):
        super().__init__("Denominator must different 0")