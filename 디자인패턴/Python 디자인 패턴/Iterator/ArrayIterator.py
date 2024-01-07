from Iterator import Iterator
from Aggregator import Aggregator
from My_Item import My_Item

class Array(Aggregator):
    items = []
    
    def __init__(self, items:list)->None: 
        self.items = items
    
    def getItem(self, idx:int)->My_Item:
        return self.items[idx]
    
    def getCount(self):
        return len(self.items)
    
    def iterator(self):
        return ArrayIterator(self)
    pass

class ArrayIterator(Iterator):
    def __init__(self, array:Array):
        self.array = array
        self.index = -1

    def next(self)->bool:
        self.index+=1
        return self.index < self.array.getCount()

    def current(self)->None:
        return self.array.getItem(self.index)
    pass