class Shop:
    def __init__(self, name, goods):
        self.name = name
        self.goods = goods

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    def __init__(self, uid, name, weight, price):
        self.uid = uid
        self.name = name
        self.weight = weight
        self.price = price
