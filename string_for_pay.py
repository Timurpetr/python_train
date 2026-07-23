class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f"{gd.name}: {gd.price}" for gd in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
cart.add(TV("Samsung UE55AU7100", 54990.0))
cart.add(TV("LG OLED B3", 129990.0))
cart.add(Table("IKEA LACK", 1499.0))
cart.add(Notebook("MacBook Air M3", 109990.0))
cart.add(Notebook("ASUS Zenbook", 89990.0))
cart.add(Cup("Керамическая кружка", 399.0))
print(cart.get_list())
