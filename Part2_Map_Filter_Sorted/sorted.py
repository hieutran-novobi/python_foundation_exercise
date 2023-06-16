'''
1
'''
def descending_order(lst: list)->list:
    '''
    Use sorted function to sort elements in the list in descending order
    '''
    return list(sorted(lst, reverse=True))

# print(descending_order([5, 7, 8, -1, 0, -4, -2, 3, 1]))

'''
2
'''
def reverse_order(lst: list)->list:
    '''
    Use sorted function to reverse the order of elements in a list
    '''
    lst.reverse()
    return lst

# print(reverse_order([5, 7, 8, -1, 0, -4, -2, 3, 1]))