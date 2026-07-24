class Book:
    def __init__(self, title="", author="", pages=0, year=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        expected_types = {"title": str, "author": str, "pages": int, "year": int}

        if key in expected_types:
            if not isinstance(value, expected_types[key]):
                raise TypeError("Неверный тип присваиваемых данных.")

        object.__setattr__(self, key, value)
