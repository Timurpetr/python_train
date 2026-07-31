class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, (int, Clock)):
            raise TypeError("seconds must be an integer or Clock")
        self.seconds = seconds % self.__DAY

    def get_type(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formated(h)}:{self.__get_formated(m)}:{self.__get_formated(s)}"

    def __get_seconds(self, other):
        if isinstance(other, Clock):
            return other.seconds
        if isinstance(other, int):
            return other
        raise TypeError("seconds must be an integer or Clock")

    @classmethod
    def __get_formated(cls, value):
        return str(value).rjust(2, "0")

    def __add__(self, other):
        return Clock(self.seconds + other)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.seconds = (self.seconds + self.__get_seconds(other)) % self.__DAY
        return self

    def __sub__(self, other):
        return Clock(self.seconds - other)

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):
        self.seconds = (self.seconds - self.__get_seconds(other)) % self.__DAY
        return self

    def __mul__(self, other):
        return Clock(self.seconds * other)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.seconds = (self.seconds * other) % self.__DAY
        return self

    def __truediv__(self, other):
        return Clock(self.seconds / other)

    def __rtruediv__(self, other):
        return self / other

    def __itruediv__(self, other):
        self.seconds = (self.seconds / other) % self.__DAY
        return self

    def __floordiv__(self, other):
        return Clock(self.seconds // other)

    def __rfloordiv__(self, other):
        return self // other

    def __ifloordiv__(self, other):
        self.seconds = (self.seconds // other) % self.__DAY
        return self

    def __mod__(self, other):
        return Clock(self.seconds % other)

    def __rmod__(self, other):
        return self % other

    def __imod__(self, other):
        self.seconds = (self.seconds % other) % self.__DAY


c1 = Clock(1030)
c1 -= 1000
print(c1.get_type())
