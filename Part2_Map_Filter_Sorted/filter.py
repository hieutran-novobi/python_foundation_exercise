# 1. Use filter function to get the list of positive numbers
def GetPos(lst):
    return list(filter(lambda ele: ele > 0, lst))

# 2. Using filter function to get the list of words having the first letter is capital
def FstLetter(lst):
    return list(filter(lambda ele: ele[0] >= 'A' and ele[0] <='Z', lst))

# 3. Using filter function to get the list of dictionaries missing the key a
def MissKey(lst):
    return list(filter(lambda ele: "a" not in ele.keys(), lst))
