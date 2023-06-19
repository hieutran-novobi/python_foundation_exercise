# 1. Write fibonacciGenerator() to create a generator, which generates Fibonacci number series value (infinite size)
def fibonacciGenerator():
    num_1 = 0
    num_2 = 0
    count = 0
    while True:
        if count == 0 :
            num_1 = 0
            num_2 = 1
            count += 1
        else:
            temp = num_2
            num_2 = num_1 + num_2
            num_1 = temp
        yield num_2

# 2. Write multipleBy(n) to create a generator, which generates n times greater than values from 1 to 100
def multipleBy(n):
    num = n
    count = 1
    result = n
    while result >= 1 and result <= 100 :
        yield result
        result = count * num
        count += 1

# 3. Write exponentialBy(n) to create a generator, which generates values to the power of n from 1 to 100
def exponentialBy(n):
    num = n
    count = 1
    result = 1
    while result >= 1 and result <= 100 :
        yield result
        result = count ** num
        count += 1



