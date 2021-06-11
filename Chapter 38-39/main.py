s = True
#? ==================== Chapter 38: Classes ================= ?#
if s is False:
    class Person(object):
        """A simple class."""
        species = "Homo Sapiens"

        def __init__(self, name):
            self.name = name

        def __str__(self):
            """
            This method is run when Python tries
            to cast the object to a string. Return
            this string when using print(), etc.
            """
            return self.name

        def rename(self, renamed):
            self.name = renamed

    p1 = Person("John Cena")
    print(str(p1))  # todo: John Cena
    print(p1)  # todo: John Cena
    print(p1.__str__())  # todo: John Cena

# * Section 38.2: Bound, unbound, and static methods
# ? bound = bağımlı
if s is False:
    class A(object):
        def f(self, x):
            return 2 * x

    print(A.f.__class__)  # todo: <class 'function'>
    import inspect
    res = inspect.isfunction(A.f)
    print(res)  # todo: True
    res = inspect.ismethod(A.f)
    print(res)  # todo: False

if s is False:
    class D(object):
        multiplier = 2

        @classmethod
        def f(cls, x):
            return cls.multiplier * x

        @staticmethod
        def g(name):
            print(f"Hello {name}!")

    print(D.f)
    print(D.f(12))
    print(D.g)
    D.g("Fatih")
    d = D()
    d.multiplier = 4
    print(d.f(4))

# * Section 38.3: Basic inheritance

if s is False:

    class Rectangle(object):
        def __init__(self, w, h):
            self.w = w
            self.h = h

        def area(self):
            return self.w * self.h

        def perimeter(self):
            return 2 * (self.w + self.h)

    r = Rectangle(10, 20)
    print(r.area(), r.perimeter())

    class Square(Rectangle):
        def __init__(self, s):
            # todo: call parent constructor, w and h both s
            super().__init__(s, s)

    s = Square(4)
    print(s.area())

# * Section 38.4: Monkey Patching

if s is False:

    class A(object):
        def __init__(self, num):
            self.num = num

        def __add__(self, other):
            return A(self.num + other.num)

    def get_num(self):
        return self.num

    A.get_num = get_num

    foo = A(42)
    foo2 = A(18)
    foo3 = foo + foo2
    print(foo3.get_num())
    print(foo3.num)

# * Section 38.6: Class methods: alternate initializers

if s is False:

    class Person(object):
        def __init__(self, first_name, last_name, age):
            self.first_name = first_name
            self.last_name = last_name
            self.age = age
            self.full_name = first_name + " " + last_name

        def greet(self):
            print(f"Hello, my name is {self.full_name}.")

if s is False:
    class Person(object):
        def __init__(self, first_name, age, last_name=None):
            if last_name is None:
                self.first_name, self.last_name = first_name.split(" ", 2)
            else:
                self.first_name = first_name
                self.last_name = last_name

            self.full_name = self.first_name + " " + self.last_name
            self.age = age

        def greet(self):
            print(f"Hello, my name is {self.first_name}.")

    name = "Fatih"
    surname = name.split(",", 3)  # todo: ['Fatih']
    p1 = Person("Fatih", 15, "")
    p1.greet()

if s is False:

    class Person(object):
        def __init__(self, first_name, last_name, age):
            self.first_name = first_name
            self.last_name = last_name
            self.age = age
            self.full_name = first_name + " " + last_name

        @classmethod
        def from_full_name(cls, name, age):
            if " " not in name:
                raise ValueError
            first_name, last_name = name.split(" ", 2)
            return cls(first_name, last_name, age)

        def greet(self):
            print(f"Hello, my name is {self.full_name}.")

    bob = Person("Bob", "Bobberson", 42)
    alice = Person.from_full_name("Alice Hendersen", 31)

    bob.greet()
    name = "Fatih Arslan Helvatica Arial"
    x = name.split(" ", 2)
    print(x)
    alice.greet()

# * Section 38.7: Multiple Inheritance
if s is False:
    class Foo(object):
        def __init__(self):
            print("Foo method")

    class Bar(object):
        def __init__(self):
            print("Bar method")

    class FooBar(Foo, Bar):
        def __init__(self):
            print("Foobar init")
            super(FooBar, self).__init__()

    fb = FooBar()

# * Section 38.8: Properties

if s is False:

    class MyClass(object):

        def __init__(self):
            self._my_string = ""

        @property
        def string(self):
            """A profoundly important string."""
            return self._my_string

        @string.setter
        def string(self, new_value):
            assert isinstance(new_value, str), \
                f"Give me a string, not a {type(new_value)}"
            self._my_string = new_value

        def foo(self):
            print(self._my_string)

        @string.deleter
        def x(self):
            self._my_string = None

    mc = MyClass()
    mc.string = "Hello!"
    # mc.string = 5 #todo: Give me a string, not a <class 'int'>
    # print(mc.string)

    class Character(object):
        def __init__(self, name, max_hp):
            self._name = name
            self._hp = max_hp
            self._max_hp = max_hp

        # todo: Make hp read only by not providing a set method
        @property
        def hp(self):
            return self._hp

        @property
        def max_hp(self):
            return self._max_hp

        # todo: Make name read only by not providing a set method
        @property
        def name(self):
            return self.name

        def take_damage(self, damage):
            self._hp -= damage
            self._hp = 0 if self.hp < 0 else self.hp

        @property
        def is_alive(self):
            return self.hp != 0

        @property
        def is_wounded(self):
            return self.hp < self.max_hp if self.hp > 0 else False

        @property
        def is_dead(self):
            return not self.is_alive

    bilbo = Character('Bilbo Baggins', 100)
    res = bilbo.hp
    print(res)
    # bilbo.hp = 200 #todo: cant set attribute
    res = bilbo.is_alive
    print(res)
    res = bilbo.is_wounded
    print(res)
    res = bilbo.is_dead
    print(bilbo.hp)
    bilbo.take_damage(10)
    print(bilbo.hp)
    res = bilbo.is_alive
    print(res)
    res = bilbo.is_wounded
    print(res)
    res = bilbo.is_dead
    print(res)

# * Section 38.9: Default values for instance variables

if s is False:
    class Rectangle(object):
        def __init__(self, width, height, color='blue'):
            self.width = width
            self.height = height
            self.color = color

        def area(self):
            return self.width * self.height
    defaultdict = Rectangle(2, 5)
    print(defaultdict.color)

    class Rectangle2D(object):
        def __init__(self, width, height, pos=[0, 0], color='blue'):
            self.width = width
            self.height = height
            self.pos = pos
            self.color = color

    r1 = Rectangle2D(5, 3)
    r2 = Rectangle2D(7, 8)
    r1.pos[0] = 4
    print(r1.pos)  # todo: 4, 0

    class Rectangle2D(object):
        def __init__(self, width, height, pos=None, color='blue'):
            self.width = width
            self.height = height
            self.pos = pos or [0, 0]  # todo: default value is [0, 0]
            self.color = color

# * Section 38.10: Class and instance variables

if s is False:

    class D:
        x = []

        def __init__(self, item):
            self.x.append(item)

    d1 = D(1)
    d2 = D(2)
    print(d1.x)

# * Section 38.11: Class composition

if s is False:
    
    class Country(object):
        def __init__(self):
            self.cities = []

        def addCity(self, city):
            self.cities.append(city)


    class City(object):
        def __init__(self, numPeople):
            
            self.people = []
            self.numPeople = numPeople

        def addPerson(self, person):
            self.people.append(person)
            
        def join_country(self, country):
            self.country = country
            country.addCity(self)
            
            for i in range(self.numPeople):
                Person(i).join_city(self)
                
    class Person(object):
        def __init__(self, ID):
            self.ID = ID
            
        def join_city(self, city):
            self.city = city
            city.addPerson(self)
            
        def people_in_my_country(self):
            x = sum([len(c.people) for c in self.city.country.cities])
            return x
        

    US = Country()
    TR = Country()
    Kastamonu = City(20)
    Kastamonu.join_country(TR)
    # TR.addCity(Kastamonu)
    Samsun = City(25)
    # Samsun.addPerson(25)
    Samsun.join_country(TR)
    # Fatih = Person(592).join_city(Samsun)
    NYC = City(10).join_country(US)
    SF = City(5).join_country(US)   
    
    
    
    print(US.cities[0].people[0].people_in_my_country())
    print(TR.cities[0].people[0].people_in_my_country())


# * Section 38.12: Listing All Class Members

if s is False:
    
    res = [m for m in dir(list) if not m.startswith('__')]
    print(res) #todo: class default methods without '__'
     
#? ===================== Chapter 39: Metaclasses =================== ?#

if s is True:
    
    Dummy = type('OtherDummy', (), dict(x = 1))
    print(Dummy.__class__)
    print(Dummy().__class__.__class__)
    
    class mytype(type):
        def __init__(cls, name, bases, dict):
            # call the base initializer
            type.__init__(cls, name, bases, dict)
            # perform custom initialization...
            cls.__custom_attribute__ = 2
    
    class MyDummy(object):
        __metaclass__ = mytype
        
    MyDummy = mytype('MyDummy', (), dict(x=2))
    x = MyDummy.__class__
    print(x)
    MyDummy().__class__.__class__ 
    MyDummy.__custom_attribute__
    res = type(MyDummy)
    print(res)
    