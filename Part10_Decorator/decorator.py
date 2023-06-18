import time

'''
2
'''
def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds.")
        return result
    return wrapper

@time_it
def mesure():
    time.sleep(2)
    print("Function executed!")
    
# mesure()

'''
1
'''
def login_required(func):
    @time_it
    def wrapper(*args, **kwargs):
        for i in range(3):
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username == "admin" and password == "admin":
                print("Login successful!")
                return func(*args, **kwargs)
            else:
                print("Invalid username or password. Please try again.")
        print("Maximum number of login attempts exceeded.")
    return wrapper

'''
execute for exercise 1
'''
@login_required
def login():
    print("After run")

login()



'''
3
'''

def bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

def underline(func):
    def wrapper(*args, **kwargs):
        return f"<u>{func(*args, **kwargs)}</u>"
    return wrapper

@bold
@italic
@underline
def my_function(text):
    return text

print(my_function("Hello, world!"))


def decor1(func):
    def wrapper():
        x = func()
        return x * x
    return wrapper

def decor2(func):
    def wrapper():
        x = func()
        return 2 * x
    return wrapper

@decor1
@decor2
def num_a():
    return 10

@decor2
@decor1
def num_b():
    return 10

print(num_a())  # Output: 400
print(num_b())  # Output: 200