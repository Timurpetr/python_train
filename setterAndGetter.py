# class Point:
#     def __init__(self, x=1, y=1):
#         self.__x = x
#         self.__y = y
#
#     def set_coords(self, x, y):
#         if isinstance(x, (int, float)) and isinstance(y, (int, float)):
#             self.__x = x
#             self.__y = y
#         else:
#             raise TypeError("Координаты должны быть цифрами")
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#
# pt = Point()
# pt.__x = 10
# pt.__y = "20"
#
# print(pt.__x)
# print(pt.__y)
# print(pt.set_coords(10, "20"))


# class Book:
#     def __init__(self, author, title, price):
#         self.__title = title
#         self.__author = author
#         self.__price = price
#
#     def set_title(self, title):
#         self.__title = title
#
#     def set_author(self, author):
#         self.__author = author
#
#     def set_price(self, price):
#         self.__price = price
#
#     def get_title(self):
#         return self.__title
#
#     def get_author(self):
#         return self.__author
#
#     def get_price(self):
#         return self.__price
#
#
# book = Book("фыввфы", "asdadsds", "adsads")


# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__x2 = x2
#         self.__y2 = y2
#
#     def set_coords(self, x1, y1, x2, y2):
#         self.__x1 = x1
#         self.__y1 = y1
#         self.__y2 = y2
#         self.__x2 = x2
#
#     def get_coords(self):
#         return self.__x1, self.__y1, self.__x2, self.__y2
#
#     def draw(self):
#         print(self.__x1, self.__y1, self.__x2, self.__y2)
#
#
# line1 = Line(0, 0, 10, 10)
#
# print(line1.get_coords())
# print(line1.draw())


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return (self.__x, self.__y)


class Rectangle:
    def __init__(self, *args):
        if len(args) == 4:
            x1, y1, x2, y2 = args
            self.__sp = Point(x1, y1)
            self.__ep = Point(x2, y2)
        else:
            sp, ep = args
            self.__sp = sp
            self.__ep = ep

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return (self.__sp, self.__ep)

    def draw(self):
        x1, y1 = self.__sp.get_coords()
        x2, y2 = self.__ep.get_coords()
        print(f"Прямоугольник с координатами: ({x1}, {y1}) ({x2}, {y2})")


r2 = Rectangle(1, 2, 1, 2)
