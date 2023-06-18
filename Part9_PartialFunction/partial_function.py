from functools import partial

def multiply(x, y):
    return x * y

doubleNum = partial(multiply, y =2)
tripleNum = partial(multiply, 3)

print(doubleNum(4))
print(tripleNum(3))