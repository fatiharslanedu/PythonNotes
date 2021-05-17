
#* ----------------- Section 1.5: Collection Types -----------------*#

import keyword

"""
    ['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""
# print(keyword.kwlist) #TODO: print above.

# a = 2 + 1j #todo: complex numbers

b = ('a', 1, 'python', (1, 2))  # * hashable = karma
# b[2] = 'JAVA' #todo: typeError

a = 'hello'

# print(list(a)) #todo: ['h', 'e', 'l', 'l', 'o']
# print(set(a)) #todo: {'e', 'o', 'h', 'l'} inordered (hashable) and unique.
# print(tuple(a)) #todo: ('h', 'e', 'l', 'l', 'o')

# ? Add a new element to list at a speciﬁc index. L.insert(index, object)
names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
names.insert(1, "Nikki")
# print(names)

a = [1, 1, 1, 2, 3, 4]
a.count(1)

# print(a[::-1]) #todo: reverse order

# * Tuple: Fixed-length, immutable for security

ip_address = ('10.20.30.40', 8080)

# * Dictionaries

state_capitals = {
    'Arkansas': 'Little Rock',
    'Colorado': 'Denver',
    'California': 'Sacramento',
    'Georgia': 'Atlanta'
}

# for k in state_capitals.keys():
#     print('{} is the capital of {}'.format(state_capitals[k], k))

# * Set: no repeat, no insertion (yerleştirme) and sorted order.

first_names = {'Adam', 'Beth', 'Charlie'}

# * Defaultdict

from collections import defaultdict

state_capitals = defaultdict(lambda: 'Boston') #todo: default statement for dict.

state_capitals['Arkansas'] = 'Little Rock'
state_capitals['California'] = 'Sacramento'
state_capitals['Colorado'] = 'Denver'
state_capitals['Georgia'] = 'Atlanta'

# print(state_capitals['Alabama'])

#* ----------  Section 1.8: Built in Modules and Functions -----------*#

# print(dir(__builtins__)) #todo: all puilt in functions.

# help(max)

import helloWorld

# print(helloWorld.__doc__) #todo: Access the global file doc.


#* ------------- Section 1.11: String function - str() and repr() ----------#

s = """w'o"w"""
# print(repr(s)) #todo: 'w\'o"w'
# print(str(s)) #todo: w'o"w
# # eval(str(s)) #todo: syntax error
# eval(repr(s)) #todo: true

import datetime
today = datetime.datetime.now() 
# print(str(today)) #todo: 2021-04-25 16:44:12.551159
# print(repr(today)) #todo: datetime.datetime(2021, 4, 25, 16, 44, 30, 952587)

class Represent(object):
    
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __repr__(self):
        return "Represent(x={},y=\"{}\")".format(self.x, self.y)
    
    def __str__(self):
        return "Representing x as {} and y as {}".format(self.x, self.y)

r = Represent(1, "Hopper")
# print(r) #todo: prints __str__
# print(r.__repr__) #todo: prints __repr__: '<bound method Represent.__repr__ of Represent(x=1,y="Hopper")>'
# rep = r.__repr__() #todo: sets the execution of __repr__ to a new variable
# print(rep) #todo: prints 'Represent(x=1,y="Hopper")'
# r2 = eval(rep) #todo: evaluates rep
# print(r2) #todo: prints __str__ from new object
# print(r2 == r) #todo: prints 'False' because they are different objects