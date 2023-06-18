'''
1
'''
def exercise_1(lst_1, lst_2):
    '''
    Concatenate two lists index-wise:
    '''
    return list(map(lambda x: x[0] + x[1], zip(lst_1, lst_2)))

# print(concat_list(lst_1 = ["W", "a", "Novo"], lst_2 = ["e", "re", "bi"]))

'''
2
'''
def exercise_2(lst_1, lst_2):
    '''
    Concatenate two lists in the following order:
    '''
    return [ s1 + ' ' + s2 for s1 in lst_1 for s2 in lst_2]

# print(concat_odered_list(lst_1 = ["Hello", "World"], lst_2 = ["Dear", "Sir"]))

'''
3
'''
def exercise_3(lst_1: list, lst_2: list): 
    lst_2.reverse()
    return [(item[0], item[1]) for item in zip(lst_1, lst_2)]
# print(exercise_3(lst_1 = [10, 20, 30], lst_2 = [100, 200, 300]))

'''
4
'''
def exercise_4(lst_1):
    return list(filter(lambda x: True if x != "" else False, lst_1))

# print(exercise_4(["10", "20", "30", "", "40"]))

'''
5
'''
def exercise_5(lst):
    return [x for x in lst if x != "20"]
# print(exercise_5(["10", "20", "30", "40", "20", "50"]))  # Output: [10, 30, 40, 50]

'''
6
'''
def exercise_6(lst: list[dict]) -> list[dict]:
    # max_dict = max(lst, key=len)
    # for item in max_dict.keys():
    return sorted(lst, key=lambda x: x['model'], reverse=True)
        

print(exercise_6( [ {"make": "Nokia", "model": 216, "color": "Black"}, {"make": "Mi Max", "model": 2, "color": "Gold"}, {"make": "Samsung", "model": 7, "color": "Blue"} ]  ))
