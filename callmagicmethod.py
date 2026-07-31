# class Counter:
#     def __init__(self, chars):
#         self.__counter = 0
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise TypeError("Аргумент должен быть строкой")
#         return args[0].strip(self.__chars)
import math

# c = Counter()
# c2 = Counter()
#           |
#           |
#           |
#           |_ _ _ _ _> __call__(self, *args, **kwargs):
#                             obj = self.__new__(self, *args, **kwargs)
#                             self.__init__(obj, *args, **kwargs)
#                             return obj
# c()
# c(2)
# res = c(10)
# c2()
# c2()
# res2 = c2(-5)
# print(res, res2)


# s1 = Counter("?:!.,;")
# s2 = Counter(" ")
# res = s1("Hello World!")
# print(res)
# res2 = s2(" Hello World!  ")
# print(res2)
class Derivative:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


def df_sin(x):
    return math.sin(x)


df_sin = Derivative(df_sin)
print(df_sin(math.pi / 3))
