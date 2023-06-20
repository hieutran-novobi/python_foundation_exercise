'''
1
'''
def data_typ_conversion(lst: list) -> list:
    '''
    Using map function for data type conversion:
    '''
    return list(map(int, lst))

# print(data_typ_conversion([10.8932, 12.434,13.6556]))

'''
2
'''
def square_list(lst: list)  -> list:
    '''
    Using map function to square the elements of a list Check multiple keys exists in a dictionary:
    '''
    return list(map(lambda x: x*x, lst))

# print(square_list([2,4,6]))

'''
3
'''
def count_same_pair(lst1: list, lst2: list) -> int: 
    '''
    Using map function to square the elements of a list Check multiple keys exists in a dictionary:
    '''
    return sum(map(lambda x: x[0] == x[1], zip(lst1, lst2)))

# print(count_same_pair( [1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9], [1, 2, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8]))



