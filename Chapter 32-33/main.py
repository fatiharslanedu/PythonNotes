s = True

if s is False:
    class MyIterable:
        def __init__(self):
            return self

        def __next__(self):
            # code
            pass

    class MySequence:
        def __getitem__(self, index):
            if (condition):
                raise IndexError
            return (item)

if s is False:
    s = {1, 2}
    i = iter(s)
    a = next(i)
    print(a)

# ? ================= Chapter 33: Functions ======================

# * Section 33.2: Defining a function with an arbitrary number of arguments

if s is False:
    def func(*args):
        # todo: args will be a tuple containing all values that are passed
        for i in args:
            print(i)
    func(1, 2, 3)
    list_of_arg_values = [1, 2, 3]
    func(*list_of_arg_values)

if s is False:
    def func(**kwargs):
        # todo: # kwargs will be a dictionary containing the names as keys and the values as values
        for name, value in kwargs.items():
            print(name, value)

    func(value1=1, value2=2, value=3)
    my_dict = {'foo': 1, 'bar': 2}
    func(**my_dict)

# * Section 33.3: Lambda (Inline/Anonymous) Functions

if s is False:
    def strip_and_upper_case(s): return s.strip().upper()
    print(strip_and_upper_case("  Hello  "))
    greeting = lambda x, *args, **kwargs: print(x, args, kwargs)
    greeting('hello', 'world', world='world')

    print(sorted([" foo ", "    bAR", "BaZ      "],
          key=lambda s: s.strip().upper()))

    def append(elem, to=None):
        if to is None:
            to = []
        to.append(elem)
        return to

    # print(append(4, [3,2,3]))

# * Section 33.8: Closure

if s is False:
    def makeInc(x):
        def inc(y):
            return x+y
        return inc

    incOne = makeInc(1)
    incFive = makeInc(5)
    print(incOne(5))
    print(incFive(5))

if s is False:

    def makeInc(x):
        def inc(y):
            nonlocal x
            x += y
            return x
        return inc

    incOne = makeInc(1)
    x = incOne(5)
    print(x)

# * Section 33.10: Nested functions

if s is False:

    def fibonacci(n):
        def step(a, b):
            return b, a+b
        a, b = 0, 1
        for i in range(n):
            a, b = step(a, b)
        return a

    print(fibonacci(5))  # todo: 1 1 2 3 5

if s is False:

    def cursing(depth):
        try:
            cursing(depth + 1)
        except RuntimeError as RE:
            print(f"I recursed {depth} times!")

    cursing(0)

# * Section 33.12: Recursive Lambda using assigned variable

if s is False:

    def lambda_factorial(i): return 1 if i == 0 else i*lambda_factorial(i-1)
    print(lambda_factorial(4))

# * Section 33.13: Recursive functions

if s is False:
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    x = factorial(5)
    print(x)

# * Section 33.15: Iterable and dictionary unpacking

if s is False:

    def unpacking(a, b, c=45, d=60, *args, **kwargs):
        print(a, b, c, d, args, kwargs)

    unpacking(1, 2)  # todo: 1 2 45 () {}
    unpacking(1, 2, 4, 15, *(1, 2), **{'floor1': 'f1', 'floor2': 'f2'})
