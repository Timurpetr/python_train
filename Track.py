# __eq__() – для равенства ==
# __ne__() – для неравенства !=
# __lt__() – для оператора меньше <
# __le__() – для оператора меньше или равно <=
# __gt__() – для оператора больше >
# __ge__() – для оператора больше или равно >=


class Track:
    def __init__(self, start_x, start_y):
        if not isinstance(start_x, (int, float)) or (
            not isinstance(start_y, (int, float))
        ):
            raise TypeError("start_x must be int or float")
        self.start_x = start_x
        self.start_y = start_y

    def add_track(self, tr):
        pass

    def get_tracks(self):
        pass


class TrackLine:
    def __init__(self, to_x, to_y, max_speed: int):
        if not isinstance(to_x, (int, float)) or not isinstance(to_y, (int, float)):
            raise TypeError("to_x must be int or float")
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed
