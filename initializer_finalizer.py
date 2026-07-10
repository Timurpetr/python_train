class Point:
    color = 'red'
    circle = 2

    def __init__(self):
        print('вызов инит')
        self.x = 0
        self.y = 0

    def set_color(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


pt = Point()
pt.set_color(1, 2)
print(pt.__dict__)