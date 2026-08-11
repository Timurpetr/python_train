class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cat(Animal):
    def __init__(self, name, age, color, weight):
        super().__init__(name, age)
        self.color = color
        self.weight = weight

    def get_info(self):
        return f"{self.name}: {self.age}, {self.color}, {self.weight}"


class Dog(Animal):
    def __init__(self, name, age, breed, size):
        super().__init__(name, age)
        self.breed = breed
        self.size = size

    def get_info(self):
        return f"{self.name}: {self.age}, {self.breed}, {self.size}"


cat = Cat("кот", 4, "black", 2.25)
print(cat.get_info())
