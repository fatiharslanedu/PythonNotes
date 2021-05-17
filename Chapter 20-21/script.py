
#? -------------------- Chapter 20: List ---------------------?#

#! = List is dynamic arrays.


import functools
from random import randrange
import collections
import itertools
import copy
from operator import itemgetter, attrgetter
import datetime
a = [1, 2, 3, 4, 5, 6, 7, 7]
b = [8, 9, 10]

a.extend(b)  # todo: [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
# todo: [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 1, 3, 5, 7, 9]
a.extend(range(1, 10, 2))
a.insert(3, 12)


class Person(object):
    def __init__(self, name, birthday, height):
        self.name = name
        self.birthday = birthday
        self.height = height

    def __repr__(self):
        return self.name


l = [
    Person("John Cena", datetime.date(1992, 9, 12), 175),
    Person("Chuck Norris", datetime.date(1990, 8, 28), 180),
    Person("Jon Skeet", datetime.date(1991, 7, 6), 185)
]

# todo: [Chuck Norris, John Cena, Jon Skeet]
l.sort(key=lambda item: item.name)
# todo: l: [Chuck Norris, Jon Skeet, John Cena]
l.sort(key=lambda item: item.birthday)
# todo: l: [John Cena, Chuck Norris, Jon Skeet]
l.sort(key=lambda item: item.height)
# print(l)

l = [{'name': 'John Cena', 'birthday': datetime.date(1992, 9, 12), 'size': {
    'height': 175, 'weight': 100}},
    {'name': 'Chuck Norris', 'birthday': datetime.date(
        1990, 8, 28), 'size': {'height': 180, 'weight': 90}},
    {'name': 'Jon Skeet', 'birthday': datetime.date(
        1991, 7, 6), 'size': {'height': 185, 'weight': 110}}]

l[1]['size']['weight']  # todo: 90

l.sort(key=lambda item: item['size']['height'])
# print(l)

# * Better way to sort using attrgetter and itemgetter


people = [{'name': 'chandan', 'age': 20, 'salary': 2000},
          {'name': 'chetan', 'age': 18, 'salary': 5000},
          {'name': 'guru', 'age': 30, 'salary': 3000}]

by_age = itemgetter('age')
by_salary = itemgetter('salary')

people.sort(key=by_age)
# print(people)
people.sort(key=by_salary, reverse=False)
# print(people)

list_of_tuples = [(1, 2), (3, 4), (5, 0)]
list_of_tuples.sort(key=itemgetter(1))  # todo: [(5, 0), (1, 2), (3, 4)]


persons = [Person("John Cena", datetime.date(1992, 9, 12), 175),
           Person("Chuck Norris", datetime.date(1990, 8, 28), 180),
           Person("Jon Skeet", datetime.date(1991, 7, 6), 185)]

# todo: [Chuck Norris, John Cena, Jon Skeet]
persons.sort(key=attrgetter('name'))
by_birthday = attrgetter('birthday')
persons.sort(key=by_birthday)  # todo: [Chuck Norris, Jon Skeet, John Cena]

b = ['blah'] * 4  # todo: ['blah', 'blah', 'blah', 'blah']

a = list(range(10))

del a[::3]  # todo: [1, 2, 4, 5, 7, 8]
del a[-1]

new_list = a[:]  # todo: copy#1

new_list = copy.copy(b)  # todo: copy#2
new_list = copy.deepcopy(a)  # todo: same object.

lst = [1, 2, 3, 4, 5]

lst[:3]  # todo : [1, 2, 3]
lst[::2]  # todo: [1, 3, 5]
lst[-1:0:-1]

# * Section 20.3: Checking if list is empty
lst = []
# if not lst:
#     print("list is empty.")


my_list = ['foo', 'bar', 'baz']

# for(index, item) in enumerate(my_list):
#     print(f"The item in position {index} is : {item}")


alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']

# for a, b in zip(alist, blist):
#     print(a, b)


alist = ['a1', 'a2', 'a3']
blist = ['b1']
clist = ['c1', 'c2', 'c3', 'c4']

# todo: Complete with None
# for a, b, c in itertools.zip_longest(alist, blist, clist):
#     print(a, b, c)

names = ["aixk", "duke", "edik", "tofp", "duke"]
list(set(names))  # todo: unique list

collections.OrderedDict.fromkeys(names).keys()
# print(names)

my_list = [None] * 10
my_list = ['test'] * 10
my_list = [{1}] * 10
# print(my_list)
# todo: [{1, 2}, {1, 2}, {1, 2}, {1, 2}, {1, 2}, {1, 2}, {1, 2}, {1, 2}, {1, 2}, {1, 2}]
my_list[0].add(2)
# print(my_list)

my_list = [{1} for _ in range(10)]
# print(my_list)  # todo: [{1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}]

#? -------------- Chapter 21: List comprehensions -------------?#

squares = [x * x for x in (1, 2, 3, 4)]  # todo: # squares: [1, 4, 9, 16]
# todo : # ['H', 'E', 'L', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']
[s.upper() for s in "Hello World"]
# todo: # ['these', 'words', 'mostly', 'have,commas']
[w.strip(",") for w in ['these,', 'words,,', 'mostly', 'have,commas,']]

sentence = "Beautiful is better than ugly."

w = ["".join(sorted(word, key=lambda x: x.lower()))
     for word in sentence.split()]
# todo: ['a', '*', '*', '*', 'e']
w = [x if x in 'aeiou' else '*' for x in 'apple']
# todo: [[1, 2], [3, 4], [0, 1]]
w = [sorted(x) for x in [[2, 1], [4, 3], [0, 1]]]


#todo : [3, 3, 2, 3, 2, 2, 6, 2, 2, 3]
w = [randrange(1, 7) for _ in range(10)]

#todo: [0, None, 2, None, 4, None, 6, None, 8, None]
w = [x if x % 2 == 0 else None for x in range(10)]

#todo: [1, -1, 5, -1, 9, -1, 13, -1, 17, -1]
w = [2 * (x if x % 2 == 0 else -1) + 1 for x in range(10)]

#todo: ['*', '*', 4, 6, 8]
w = [x if x > 2 else '*' for x in range(10) if x % 2 == 0]

#todo: ['*', '*', '*', '*', 4, '*', 6, '*', 8, '*']
w = [x if x > 2 and x % 2 == 0 else '*' for x in range(10)]


def f(x):
    import time
    time.sleep(.1)
    return x**2

# w = [f(x) for x in range(100) if f(x) > 10]


l = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]

w = functools.reduce(lambda x, y: x+y, l)
w = sum(l, [])

w = dict((x, x * x) for x in (1, 2, 3, 4))

w = {name: len(name)
     for name in ('Stack', 'Overflow', 'Exchange') if len(name) > 6}


my_dict = {1: 'a', 2: 'b', 3: 'c'}

swapped = {v: k for k, v in my_dict.items()}

data = [[1], [2, 3], [4, 5]]

output = [element for each_list in data
          if len(each_list) == 2
          for element in each_list
          if element != 5]  # todo: [2, 3, 4]

# * Generator Expressions

# for i in [x**2 for x in range(10)]:
#     print(i)

text = "When in the Course of human events it becomes necessary for one people..."
w = {ch.lower() for ch in text if ch.isalpha()}

# * Map brief

#! Usage 1
l = ['sat', 'bat', 'cat', 'mat']
# todo: [['s', 'a', 't'], ['b', 'a', 't'], ['c', 'a', 't'], ['m', 'a', 't']]
test = list(map(list, l))


def add(n):
    return n + n


#! Usage 2
numbers = [1, 2, 3, 4, 5]
result = list(map(add, numbers))  # todo: [2, 4, 6, 8, 10]

sum = (sum(
    1 for x in range(1000)
    if x % 2 == 0 and
    '9' in str(x)
)) #todo: 95

list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c', 'd']
list_3 = ['6', '7', '8', '9']

x = [(i, j, k) for i, j, k in zip(list_1, list_2, list_3)]
#todo: [(1, 'a', '6'), (2, 'b', '7'), (3, 'c', '8'), (4, 'd', '9')]
# print(x)