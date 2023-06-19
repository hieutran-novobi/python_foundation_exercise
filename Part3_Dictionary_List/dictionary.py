# 1. Map two lists into a dictionary:
def MapDic(lst_1, lst_2):
    lenL = len(lst_1)
    result = {}
    for i in range(0, lenL):
        result[lst_1[i]] = lst_2[i]
    return result

# 2. Check multiple keys exists in a dictionary:
def Check(dic, lst):
    rs = [key for key in lst if key in dic]
    return True if len(rs) == len(lst) else False

# 3. Remove a key from a dictionary:
def Remove(dic, key):
    try:
        dic.pop(key)       
    except:
        print("Invalid key")
    return dic

# 4. Concatenate dictionaries to create a new one
def ConDic(*arg):
    result = {}
    for dic in arg:
        result.update(dic)
    return result

# 5. Count number of items in a dictionary that value is a list
def CountNum(lst):
    count = 0
    for value in lst.values():
        if type(value) is list: count += len(value)
    return count


# 6. Group elements of a list based on its length:
def GroupLst(lst):
    result = {}
    for item in lst:
        len_ = len(item)
        if len_ not in result.keys():
            result[len_] = [item]
        else:
            result[len_] += [item] 
    return result
