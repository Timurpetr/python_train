class Point:
    color = "red"
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y


pt = Point()
Point.set_coords(pt, 1, 2)
# print(pt.__dict__)


class MediaPlayer:
    def open(self, file):
        self.filename = file

    def play(self):
        print(f"Воспроизведение {self.filename}")


media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open("filemedia1")
media2.open("filemedia2")

media1.play()
media2.play()


class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        res = [x for x in self.data if self.LIMIT_Y[0] < x < self.LIMIT_Y[1]]
        print(*res)


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()


import sys


class StreamData:
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False
        else:
            for field, value in zip(fields, lst_values):
                setattr(self, field, value)
            return True


class StreamReader:
    FIELDS = ("id", "title", "pages")

    def readlines(self):
        lst_in = list(
            map(str.strip, sys.stdin.readlines())
        )  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
