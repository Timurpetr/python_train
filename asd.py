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
from black.linegen import split_wrapper

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
# print(hash((1, 2, 3, {1: "", 2: ""})))
a = "Табачник Ян Ефимович\n Черемесонов Михаил Дмитриевич\n Бабинець Ринат Гермонович \n Цызин Ринат Владимирович \n Тинаев Виталий Викторович"


def func(lst):
    split_lst = [line.strip() for line in lst.split("\n")]
    surname_lst = [surname.split(" ")[0] for surname in split_lst]
    i = 0
    count = []
    while i < len(surname_lst):
        s = len(surname_lst[i])
        count.append(s)
        i += 1
    res = []
    mid = int(sum(count) / len(count))
    for surname in surname_lst:
        if len(surname) == min(count, key=lambda x: abs(x - mid)):
            continue
        else:
            res.append(surname)

    return res, count


print(func(a))
