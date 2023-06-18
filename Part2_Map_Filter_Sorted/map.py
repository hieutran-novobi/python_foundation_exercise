# 1. Using map function for data type conversion
def conversion(lst):
    return list(map(lambda ele: int(ele), lst))


# 2. Using map function to square the elements of a list Check multiple keys exists in a dictionary
def SquareList(lst):
    return list(map(lambda ele: ele * ele, lst))


# 3. Using map function to count the same pair in two given lists
def CountPair(lst_1, lst_2):
    return sum(list(map(lambda e1, e2: 1 if e1 == e2 else 0, lst_1, lst_2)))


