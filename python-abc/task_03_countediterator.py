#!/usr/bin/python3

""" Module that contains the CountedIterator class that extends
    the Iter function by adjusted the method __next__
"""


class CountedIterator:
    """
    Class CountedIterator the extends the functionality of 
    the Iter() function overriding the __next__ method

    Methods:
        __extend__ : standard behaviour plus incrementing
        a counter each time an item is fetched.
    """
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        return (self.counter)
    
    def __next__(self):
        try:
            item = next(self.iterator)
        except StopIteration as e:
            raise StopIteration("That was the last item on the Iterable") from e
        self.counter += 1
        return item
        
