class Point:
    def __init__(self, a, b, color="black"):
        self.x = a
        self.y = b
        self.color = color


p1 = Point(10, 20)
p2 = Point(12, 5, "red")

points = []
i = 1
while len(points) < 1000:
    if i == 3:
        points.append(Point(i, i, "yellow"))
    else:
        points.append(Point(i, i))
    i += 2
