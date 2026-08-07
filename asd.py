# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     def __hash__(self):
#         return hash((self.x, self.y))
#
#
# p1 = Point(1, 2)
# p2 = Point(1, 2)
#
# print(p1 == p2)
# print(hash(p1) == hash(p2))


# class PathLine:
#     def __init__(self, dist, angle):
#         self.dist = dist
#         self.angle = angle
#
#     def __eq__(self, other):
#         return abs(self.dist) == abs(other.dist)
#
#
# p1 = PathLine(10, 1.57)
# p2 = PathLine(-10, 0.49)
# h1, h2 = hash(p1), hash(p2)
# print(h1, h2)
# class Rect:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def __hash__(self):
#         return hash((self.width, self.height))
#
#
# r1 = Rect(10, 5, 100, 50)
# r2 = Rect(-10, 4, 100, 50)
# h1, h2 = hash(r1), hash(r2)
# print(h1 == h2)


# class Index:
#     START_INDEX = 0
#
#     def __init__(self):
#         self.id = Index.START_INDEX
#         Index.START_INDEX += 1
#
#     def __hash__(self):
#         return hash(str(self.id))
#
#
# id1 = Index()
# id2 = Index()
# d = {id1: id1, id2: id2}
# print(d)
