
import itertools
import fileinput
import mmap
import os
import errno
statement = True

# * Reading a file line-by-line

# todo: Option 1
if statement is False:
    with open("dum.txt", "r") as fp:
        for line in fp:
            print(line)

# todo: Option 2
if statement is False:
    with open("dum.txt", "r") as fp:
        while True:
            cur_line = fp.readline()
            if cur_line == '':
                break
            print(cur_line)


# todo: Option 3
if statement is False:
    with open("dum.txt", "r") as fp:
        lines = fp.readlines()
    for i in range(len(lines)):
        print("Lines " + str(i) + ": " + lines[i])


# * Section 30.3: Iterate ﬁles (recursively)

if statement is False:
    import os
    root_dir = '/home/fatih/Desktop/Archive/Books/C-in-One-Hour'
    for root, folders, files in os.walk(root_dir):
        for filename in files:
            print(root, filename)

# * Section 30.5: Writing to a ﬁle

# todo: line by line
if statement is False:
    with open("writefile.txt", "w", encoding="utf-8") as f:
        f.write("Line 1\n")
        f.write("Line 2\n")
        f.write("Line 3\n")

if statement is False:
    with open("writefile.txt", "w", encoding="utf-8") as f:
        s = "Input File"
        print(s)
        print(s, file=f)
        f = None  # todo: after that not gonna write.
        print(s, file=f)  # todo: only stdout.
        print(s, file=None)

# * Section 30.6: Check whether a ﬁle or path exists

path = '/home/fatih/Desktop/Archive/Books/PythonForProfessional/Chapter 30/writefile.txt'
if statement is False:
    print(os.path.isfile(path))


# * Section 30.8: Replacing text in a ﬁle


replacements = {'Search1': 'Replace1',
                'Search2': 'Replace2'}

if statement is False:  # todo: Change the Search1 and Search2 on file
    for line in fileinput.input("writefile.txt", inplace=True):
        for search_for in replacements:
            replace_with = replacements[search_for]
            line = line.replace(search_for, replace_with)
        print(line, end='')

if statement is False:  # todo: Check the file size
    x = os.stat(path).st_size > 0
    print(x)

# * Section 30.10: Read a ﬁle between a range of lines

if statement is False: #todo: Show the 12 and 30 lines
    with open("dum.txt", 'r') as f:
        i = 11
        for line in itertools.islice(f, 12, 30):
            i+= 1
            print("Line " + str(i) + ": " + line)

# * Section 30.12: Copying contents of one ﬁle to a dierent ﬁle

if statement is False:
    with open("dum.txt", 'r') as in_file, open("writefile.txt", "w") as out_file:
        for line in itertools.islice(in_file, 12, 30):
            out_file.write(line)

#? =============== Chapter 31: os.path ==================

if statement is False:
    x = os.path.join('a','b','c') #todo: a/b/c
    print(x)

# * Section 31.2: Path Component Manipulation

if statement is False: #todo: show the path.
    p = os.path.join(os.getcwd(), 'dum.txt')
    print(p)
    print(os.path.abspath(os.path.join('dum.txt', os.pardir)))
    print(os.path.isdir(path))