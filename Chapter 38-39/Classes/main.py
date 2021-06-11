class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.li = [1, 3, 4]
        
    def speak(self):
        print(f"Hi I am {self.name} and I am {self.age} years old.")
        
    def change_age(self, age):
        self.age = age
        
    def add_weight(self, weight):
        self.weight = weight
    
        
class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
        
tim = Cat("Fatih", 25, "Blue")
tim.speak()