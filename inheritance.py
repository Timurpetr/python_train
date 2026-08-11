# class Geom:
#     name = "Geom"
#
#     def self_cords(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#         self.draw()
#
#
# class Line(Geom):
#     name = "Line"
#
#     def draw(self):
#         print("Рисование линии")
#
#
# class Rect(Geom):
#     name = "Rect"
#
#     def draw(self):
#         print("Рисование прямоугольника")
#
#
# g = Geom()
# r = Rect()
# l = Line()
# print(l.name)
# print(r.name)
# class Style:
#     def __init__(self, color, size):
#         self.color = color
#         self.size = size
#
#
# class Window(Style):
#     def __init__(self, color, size, material, model):
#         super().__init__(color, size)
#         self.material = material
#         self.model = model
#
#
# wnd = Window("white", 100, "wood", "the best window")
# print(wnd.__dict__)  # {'material': 'wood', 'model': 'the best window'}
