class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    # def set_bound(self, left):
    #     self.MIN_COORD = left
    # @classmethod
    # def set_bound(cls, left):
    #     cls.MIN_COORD = left
    def __getattribute__(self, item):
        if item == "x":
            raise ValueError("Доступ запрещен")
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == "z":
            raise AttributeError("Недопустимое имя")
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        print("__delattr__" + item)
        object.__delattr__(self, item)


pt1 = Point(1, 2)

pt2 = Point(3, 4)
a = pt1.y
del pt1.x
print(pt1.__dict__)
