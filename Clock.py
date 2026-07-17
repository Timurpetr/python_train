class Clock:

    def __init__(self, tm):
        __time = 0
        self.set_time(tm)

    @staticmethod
    def __chek_time(tm):
        return isinstance(tm, int) and 100000 > tm >= 0

    def set_time(self, tm):
        if self.__chek_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time


clock = Clock(4530)

print(clock.get_time())
