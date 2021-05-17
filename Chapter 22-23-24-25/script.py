
#? ------ Chapter 22: List slicing (selecting parts of lists) --------?#

lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

lst[::2]  # todo: ['a', 'c', 'e', 'g']
lst[::3]  # todo: ['a', 'd', 'g']


def shift_list(array, s):
    """Shifts the elements of a list to the left or right.

    Args:
        array - the list to shift
        s - the amount to shift the list ('+': right-shift, '-': left-shift)

    Returns:
        shifted_array - the shifted list
        """

    # * calculate actual shift amount (e.g., 11 --> 1 if length of the array is 5)
    s %= len(array)
    # * reverse the shift direction to be more intuitive
    s *= -1
    # * shift array with list slicing
    shifted_array = array[s:] + array[:s]
    return shifted_array


my_array = [1, 2, 3, 4, 5]

# print(shift_list(my_array, -7)) #todo: [3, 4, 5, 1, 2]
# print(shift_list(my_array, 2)) #todo: [4, 5, 1, 2, 3]

#? -------------------------- Chapter 23: groupby() --------------------?#
from itertools import groupby
things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), \
          ("vehicle", "harley"), ("vehicle", "speed boat"), ("vehicle", "school bus")]

dic = {}
f = lambda x : x[0]

for key, group in groupby(sorted(things, key = f), f):
    dic[key] = list(group)
"""
{'animal': [('animal', 'bear'), ('animal', 'duck')], 
'plant': [('plant', 'cactus')], 
'vehicle': [('vehicle', 'harley'), ('vehicle', 'speed boat'), ('vehicle', 'school bus')]}
"""


c = groupby(['goat', 'dog', 'cow', 1, 1, 2, 3, 11, 10, ('persons', 'man', 'woman')])
dic = {}

for k, v in c:
    dic[k] = list(v)

"""
    {'goat': ['goat'], 'dog': ['dog'], 'cow': ['cow'], 
    1: [1, 1], 2: [2], 3: [3], 11: [11], 10: [10], 
    ('persons', 'man', 'woman'): [('persons', 'man', 'woman')]}
"""

#? ------------------- Chapter 24: Linked lists -----------------?#

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, val):
        self.data = val

    def setNext(self, val):
        self.next = val

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        """Check if the list is empty."""
        return self.head is None

    def add(self, item):
        """Add the item to the list"""
        new_node = Node(item)
        new_node.setNext(self.head)
        self.head = new_node

    def size(self):
        """Return the length / size of the list. """
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.getNext()

        return count

    def search(self, item):
        """Search for item in list. If found, return True. Otherwise False."""
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() is item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        """Remove item from list. If item is not found in list, return ValueError."""
        current = self.head
        previous = None
        found = False

        while current is not None and not found:
            if current.getData() is item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if found:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        else:
            raise ValueError
            print("Value not found.")

    def insert(self, position, item):
        """ 
            Insert item at position specified. If position specified is 
            out of bounds, raise ValueError.
        """

        if position > self.size() - 1:
            raise ValueError
            print("Index out of bounds.")

        current = self.head
        previous = None
        pos = 0

        if position is 0:
            self.add(item)
        else:
            new_node = Node(item)
            while pos < position:
                pos += 1
                previous = current
                current = current.getNext()
            previous.setNext(new_node)
            new_node.setNext(current)

    def index(self, item):
        """
            Return the index where item is found.
            If item is not found, return None.
        """
        current = self.head
        pos = 0
        found = False
        while current is not None and not found:
            if current.getData() is item:
                found = True
            else:
                current = current.getNext()
                pos += 1

        if found:
            pass
        else:
            pos = None
        return pos

    def pop(self, position = None):
        """
            If no argument is provided, return and remove the item at the head.
            If position is provided, return and remove item at that position.
            If index is out of bounds, raise ValueError
        """

        if position > self.size():
            print("Index out of bounds.")
            raise ValueError

        current = self.head
        if position is None:
            ret = current.getData()
            self.head = current.getNext()
        else:
            pos = 0
            previous = None
            while pos < position:
                previous = current
                current = current.getNext()
                pos += 1
                ret = current.getData()
            previous.setNext(current.getNext())
        print(ret)
        return ret
            
    def append(self, item):
        """Append item to the end of the list."""
        current = self.head
        previous = None
        pos = 0
        length = self.size()
        while pos < length:
            previous = current
            current = current.getNext()
            pos += 1            
        new_node = Node(item)
        if previous is None:
            new_node.setNext(current)
            self.head = new_node
        else:
            previous.setNext(new_node)


    def printList(self):
        """Print the list."""
        current = self.head
        while current is not None:
            print (current.getData())
            current = current.getNext()


l = LinkedList()
l.add('e')
l.add('d')
l.add('c')
l.add('b')
l.add('a')
l.insert(3,'e')
l.append('f')
# l.printList()

#? ---------------------------- Chapter 25: Linked List Node -------------------?#

class Node:
    def __init__(self, cargo=None, next=None):
        self.car = cargo
        self.cdr = next

    def __str__(self):
        return str(self.car)

    def display(lst):
        if lst:
            w("%s" % list)
            display(lst.cdr)
        else:
            w("nil\n")

