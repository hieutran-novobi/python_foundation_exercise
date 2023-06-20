'''
6
'''
class IntegerError(Exception):
    def __init__(self) -> None:
        super().__init__("Error: Numerator or Denominator is not an integer")

class ZeroDenominatorError(Exception):
    def __init__(self):
        super().__init__("Error: Denominator must not be zero.")

'''
5, 6
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
class RationalNumber:
    def __init__(self, numerator, denominator = 1)->None:
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise IntegerError()
        if denominator == 0:
            raise ZeroDenominatorError()
        self.numerator = numerator
        self.denominator = denominator
    def simplify(self):
        temp = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator/temp
        self.denominator = self.denominator/temp
    
    def __str__(self):
        return f"{int(self.numerator)}/{int(self.denominator)}"
    
    def __add__(self, other):
        temp = RationalNumber(self.numerator*other.denominator + other.numerator*self.denominator, self.denominator*other.denominator)
        temp.simplify()
        return temp
    
    def __sub__(self, other):
        temp = RationalNumber(self.numerator*other.denominator - other.numerator*self.denominator, self.denominator*other.denominator)
        temp.simplify()
        return temp      
    
    def __mul__(self, other):
        temp = RationalNumber(self.numerator * other.numerator, self.denominator*other.denominator)
        temp.simplify()
        return temp
    
    def __truediv__(self, other):
        temp = RationalNumber(self.numerator * other.denominator, self.denominator*other.numerator)
        temp.simplify()
        return temp
    
    def __lt__(self, other):
        print(self.numerator*other.denominator)
        print(other.numerator*self.denominator)
        return True if (self.numerator*other.denominator < other.numerator*self.denominator) else False
    def __gt__(self, other):
        return True if (self.numerator*other.denominator > other.numerator*self.denominator) else False
    def __eq__(self, other): 
        return True if (self.numerator*other.denominator == other.numerator*self.denominator) else False

# temp = RationalNumber(2,3)
# temp1 = RationalNumber(4,6)
# temp2 = temp / temp1
# print(temp1 == temp)        
        
    
    
# temp = RationalNumber(2,3)
# print(temp.simplify())
        

# temp = RationalNumber(-9.5, 3)