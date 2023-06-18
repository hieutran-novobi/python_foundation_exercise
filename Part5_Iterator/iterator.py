'''
1
'''
class Enumerate:
    def __init__(self, iterable, start = 0):
        self.iterable = iterable
        self.index = 0
        self.count = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.iterable):
            raise StopIteration
        result = (self.count, self.iterable[self.index])
        self.index += 1
        self.count += 1
        return result
    
# temp = Enumerate(["a", "b", "c"], start=2)
# enum_iter = iter(temp)
# print(next(enum_iter)) 
# print(next(enum_iter))
# print(next(enum_iter)) 
# print(next(enum_iter))
# print(next(enum_iter))
'''
2
'''
class Zip:
    def __init__(self, *args):
        self.lists = [list(x) for x in args]

    def __iter__(self):
        min_length = min([len(x) for x in self.lists])
        iterators = [iter(x) for x in self.lists]
        return iter([tuple(next(x) for x in iterators) for _ in range(min_length)])
    def __next___(self):
        try:
            result = tuple(next(x) for x in self.iterators)
        except StopIteration:
            raise StopIteration
        return result
    
# zip_obj = Zip(["a", "b", "c"], [1, 2, 3, 4], ["x", "y", "z"])
# zip_iter = iter(zip_obj)
# print(next(zip_iter))
# print(next(zip_iter))
# print(next(zip_iter))
# print(next(zip_iter))
        
        
