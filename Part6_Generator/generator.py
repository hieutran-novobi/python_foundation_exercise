'''
1
'''
import math

def fibonacciGenerator():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

# fibonacci = fibonacciGenerator()
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))
# print(next(fibonacci))


'''
2
'''


def multipleBy(n):
    for i in range(1, 100):
        yield i * n


multiply = multipleBy(5)
print(next(multiply))

def exponentialBy(n):
    for i in range(1, 100):
        yield int(math.pow(i, n))
        
exponential = exponentialBy(3)
print(next(exponential))
print(next(exponential))
print(next(exponential))
print(next(exponential))