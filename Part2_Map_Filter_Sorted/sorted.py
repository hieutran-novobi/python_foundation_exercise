# 1. Use sorted function to sort elements in the list in descending order
def DescOrder(lst):
    return sorted(lst, reverse = True)


# 2. Use sorted function to reverse the order of elements in a list
count = 0

def Counting(ele):
    global count 
    count += 1
    return count 

def ReverseOrder(lst):
    return sorted(lst, key = Counting, reverse = True)
