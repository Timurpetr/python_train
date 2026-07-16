# Декоратор classmethod
class Vector:
    MIN_CORDS = 0
    MAX_CORS = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_CORDS <= arg <= cls.MAX_CORS

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        print(self.normalize_quadrant(x, y))

    def get_cors(self):
        return (self.x, self.y)

    # Декоратор staticmethod
    @staticmethod
    def normalize_quadrant(x, y):
        return x * x + y * y


v = Vector(2, 3)
print(Vector.normalize_quadrant(5, 6))


class Math:
    @staticmethod
    def sqrt(x):
        return x**0.5


m = Math()

res = m.sqrt(2)
m.Math.sqrt(3)
