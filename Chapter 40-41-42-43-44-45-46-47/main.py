from collections import defaultdict


s = True
#? ===================== Chapter 40: String Formatting ================ ?#


def basicsString40e1e5():
    # todo: Centered text
    strCentered = '{:~^20}'.format('centered')
    print(strCentered)
    number_list = [12, 45, 78]
    print(list(map('The number is {}'. format, number_list)))

    from datetime import datetime, timedelta
    once_upon_a_time = datetime(2020, 6, 5, 12, 45, 16)
    delta = timedelta(days=13, hours=8, minutes=20)

    gen = (once_upon_a_time + (x * delta) for x in range(5))
    print('\n'.join(map('{:%Y-%m-%d %H:%M:%S}'.format, gen)))

    price = 478.23
    print(f"{f'{price:0.2f}':*>10s}")

    print('{0:.4f}'.format(42.12345))

    string = 'HelloWorldonceAgain'
    a, b, c = 1.12345, 2.34567, 34.5678
    digits = 3
    res = '{0}! {1:.{n}f}, {2:.{n}f}, {3:.{n}f}'.format(s, a, b, c, n=digits)
    print(res)

    data = {'first': 'Hodor', 'last': 'Hodor!'}

    # todo: is equal to '{first} {last}'.format(first='Hodor', last='Hodor!')
    res = '{first} {last}'.format_map(data)
    print(res)


def basicsString40e6e10():
    from datetime import datetime
    res = 'Turkey: {dt:%m/%d/%Y}, ISO: {dt:%Y-%m-%d}.'.format(
        dt=datetime.now())
    print(res)

    res = '{:c}'.format(65)
    print(res)


def basicsString40e11():

    class Example(object):
        def __init__(self, a, b, c):
            self.a, self.b, self.c = a, b, c

        def __format__(self, format_spec):
            """ Implement special semantics for the 's' format specifier """
            # Reject anything that isn't an s
            if format_spec[-1] != 's':
                raise ValueError(
                    '{} format specifier not understood for this object', format_spec[:-1])
            # Output in this example will be (<a>,<b>,<c>)
            raw = "("+",".join([str(self.a), str(self.b), str(self.c)]) + ")"
            return "{r:{f}}".format(r=raw, f=format_spec)

    inst = Example(1, 2, 3)
    print("{0:>20s}".format(inst))


#? =========================== Chapter 41: String Methods =============== ?#

def basicsString41e1e7():

    res = map(str.upper, ['These', 'are', 'some', 'string'])
    print(tuple(res))

    translation_table = (str.maketrans("aeiou", "12345"))
    my_string = "This is a string!"
    translated = my_string.translate(translation_table)
    print((translated))

    import string
    res = string.ascii_letters
    print("Ascii letters: " + res)
    res = string.punctuation
    print("Punctuation: " + res)
    res = string.whitespace  # todo: ' \t\n\r\x0b\x0c'
    # todo: '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\t\n\r\x0b\x0c'
    res = string.printable
    print(res)
    str1 = "       a line with leading and trailing space        "
    print(str1.strip())
    str2 = "This is a sentence."
    print("Only with one parameter 'e': " + str(str2.split('e')))
    print("With parameter: " + str(str2.split('e', 2)))


def basicsString41e8e16():
    string1 = "Make sure to foo your foo sentence.".replace('foo', 'spam', 1)
    print(string1)
    print("-".join(["once", "upon", "a", "time"]))
    s = "She sells seashells by the seashore."
    c = s.count("sea", 12)
    print(c)

    def func(params):
        for value in params:
            print('Got value {}'.format(value))

            if value == 1:
                print("Got {}".format(value))
                return 1

            print("Looping...")

        print("there is no 1")

    func([5, 3, 1, 2, 8, 9])

#? ====================== Chapter 43: Importing modules ================= ?#


def importingmodules43e1():
    import math
    print(math.sin(90))
    degreeCalc = math.sin(math.radians(90))  # ! Perfect...
    print(degreeCalc)
    import time
    # * time
    start = time.time()
    for x in range(50000):
        b = x**3
    # time.sleep(1)
    end = time.time() - start
    print(end)
    # * Logarithms
    res = math.log(math.e)  # todo: loge
    print(res)
    import cmath  # todo: complex math
    print(cmath.sqrt(-1))

#? ====================== Chapter 47: Collections module ================ ?#


def collections47e1e16():
    import collections
    counts = collections.Counter([1, 2, 3])
    print(counts)
    strings = 'I am Sam Sam I am That Sam-I-am That Sam-I-am! I do not like that Sam-I-am'
    counts = collections.Counter(strings.split())
    print(counts)
    print(counts['Sam'])
    print("Count sum: " + str(sum(counts.values())))
    print(list(counts.elements()))
    # todo: Remove keys with 0 or negative value
    print("Counters: " + str(counts - collections.Counter()))
    print("Without counters: " + str(sum((counts - collections.Counter()).values())))

    # todo: Order dict with given order...
    d = collections.OrderedDict([('b', 4), ('a', 3), ('c', 9)])
    print(d)
    o = collections.OrderedDict()
    o['key1'] = 15
    o['key2'] = 10
    o['key3'] = 16
    print(dict(o))

    # todo: default dict
    fruit_counts = defaultdict(int)
    fruit_counts['apple'] += 2
    fruit_counts['banana'] += 4
    fruit_counts['pear']
    print(fruit_counts)

    #todo: namedTuple
    Person = collections.namedtuple('Person', ['name', 'age', 'height'])
    Person = collections.namedtuple('Person', 'age height name')
    Person = collections.namedtuple('Person', 'age, height, name')
    fatih = Person(15, 180, 'Fatih')
    print(fatih)

    # * deque
    d = collections.deque('HelloWorld')
    print([i for i in d])
    indexF = d.index('l')
    print(indexF)
    d.rotate(-1)
    print(d)
    d.rotate(1)
    print(d)


if __name__ == '__main__':
    pass
