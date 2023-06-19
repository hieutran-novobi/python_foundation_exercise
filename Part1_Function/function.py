# 1. Write a function to check whether a passed string is a palindrome or not
def CheckPal(str_):
    i = 0
    j = len(str_) - 1
    while i < j :
        if str_[i] != str_[j]:
            return False
        i += 1
        j -= 1
    return True


# 2. Write a function that accept two parameters: a list of integers lst and an integer n 
#    and return the list of lists where each list stores elements that have the same remainder after the division with n
def NestList(lst, n):
    result = {}
    for item in lst:
        remain = item % n
        if remain in result:
            result[remain] += [item]
        else: 
            result[remain] = [item]

    return list(result.values())

# 3. Write a Python function to split a string into a list of words
def SplitStr(str_):
    return str_.split(' ')

# 4. Write a function with variable length of arguments and calculate the total
def sum(*arg):
    result = 0
    for ele in arg:
        result += ele
    return result

# 5. Write a function that accept the employee's name and return basic information
def initialize_employee(name = "", gender = "", salary = ""):
    return {"name": name, "gender": gender, "salary": salary}
