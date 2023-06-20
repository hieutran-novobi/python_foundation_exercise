'''
1
'''
def get_positive_number(lst: list)->list:
    '''
    Use filter function to get the list of positive numbers
    '''
    return list(filter(lambda x: x > 0, lst))
# print(get_positive_number([4,-3, 2]))

'''
2
'''
def list_of_capital_word(lst: list)->list:
    return list(filter(lambda s: s[0].isupper(), lst))

# print(list_of_capital_word(["We", "are", "Novobi"]))

'''
3
'''
def missed_key(lst: list)-> list:
    return list(filter(lambda x: False if 'a' in x else True, lst))

# print(missed_key([{"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5}, {"a": 2, "c": 6}, {"b": 4, "c": 5}]))


