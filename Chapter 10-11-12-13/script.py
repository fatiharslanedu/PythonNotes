
#? ------------------ Chapter 10: Bitwise Operators --------------?#

#todo: -2
#todo: -2 = 1111 1110

#* Bitwise XOR

a = 0b111100 #todo: 60
b = 0b011110 #todo: 30

a ^ b #todo: 34
bin(60^30) #todo: 60

#* Bitwise and

60 & 30 #todo: 28
bin(60 & 30) #todo: 0b11100

#* Bitwise OR

60 | 30 #todo:62
bin(60 | 30) #todo:0b111110

#* Bitwise Left Shift

3 << 4 #todo: 3 --> 0011 --> 0110 --> 1100 --> 11000 --> 110000(48)

#* Bitwise Right Shift

59 >> 3 #todo: 59 --> 111011 --> 011101 --> 001110 --> 000111(7)

def true_func():
    print("true_func()")
    return True

def false_func():
    print("false_func()")
    return False

# true_func() or false_func() #todo: True
# print(true_func() and false_func()) #todo: False

#? --------------- Chapter 13: Variable Scope and Binding ----------?#

#? ---------------- Section 13.1: Nonlocal Variables ---------------?#

def counter():
    num = 0
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer

c = counter()
c()
c()
c()
# print(c()) #todo: 4

#* Global Variables

x = 'Hi'

def read_x():
    print(x)

# read_x()

def read_y():
    print(y)

# read_y() #todo: Error

def read_y():
    y = 'Hey'
    print(y)

# read_y()

def read_x_local_fail():
    if False:
        x = 'Hey'
    print(x)

# read_x_local_fail() #todo: UnboundLocalError: local variable 'x' referenced before assignment

def change_local_x():
    x = 'Bye'
    print(x)

# change_local_x() #todo: prints Bye
# print(x) #todo: prints Hi

# * Del

x = [0, 1, 2, 3, 4]
del x[1:3] #todo: [0, 3, 4]

a = 'global'

class Fred:
    a = 'class'
    b = (a for i in range(10))
    c = [a for i in range(10)]
    d = a
    e = lambda: a
    f = lambda a=a: a

    @staticmethod
    def g():
        return a

# print("a: " + Fred.a)
# print("b: " + next(Fred.b))
# print("c: " + Fred.c[0])
# print("d: " + Fred.d)
# print("e: " + Fred.e())
# print("f: " + Fred.f())
# print("g: " + Fred.g())

foo = 1

def func():
    bar = 2
    print(globals().keys())
    print(locals().keys())

# func()

foo = 1
def f1():
    bar = 1
    def f2():
        baz = 2
        # here, foo is a global variable, baz is a local variable
        # bar is not in either scope
        print(locals().keys()) # ['baz']
        print('bar' in locals()) # False
        print('bar' in globals()) # False
    def f3():
        baz = 3
        print(bar) # bar from f1 is referenced so it enters local scope of f3 (closure)
        print(locals().keys()) # ['bar', 'baz']
        print('bar' in locals()) # True
        print('bar' in globals()) # False
    def f4():
        bar = 4 # a new local bar which hides bar from local scope of f1
        baz = 4
        print(bar)
        print(locals().keys()) # ['bar', 'baz']
        print('bar' in locals()) # True
        print('bar' in globals()) # False

def f1():

    def f2():
        foo = 2 #a new foo local in f2
        def f3():
            nonlocal foo # foo from f2, which is the nearest enclosing scope
            print(foo) # 2
            foo = 20
            return foo
        return f3()
    return f2()

# print(f1())