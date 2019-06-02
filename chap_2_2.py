import math

"""
What if we don't want to make those two arguments required? Well then we can use
the same syntax Python functions use to provide default arguments

 class Point:
 def __init__(self, x=0, y=0):
 self.move(x, y)

 So is not a must to provide an x/y cordinate numbers 
"""
class Point:
    "represents a point in a two dimensional geometric coordinates "
    def __init__(self,x=0,y=0):
        self.move(x,y)

    def move(self,x,y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0,0)

    def calculate_distance(self,other_point):
        return math.sqrt((self.x - other_point.x)**2+(self.y - other_point.y)**2)


# creating a point

p = Point(3,5)
print(p.x,p.y)
# moving the point
p.move(5,5)
print(p.x,p.y)

# creating second point
p2 = Point(7,7)
print(p2.x,p2.y)

# calculating distance between the teo points
print(p.calculate_distance(p2))
print(p2.calculate_distance(p))


