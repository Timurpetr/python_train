class Tuple(tuple):

    def __new__(cls, iterable):
        return super().__new__(cls, iterable)

    def __add__(self, other):
        return Tuple(tuple(self) + tuple(other))


t = Tuple([1, 2, 3])
t = t + "Python"
print(t)  # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
t = (t + "Python") + "ООП"
