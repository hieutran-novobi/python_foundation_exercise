# 1. Use partial function from `functools` module to rewrite `doubleNum()` and `tripleNum()` methods
from functools import partial

def multiply(x, y):
    return x * y

def doubleNum(x):
    func = partial(multiply, y = 2)
    return func(x)

def tripleNum(x):
    func = partial(multiply, y = 3)
    return func(x)

print(tripleNum(3))