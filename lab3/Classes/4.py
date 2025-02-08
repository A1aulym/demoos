class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        f = ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5
        print(f)
        return f
    
a = Point (4, 9)
a.show()
a.move(3, 8)



b = Point(6, 8)
distance = a.dist(b)  

