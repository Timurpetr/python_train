class Vector:
    def __init__(self, *args):
        self.coors = list(args)

    def _check_same_length(self, other):
        if len(self.coors) != len(other.coors):
            raise TypeError("размерности векторов не совпадают")

    def __add__(self, other):
        self._check_same_length(other)
        res = [x + y for x, y in zip(self.coors, other.coors)]
        if isinstance(other, VectorInt):
            if all(isinstance(x, int) for x in res):
                return VectorInt(*res)
            return Vector(*res)
        return Vector(*res)

    def __sub__(self, other):
        self._check_same_length(other)
        res = [x - y for x, y in zip(self.coors, other.coors)]
        if isinstance(other, VectorInt):
            if all(isinstance(x, int) for x in res):
                return VectorInt(*res)
            return Vector(*res)
        return Vector(*res)

    def get_coords(self):
        return tuple(self.coors)


class VectorInt(Vector):
    def __init__(self, *args):
        super().__init__(*args)
        self._check_int()

    def _check_int(self):
        for x in self.coors:
            if not isinstance(x, int):
                raise ValueError("координаты должны быть целыми числами")

    def __add__(self, other):
        self._check_same_length(other)
        res = [x + y for x, y in zip(self.coors, other.coors)]
        if all(isinstance(x, int) for x in res):
            return VectorInt(*res)
        return Vector(*res)

    def __sub__(self, other):
        self._check_same_length(other)
        res = [x - y for x, y in zip(self.coors, other.coors)]
        if all(isinstance(x, int) for x in res):
            return VectorInt(*res)
        return Vector(*res)
