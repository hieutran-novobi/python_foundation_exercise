from itertools import *
'''
1
'''


'''
2
'''


def exercise_2(lst_1, lst_2):
    return list(chain.from_iterable([item if isinstance(item, list) else [item] for item in lst_1 + lst_2]))
# print(exercise_2(lst_1=[["We", "are"], "Novobi"], lst_2= ["We", ["are", "Novobi"]]))




'''
3
'''


def exercise_3(lst):
    return [f"{item[0]} - {item[1]}" for item in list(combinations(lst, 2))]

# print(exercise_3(["Red", "Yellow", "Green"]))


'''
4
'''


def exercise_4(*args):
    return list(chain(*args))


# print(exercise_4([1, 4, 7, 10, 13, 16], [2, 5, 8, 11, 14, 17], [3, 6, 9, 12, 15, 18]))

'''
5
'''
def exercise_5(lst):
    groups = {}
    for key, group in groupby(sorted(lst, key=len), len):
        groups[key] = list(group)
    for key, group in groups.items():
        print(f"Key: {key} - Group: {group}")
        
# exercise_5(["keep", "smiling", "because", "life", "is", "a", "beautiful", "thing", "and", "there", "is", "so", "much", "to", "smile", "about"])
