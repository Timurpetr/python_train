class ListInteger(list):
    def __init__(self, iterable):
        for x in iterable:
            if not type(x) is int:
                raise TypeError("можно передавать только целочисленные значения")
        super().__init__(iterable)

    def __setitem__(self, index, value):
        if not type(value) is int:
            raise TypeError("можно передавать только целочисленные значения")
        super().__setitem__(index, value)

    def append(self, value):
        if not type(value) is int:
            raise TypeError("можно передавать только целочисленные значения")
        super().append(value)


s = ListInteger((1, 2, 3))
s[1] = 10
s.append(123)
print(s)
print(s)
