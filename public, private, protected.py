class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @classmethod
    def __check_coord(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_coord(x) and self.__check_coord(y):
            self.__x = x
            self.__y = y
        else:
            raise TypeError("Координаты должны быть числами")

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(12, 20)
print(pt.get_coord())
