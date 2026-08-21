# class Geom:
#     name = "Geom"
#
#     def __init__(self, x1, y1, x2, y2):
#         print(f"Инициализатор Geom для {self.__class__}")
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#
#
# class Line(Geom):
#
#     def draw(self):
#         print("Line")
#
#
# class Rect(Geom):
#     def __init__(self, x1, y1, x2, y2, fill=None):
#         super().__init__(x1, y1, x2, y2)
#         print("Rect")
#         self.fill = fill
#
#     def draw(self):
#         print("Rect")
#
#
# l = Line(0, 0, 19, 10)
# r = Rect(0, 0, 19, 10)


class Book:
    def __init__(self, title, author, pages, year):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year


class DigitBook(Book):
    def __init__(self, title, author, pages, year, size, frm):
        super().__init__(title, author, pages, year)
        self.size = size
        self.frm = frm


book1 = Book("Евгений Онегин", "Пушкин", 666, 1830)
book2 = DigitBook("Борис Годунов ", "Пушкин", 777, 1825, 1024, "fb2")
print(book1.__dict__)
print(book2.__dict__)
