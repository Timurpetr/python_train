class Box3D:
    def __init__(self, width, height, depth):
        if not all(isinstance(x, (int, float)) for x in (width, height, depth)):
            raise TypeError("Box3D dimensions must be integers or floats")

        self.width = width
        self.height = height
        self.depth = depth

    def get_type(self):
        return f"{self.width} {self.height} {self.depth}"

    def __add__(self, other):
        if not isinstance(other, Box3D):
            return NotImplemented
        return Box3D(
            self.width + other.width,
            self.height + other.height,
            self.depth + other.depth,
        )

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if not isinstance(other, Box3D):
            return NotImplemented
        return Box3D(
            self.width - other.width,
            self.height - other.height,
            self.depth - other.depth,
        )

    def __mul__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Box3D(self.width * other, self.height * other, self.depth * other)

    def __rmul__(self, other):
        return self * other

    def __floordiv__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Box3D(self.width // other, self.height // other, self.depth // other)

    def __mod__(self, other):
        if not isinstance(other, (int, float)):
            return NotImplemented
        return Box3D(self.width % other, self.height % other, self.depth % other)
