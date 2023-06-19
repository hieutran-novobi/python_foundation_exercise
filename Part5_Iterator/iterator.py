# 1. Instead of using enumerate function, create your own class.....
class Enumerate:
    def __init__(self, lst, start = 0):
        self.lst = lst
        self.start = start
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        len_ = len(self.lst)
        if self.count < len_:
            result = (self.start,self.lst[self.count])
            self.start += 1
            self.count += 1
            return result
        else:
            raise StopIteration      

# 2. Instead of using zip function, create your own class ...
class Zip:
    def __init__(self, *lst):
        self.lsts = lst
        self.count = 0
        self.len = min(list(map(lambda ele: len(ele), lst)))
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.len:
            result = tuple(ele[self.count] for ele in self.lsts)
            self.count += 1
            return result
        else:
            raise StopIteration

