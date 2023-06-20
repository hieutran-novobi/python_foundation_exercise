'''
1
'''
def map_dict(keys: list, values: list)->dict:
    '''
    Use sorted function to sort elements in the list in descending order
    '''
    return dict(list(zip(keys, values)))

# print(map_dict(["key_1", "key_2", "key_3"], ["value_1", "value_2", "value_3"]))

'''
2
'''
def check_keys_exist(dict, lst):
    for item in lst:
        if not(item in dict):
            return False
    return True
    
def is_multiple_keys_exists(dict: dict, lst1: list, lst2: list):
    '''
    Check multiple keys exists in a dictionary:
    '''
    print('Check lst_1 => ',check_keys_exist(dict, lst1))
    print('Check lst_1 => ',check_keys_exist(dict, lst2))
    
# is_multiple_keys_exists({"key_1": "value_1", "key_2": "value_2", "key_3": "value_3"}, ["key_1", "key_4"], ["key_2", "key_3"] )

'''
3
'''
def remove_key(dict: dict, key) -> dict:
    '''
    Remove a key from a dictionary:
    '''
    try:
        dict.pop(key)
    except:
        print('dict do not have this key, return original dict')
        return dict
    return dict
    
# print(remove_key({"key_1": "value_1", "key_2": "value_2", "key_3": "value_3"},"key_5"))

'''
4
'''
def concat_dicts(*dict)->dict:
    '''
    Concatenate dictionaries to create a new one
    '''
    ans = {}
    for item in dict:
        ans.update(item)
    return ans
# print(concat_dicts({1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50, 6: 60}))

'''
5
'''
def count_list_item(dict: dict)->int:
    '''
    Count number of items in a dictionary that value is a list
    '''
    return sum(map(lambda x: len(x[1])  if isinstance(x[1], list) else 0, dict.items()))
# print(count_list_item({"key_1": ["value_1", "value_2"], "key_2": ["value_3", "value_4", "value_5"]}))    

