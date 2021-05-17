
#? ------------ Section 7.1: Creating an enum (Python 2.4 through 3.3) --------?#

from enum import Enum

class Color(Enum):
    red = 1
    green = 2
    blue = 3

# print(Color.red)    #todo: Color.red
# print(Color(1))#todo: Color.red
# print(Color['red'])#todo: Color.red

# print([c for c in Color])#todo: [<Color.red: 1>, <Color.green: 2>, <Color.blue: 3>]

#? ------------------ Section 8.1: Operations on sets -------------------------?#

# Intersection
{1, 2, 3, 4, 5}.intersection({3, 4, 5, 6})  #todo: {3, 4, 5}
{1, 2, 3, 4, 5} & {3, 4, 5, 6}  #todo: {3, 4, 5}
# Union
{1, 2, 3, 4, 5}.union({3, 4, 5, 6}) #todo: {1, 2, 3, 4, 5, 6}  
{1, 2, 3, 4, 5} | {3, 4, 5, 6}  #todo: {1, 2, 3, 4, 5, 6}
# Difference
{1, 2, 3, 4}.difference({2, 3, 5})  #todo: {1, 4}
{1, 2, 3, 4} - {2, 3, 5} #todo: {1, 4}

# Symmetric difference with
{1, 2, 3, 4}.symmetric_difference({2, 3, 5}) #todo: {1, 4, 5}
{1, 2, 3, 4} ^ {2, 3, 5} #todo: {1, 4, 5}
# Superset check
{1, 2}.issuperset({1, 2, 3})  #todo: False
{1, 2} >= {1, 2, 3} #todo: False
# Subset check
{1, 2}.issubset({1, 2, 3})  #todo: True
{1, 2} <= {1, 2, 3} #todo: True
# Disjoint check
{1, 2}.isdisjoint({3, 4}) #todo: True
{1, 2}.isdisjoint({1, 4}) #todo: False

#* Get unique list
restaurants = ["McDonald's", "Burger King", "McDonald's", "Chicken Chicken"]
list(set(restaurants)) #todo: ['Chicken Chicken', "McDonald's", 'Burger King']

a = {1, 2, 3, 4, 5}
b = {3, 3, 4, 4, 5}

# print(a.intersection(b)) #todo: {3, 4, 5}
a.symmetric_difference(b)  #todo: {1, 2, 5}
b.symmetric_difference(a) #todo: {1, 2, 5}
c = {1, 2}
c.issubset(a) #todo: True
a.issubset(c) #todo: True

""" 
    a.intersection(b) a & b
    a.union(b) a | b
    a.difference(b) a - b
    a.symmetric_difference(b) a ^ b
    a.issubset(b) a <= b
    a.issuperset(b) a >= b
"""

#? ---------------------- Chapter 9: Simple Mathematical Operators -------?#
import math
import cmath
#* The function math.exp(x) computes e ** x

math.exp(0) #todo: 1.0
math.exp(1) #todo: 2.718281828459045

a, b = 1, 2

math.atan(math.pi) #todo: returns the arc tangent of 'pi' in radians

#todo: To convert from radians -> degrees and degrees -> radians respectively use math.degrees and math.radians

# print(math.degrees(a))
# print(math.radians(57.29577951308232))
math.log(1000, 10) #todo: 3.0 (always returns float)
cmath.log(1000, 10) #todo: (3+0j)

#* Find the quitient and remainder
quitient, remainder = divmod(9, 4)
# print(quitient, remainder) #todo: 2 1