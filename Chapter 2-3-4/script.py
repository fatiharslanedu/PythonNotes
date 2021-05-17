
# * Chapter 2: Python Data Types

#? ----------------- Section 2.2: Set Data Types -------------------?#

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket) #todo: {'orange', 'pear', 'banana', 'apple'}

a = set('abracadabra')
# print(a) #todo: {'r', 'c', 'd', 'a', 'b'}

b = frozenset('asdfagsa')
# print(b) #todo: frozenset({'d', 'g', 's', 'a', 'f'})

cities = frozenset(["Frankfurt", "Basel","Freiburg"])
# print(cities) #todo: frozenset({'Frankfurt', 'Basel', 'Freiburg'})

dic = {'name':'red', 'age':10}
# print(dic['name'])
# print(dic.values()) #todo: dict_values(['red', 10])
# print(dic.keys()) #todo: dict_keys(['name', 'age'])

#? ------- Section 4.2: Programmatically accessing docstring ---------?#

def func():
    """This function doing nothing."""
    pass

# help(func) #todo: return "This function doing nothing."

def greet(name, greeting="Hello"):
    """Print a greeting to the user `name` 
    Optional parameter `greeting` can change what they're greeted with."""
    print("{} {}".format(greeting, name))

# help(greet)

#* Google Python Style Guide

def hello(name, language="en"):
    """Say hello to a person.
Args:
    name: the name of the person as string
    language: the language code string
Returns:
    A number.
"""
    print(greeting[language]+" "+name)
    return 4