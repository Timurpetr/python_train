# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def get_old(self):
#         return self.__age
#
#     @get_old.setter
#     def get_old(self, age):
#         self.__age = age
#
#
# p = Person("", 18)
# p.get_old = 35
# print(p.get_old)
from pyexpat import model

# class Car:
#     def __init__(self):
#         self.__model = None
#
#     @property
#     def model(self):
#         return self.__model
#
#     @model.setter
#     def model(self, model):
#         if type(model) == str and 2 <= len(model) <= 100:
#             self.__model = model
#
#
# car = Car()
# car.model = "Toyota"
# print(car.model)


class WindowDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width = None
        self.__height = None
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) == int and 0 <= value <= 10000:
            if self.__width:
                self.show()
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) == int and 0 <= value <= 10000:
            if self.__height:
                self.show()
            self.__height = value

    def show(self):
        print(f"{self.__title}: {self.__width}, {self.__height}")
