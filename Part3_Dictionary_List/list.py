# 1. Concatenate two lists index-wise:
def ConIndex(lst_1, lst_2):
    len_ = len(lst_1)
    return [lst_1[i] + lst_2[i] for i in range(0, len_)]

# 2. Concatenate two lists in the following order:
def ConIndex(lst_1, lst_2):
    len_1 = len(lst_1)
    len_2 = len(lst_2)
    return [lst_1[i] + " " + lst_2[j] for i in range(0, len_1) for j in range(0, len_2)]

# 3. Iterate both lists simultaneously such that lst_1 should display item in original order and lst_2 in reverse order:
def SimulRevers(lst_1, lst_2):
    len_ = len(lst_1)
    return [(lst_1[i], lst_2[len_ - 1 - i]) for i in range(0, len_)]

# 4. Remove empty strings from the list of strings by using filter function:
def RemoveEmpt(lst):
    return list(filter(lambda item: len(item) > 0, lst))

# 5. Remove all occurrence of 20 from the list by using list comprehension:
def RemoveOccur(lst):
    return [item for item in lst if item != "20"]

# 6. Sort a list of dictionaries
def SortLst(lst, ksort = "color"):
    return sorted(lst, key = lambda ele: ele[ksort])

print(SortLst([ {"make": "Nokia", "model": 216, "color": "Black"}, {"make": "Mi Max", "model": 2, "color": "Gold"}, {"make": "Samsung", "model": 7, "color": "Blue"} ]))