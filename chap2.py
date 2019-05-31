class point:
    def reset(self):
        self.x = 0
        self.y = 0

first = point ()
# creates 2 points x, and y
first.x = 5
first.y = 7

# resets the points to zero
# first.reset()
point.reset(first)
print(first.x,first.y)