class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.coords = {self.x, self.y}
        
    def move(self, x, y):
        self.x += x
        self.y += y
        
p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3)
p4 = Point(0,1)