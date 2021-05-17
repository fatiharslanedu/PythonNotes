
#? -------- Section 15.6: Comparing Objects ----------?#

import itertools
from collections import OrderedDict
from collections import defaultdict
from array import *


class Foo(object):
    def __init__(self, item):
        self.my_item = item

    def __eq__(self, other):
        return self.my_item == other.my_item


a = Foo(5)
b = Foo(5)

# print(a==b) #todo: True
# print(a!=b) #todo: False
# print(a is b) #todo: False

#? ---------------- Chapter 17: Arrays ------------------?#


my_array = array('i', [1, 2, 3, 4, 5])
# my_array.insert(0,0)
# print(my_array)

#? --------------- Chapter 19: Dictionary ----------------?#


mydict = {}
mydict.setdefault('foo', 'bar')

d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     print(key, d[key]) #todo: a 1, b 2, c 3


d = defaultdict(int)
d['key']  # todo: 0
d['key'] = 5  # todo: 5

d = defaultdict(lambda: 'empty')

# * Section 19.5: Merging dictionaries

fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}

fishdog = {**fish, **dog}
# print(fishdog) #todo: {'name': 'Clifford', 'hands': 'paws', 'special': 'gills', 'color': 'red'}


d = OrderedDict()
d['first'] = 1
d['second'] = 2
d['third'] = 3
d['last'] = 4

# * Section 19.10: Unpacking dictionaries using the ** operator


def parrot(voltage, state, action):
    print("This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# parrot(**d)

# * Section 19.14: All combinations of dictionary values


options = {
    "x": ["a", "b"],
    "y": [10, 20, 30]}

keys = options.keys()
values = (options[key] for key in keys)
combinations = [dict(zip(keys, combination)) for combination in itertools.product(*values)]
# print(combinations)

#* Zip 

name = ["Gurmeet Singh","Amandeep Singh","Simrandeep Kaur","Manmeet Singh"]
age = [21,12,10,9]
score = [99,80,85]

#todo: Zipped iteration
#todo: ('Gurmeet Singh', 21, 99) 
#todo: ('Amandeep Singh', 12, 80)
#todo: ('Simrandeep Kaur', 10, 85)
# for one in zip(name, age, score):
#     print(one)

#todo: Another Type of Zipped Iteration
# for name, age, score in zip(name, age, score):
#     #todo: Gurmeet Singh is aged 21 and scored 99.
#     #todo: Amandeep Singh is aged 12 and scored 80.
#     #todo: Simrandeep Kaur is aged 10 and scored 85.
#     print(name + " is aged " + str(age)+ " and scored "+ str(score)+".") 