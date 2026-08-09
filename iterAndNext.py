# class FRange:
#     def __init__(self, start, stop, step):
#         self.start = start
#         self.stop = stop
#         self.step = step
#         self.value = self.start - self.step
#
#     def __iter__(self):
#         self.value = self.start - self.step
#         return self
#
#     def __next__(self):
#         if self.value + self.step < self.stop:
#             self.value += self.step
#             return self.value
#         else:
#             raise StopIteration
#
#
# fr = FRange(0, 2, 0.5)
# for x in fr:
#     print(x)


class GeomRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        self.__value = self.start

    def __next__(self):
        if self.__value < self.stop:
            ret_value = self.__value
            self.__value *= self.step
            return ret_value
        else:
            raise StopIteration

    def __iter__(self):
        self.__value = self.start
        return self


g = GeomRange(1, 2, 1.2)


it = iter(g)
res = next(g)

for x in g:
    print(x)

for x in g:
    print(x)
for x in g:
    print(x)
