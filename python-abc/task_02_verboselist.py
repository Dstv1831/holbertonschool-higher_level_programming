#!/usr/bin/python3

""" Module that contains a class that extends
    the Python "list" class by introducing a notification 
    message when items ar added or deleted
"""


class VerboseList(list):
    """
    Class VerboseList that will overwrite the methods append, extend, remove and pop

    Methods:
        append: After adding the item to the list,
        print a message like “Added [item] to the list.”
        extend: After extending the list,
        print a message like “Extended the list with [x] items.
        remove: Before removing the item from the list,
        print a message like “Removed [item] from the list.
        pop: Before popping the item from the list,
        print a message like “Popped [item] from the list.
    """
    # The constructor __init__ is unnecessary since list already initializes itself.
    # def __init__(self):
    #     super().__init__()

    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list")

    def extend(self, new_vector):
        x = len(new_vector)
        super().extend(new_vector)
        print(f"Extended the list with {x} items")
        
    def remove(self, item):
        print(f"Removed {item} from the list")
        super().remove(item)
        

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"Popped {item} from the list")
