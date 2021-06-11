from functools import wraps
from types import MethodType
import functools
s = True
#? ========== Chapter 34: Defining functions with list arguments ====== ?#

if s is False:
    def func(myList):
        for item in myList:
            print(item)

    func([1, 2, 3, 5, 7])

#? ============== Chapter 35: Functional Programming in Python ======== ?#

if s is False:
    name_lengths = map(len, ['Mary', 'Jason', 'Sam'])
    print(tuple(name_lengths))

# * Section 35.3: Reduce Function

if s is False:
    total = functools.reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])
    print(total)

# * Section 35.4: Filter Function

if s is False:
    arr = [1, 2, 3, 4, 5, 6]
    res = [i for i in filter(lambda x: x > 4, arr)]
    print(res)


#? ======================== Chapter 36: Partial functions ============== ?#

#? ======================== Chapter 37: Decorators ===================== ?#

# * Section 37.1: Decorator function


if s is False:

    def super_secret_function(f):
        return f

    @super_secret_function
    def my_function():
        print("This is my secret function.")

    #todo: my_function = super_secret_function(my_function)

    def disabled(f):
        """
        This function returns nothing, and hence removes the decorated function
        from the local scope.
        """
        pass

    @disabled
    def my_function():
        print("This function can no longer be called...")

    # my_function()

    def print_args(func):
        def inner_func(*args, **kwargs):
            print(args)
            print(kwargs)
            return func(*args, **kwargs)
        return inner_func

    @print_args
    def multiply(num_a, num_b):
        return num_a * num_b

    print(multiply(3, 5))

# * Section 37.2: Decorator class

if s is False:

    class Decorator(object):
        """Simple decorater class."""

        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            print("Before the function call.")
            res = self.func(*args, **kwargs)
            print("After the function call.")
            return res

    @Decorator
    def testFunc():
        print("Inside the function.")

    testFunc()

if s is False:

    class Decorator(object):
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            print("Inside the decorater")
            return self.func(*args, **kwargs)

        def __get__(self, instance, cls):
            # todo: Return a Method if it is called on an instance (durum)
            return self if instance is None else MethodType(self, instance)

    class Test(object):
        @Decorator
        def __init__(self):
            pass

    a = Test()

if s is False:

    class CountCallsDecorator(object):
        def __init__(self, func):
            self.func = func
            self.ncalls = 0  # todo: Number of calls of this method

        def __call__(self, *args, **kwargs):
            self.ncalls += 1
            return self.func(*args, **kwargs)

        def __get__(self, instance, cls):
            return self if instance is None else MethodType(self, instance)

    class Test(object):
        def __init__(self):
            pass

        @CountCallsDecorator
        def do_something(self):
            return 'something was done.'

    a = Test()
    a.do_something()
    number = a.do_something.ncalls
    print(number)
    b = Test()
    b.do_something()
    number = b.do_something.ncalls
    print(number)


# * Section 37.3: Decorator with arguments (decorator factory)

if s is False:
    def decoratorfactory(message):
        def decarator(func):
            def wrapped_func(*args, **kwargs):
                print(f"The decarator wants to tell you: {message}")
                return func(*args, **kwargs)
            return wrapped_func
        return decarator

    @decoratorfactory("Hello World")
    def test():
        pass
    test()

if s is False:
    def decaratorfactory(*decorator_args, **decarator_kwargs):
        class Decorator(object):
            def __init__(self, func):
                self.func = func

            def __call__(self, *args, **kwargs):
                print(f"Inside the decarator with arguments {decorator_args}")
                return self.func(*args, **kwargs)

        return Decorator

    @decaratorfactory(10)
    def test():
        pass

    test()

# * Section 37.4: Making a decorator look like the decorated function

if s is True:

    def decarator(func):
        # todo: Copies the docstring, name, annotations and module to the decorator
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapped_func

    @decarator
    def test():
        pass

    # test.__name__

    class Decorator(object):
        def __init__(self, func):
            # Copies name, module, annotations and docstring to the instance.
            self._wrapped = wraps(func)(self)

        def __call__(self, *args, **kwargs):
            print("Hello")
            return self._wrapped(*args, **kwargs)

    @Decorator
    def test():
        """Docstring of test."""

    test.__doc__

# * Section 37.5: Using a decorator to time a function
    import time
    
    def timer(func):
        def inner(*args, **kwargs):
            t1 = time.time()
            f = func(*args, **kwargs)
            t2 = time.time()
            print(f'Runtime took {t2-t1} seconds')
            return f
        return inner
    
    @timer
    def example_function():
        print("ExampleFunction")
        
    example_function()