import math

class point:
    def move(self,x,y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0,0)

    def calculate_distance(self,other_point):
        return math.sqrt(      # calculates a square root
            (self.x - other_point.x)**2 +
            (self.y - other_point.y)**2)

point1 = point()
point2 = point()

point1.reset()
point2.move(5,0)
print( point2.calculate_distance(point1))
assert(point2.calculate_distance(point1)) == point1.calculate_distance(point2)  # simple test tool, the program will baiil f the statement after assert is false
point1.move(3,4)
print(point1.calculate_distance(point2))
print(point1.calculate_distance(point1))

