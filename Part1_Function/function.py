
## 1. Write a function to check whether a passed string is a palindrome or not
def palindrome(s: str) -> bool:
    for i in range(int(len(s)/2)):
        if(s[i] != s[len(s)-1-i]):
            return False
    return True
# print(palindrome('banana'))

''' 
2.
'''
def filter_integer_division(lst: list, n: int) -> list:
    '''
    A function that accept two parameters: a list of integers **lst** and an integer **n**
    and return the list of lists where each list stores elements that have the same remainder after the division with n
    '''
    remainder_dict = {}
    for num in lst:
        remainder = num % n
        if remainder in remainder_dict:
            remainder_dict[remainder].append(num)
        else:
            remainder_dict[remainder] = [num]
    return list(remainder_dict.values())

# print(filter_integer_division([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))


'''
3.
'''
def split_words(s: str) -> list:
    '''
    A function to split a string into a list of words
    '''
    return s.split()


'''
4. 
'''
def sum_of_list(*nums: int) -> dict:
    '''
    A function with variable length of arguments and calculate the total
    '''
    return sum([num for num in nums])
# print(sum_of_list(10,20,30))

'''
5. Write a function that accept the employee's name and return basic information
'''
    