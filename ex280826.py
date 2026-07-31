# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}({self.name})"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = Cat("Mario")
# print(repr(cat))
class Point:
    def __init__(self, *args):
        self._coords = args

    def __len__(self):
        return len(self._coords)

    def __abs__(self):
        return list(map(abs, self._coords))


p = Point(-1, 2)
print(len(p))
print(abs(p))
