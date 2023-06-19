# 1. Write the decorator, let the user enter the user name, password, and give the user three chances before each execution of the decorated function. After the login is successful, the function can be accessed.
def Login(func):
    def Checker():
        username = "luong"
        password = "123"
        count = 0
        while count < 3 :
            usr = input("Please enter your username: ")
            pwd = input("Please enter your passowrd: ")
            if usr == username and pwd == password:
                func()
                return
            elif usr != username and pwd != password:
                print("Incorrect username and password")
            elif usr != username:
                print("Incorrect username")
            else:
                print("Incorrect password")
            count += 1
        print("Expired session")
    return Checker

@Login
def func():
    print("Login success")

# 2. Write a decorator to evaluate the execution time of a function
import time

def EvalExe(func):
    def Timer():
        start = time.time()
        func()
        finish = time.time()
        print(f"The execution time: {finish - start} seconds")
    return Timer

@EvalExe
def func_1():
    x = 12
    y = 15
    print(12 + 15)

# 3. Write a chain of function decorators (bold, italic, underline)
def bold(func):
    def adjust():
        text = func()
        text = f"bold {text}"
        print(text)
        return text 
    return adjust

def italic(func):
    def adjust():
        text = func()
        text = f"italic {text}"
        print(text)
        return text
    return adjust 

def underline(func):
    def adjust():
        text = func()
        text = f"underline {text}"
        print(text)
        return text
    return adjust 

@underline
@italic
@bold
def func_2():
    text = "Hello guys"
    return text

# 4. Write decor1 and decor2 decorators to make num_a() and num_b() run correctly
def decor1(func):
    def Caculs():
        num = func()
        return num ** 2
    return Caculs
    
def decor2(func):
    def Caculs():
        num = func()
        return num * 2
    return Caculs

@decor1
@decor2
def num_a():
    return 10

@decor2
@decor1
def num_b():
    return 10