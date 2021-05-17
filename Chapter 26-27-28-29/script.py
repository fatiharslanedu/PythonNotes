import heapq

numbers = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8]
heapq.nlargest(4, numbers)  # todo: [200, 150, 100, 50]
heapq.nsmallest(4, numbers)  # todo: [1, 2, 4, 8]


people = [
    {'firstname':  'John', 'lastname':   'Doe', 'age': 30},
    {'firstname':  'Jane', 'lastname':  'Doe', 'age': 25},
    {'firstname':  'Janie', 'lastname':  'Doe', 'age': 10},
    {'firstname':  'Jane', 'lastname':  'Roe', 'age': 22},
    {'firstname':  'Johnny', 'lastname': 'Doe', 'age': 12},
    {'firstname':  'John', 'lastname': 'Roe', 'age': 45}
]

oldest = heapq.nlargest(2, people, key = lambda s: s['age'])
# print(oldest)
youngest = heapq.nsmallest(2, people, key=lambda s: s['age'])
# print(youngest)

#? ---------------------- Chapter 28: Tuple ---------------?#

t = tuple('lupins')
# print(t) #todo: ('l', 'u', 'p', 'i', 'n', 's')

t = (1,2)
q = (3,4)
t += q
# print(t)

#? --------------------- Chapter 29: Basic Input and Output -------?#

with open("./shoppinglist.txt", 'w') as fileobj:
    fileobj.write('tomato\npasta\ngarlic')

with open('./shoppinglist.txt', 'r') as fileobj:
    lines = []
    for line in fileobj:
        lines.append(line.strip())

# print(lines) #todo: ['tomato', 'pasta', 'garlic']

fileobj = open("./shoppinglist.txt", 'r')
content = fileobj.read()
# print(content)
end = fileobj.tell()
# print(end) #todo: 19
fileobj.close()

import sys

# for line in sys.stdin:
    # print(line)

#* Section 29.6: Printing a string without a newline at the end

# print("Hello", end=" ")
# print("World.")

#? -------------- Chapter 30: Files & Folders I/O ---------------?#

# with open("./myfile.txt", "r") as fp:
#     while True:
#         cur_line = fp.readline()
#         if cur_line == "":
#             break
#         # print(cur_line)
import os
path = '/home/fatih/Desktop'
# for entry in os.scandir(path):    
#     print(entry.name)

with open('./myfile.txt') as in_file: #todo: Full contents of file.
    content = in_file.read()
# print(content)

with open('./my_file.txt', 'w', encoding='utf-8') as f:
    f.write("utf-8 text")

# with open('fred.txt', 'w') as outfile:
#     s = "I'm Not Dead Yet!"
#     print(s) # writes to stdout
#     print(s, file = outfile) # writes to outfile
#     myfile = None
#     print(s, file = myfile) # writes to stdout
#     print(s, file = None)
#     # writes to stdout


import errno
try:
    with open(path) as f:
        pass
        #File exists
except IOError as e:
    # Raise the exception if it is not ENOENT (No such file or directory)
    if e.errno != errno.ENOENT:
        raise