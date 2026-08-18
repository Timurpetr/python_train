# from math import floor
#
# lst = list(map(float,input().split()))
#
# lst_res = [a for a in lst if int(a) % 2 == 0]
# print(*lst_res)
#


# my_gen = (x for x in range(1000000))
# print(next(my_gen))
# print(next(my_gen))
# # print(next(my_gen))
# func = lambda x: x * 2
#
#
# my_gen = (func(x) for x in range(10))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))


# def generate(func, lst):
#     for item in lst:
#         if func(item):
#             yield item
#
#
# assert generate(lambda x: x > 0, [1, 2, 3]) == [1, 2, 3]


# def even_numbers(n):
#     for i in range(n):
#         if i % 2 == 0:
#             yield i
#
#
# g = even_numbers(10)
#
# print(list(g))


# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1
#
#
# print(list(countdown(5)))


# class Animal:
#     def __init__(self, color, size):
#         self.color = color
#         self.size = size
#
#
# class Cat(Animal):
#     def __init__(self, color, size, name):
#         super().__init__(color, size)
#         self.name = name
#
#
# ry = Cat("red", 3, "ry")
# print(ry.color)
# print(ry.size)
# print(ry.name)
# class Singleton:
#     __instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
#
#
# class Game(Singleton):
#     def __init__(self, name):
#         if not hasattr(self, "name"):
#             self.name = name
# class MyIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration
#
#         value = self.data[self.index]
#         self.index += 1
#         return value
#
#
# it = MyIterator([10, 20, 30])
# print(next(it))
# print(next(it))


# class Counter:
#     def __init__(self, data):
#         self.data = data
#         self.index = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index > self.data:
#             raise StopIteration
#         value = self.index
#         self.index += 1
#         return value
#
#
# c = Counter(3)
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next_node = None
#
#
# class NodeIterator:
#     def __init__(self, node):
#         self.current = node
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current == None:
#             raise StopIteration
#         value = self.current
#         self.current = self.current.next_node
#         return value
#
#
# a = Node("A")
# b = Node("B")
# c = Node("C")
#
# a.next_node = b
# b.next_node = c


# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         return Number(self.value + other.value)
#
#
# a = Number(10)
# b = Number(5)
#
# c = a + b
#
# print(c.value)


# class MyTuple(tuple):
#     def __new__(cls, iterable):
#         return tuple.__new__(cls, iterable)
#
#
# t = MyTuple([1, 2, 3])
#
# print(t)


class MyTuple(tuple):

    def __new__(cls, iterable):
        return tuple.__new__(cls, iterable)

    def __init__(self, iterable):
        self.iterable = iterable

    def __add__(self, other):
        c = []
        for x in self.iterable:
            c.append(x)
        for y in other:
            c.append(y)
        return MyTuple(c)


t = MyTuple([1, 2, 3])

t2 = t + [4, 5]

print(t2)
print(type(t2))
