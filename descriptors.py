class Matherfucker:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(self.name, value)
        instance.__dict__[self.name] = value


class Point3D:
    x = Matherfucker()
    y = Matherfucker()
    z = Matherfucker()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def verify_coords(cls, coord):
        if type(coord) != int:
            raise TypeError("Coordinates must be an integer")


p = Point3D(1, 2, 3)
print(p.x, p.y, p.z)
