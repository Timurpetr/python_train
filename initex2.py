# class TriangleChecker:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         match (self.a, self.b, self.c):
#             case (a, b, c) if not (
#                 type(a) in (int, float)
#                 and type(b) in (int, float)
#                 and type(c) in (int, float)
#             ):
#                 return 1
#             case (a, b, c) if a <= 0 or b <= 0 or c <= 0:
#                 return 1
#             case (a, b, c) if a >= b + c or b >= a + c or c >= a + b:
#                 return 2
#             case _:
#                 return 3
#
#
# a, b, c = map(int, input().split())
# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())


class Graph:
    def __init__(self, data, is_show=True):
        self.is_show = is_show
        self.data = data.copy()

    def set_data(self, data):
        self.data = data.copy()

    def show_table(self):
        if self.is_show == False:
            print("Отображение данных закрыто")
        else:
            print(self.data)

    def show_graph(self):
        if self.is_show == False:
            print("Отображение данных закрыто")
        else:
            print("Графическое отображение данных:", *self.data)

    def show_bar(self):
        if self.is_show == False:
            print("Отображение данных закрыто")
        else:
            print("Столбчатая диаграмма:", *self.data)

    def set_show(self, fl_show):
        self.is_show = fl_show


data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()
