class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("len")
        return self.x

    def __bool__(self):
        return bool(self.x)


p = Point(0, 5)
print(bool(p))
