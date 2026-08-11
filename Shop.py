class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    start_uid = 0

    def __init__(self, name, weight, price):
        Product.start_uid += 1
        self.uid = Product.start_uid
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key == "name" and not isinstance(value, str):
            raise TypeError("Неверный тип присваиваемых данных.")
        if key in ("weight", "price") and (
            not isinstance(value, (int, float)) or value < 0
        ):
            raise TypeError("Неверный тип присваиваемых данных.")
        if key == "uid" and not isinstance(value, int):
            raise TypeError("Неверный тип присваиваемых данных.")

        object.__setattr__(self, key, value)

    def __delattr__(self, key):
        if key == "uid":
            raise AttributeError("Атрибут uid удалять запрещено.")
        object.__delattr__(self, key)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 123, 123))
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}")
