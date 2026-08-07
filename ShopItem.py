import sys


class ShopItem:
    def __init__(self, name: str, weight: int | float, price: int | float):
        self.name = name
        self.weight = weight
        self.price = price

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))

    def __eq__(self, other):
        return (self.name.lower(), self.weight, self.price) == (
            other.name.lower(),
            other.weight,
            other.price,
        )


lst_in = list(map(str.strip, sys.stdin.readlines()))


shop_items = {}

for line in lst_in:
    name_part, numbers_part = line.split(":")
    name = name_part.strip()

    numbers = numbers_part.split()
    weight = float(numbers[0]) if "." in numbers[0] else int(numbers[0])
    price = float(numbers[1]) if "." in numbers[1] else int(numbers[1])

    obj = ShopItem(name, weight, price)

    if obj in shop_items:
        shop_items[obj][1] += 1
    else:
        shop_items[obj] = [obj, 1]
