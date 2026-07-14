# class Point:
#     color = "red"
#     circle = 2
#
#     def __init__(self, a, b):
#         self.x = a
#         self.y = b
#
#     def __del__(self):
#         print(str(self))
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#     def get_coords(self):
#         return self.x, self.y
#
#
# pt = Point(1, 2)
# print(pt.__dict__)
# print(Point.get_coords)


class Cat:
    speak = "Meow"
    bad_things = "Кака"

    def __init__(self, year, color):
        self.year = 1
        self.color = "red"
        self._print_on_delete = False

    def __del__(self):
        if getattr(self, "_print_on_delete", False):
            print("Кот исчез...")


Tom = Cat(4, "grey")
print(Tom.__dict__)
print(Tom.speak)

Elya = Cat(1, "white")
Elya.speak = "Муррр"

print(vars(Elya))
print(Tom.speak)
Tom._print_on_delete = True
del Tom
