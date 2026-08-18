# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class Student(Person):
#     def __init__(self, name, age, course):
#         super().__init__(name, age)
#         self.course = course
#
#
# s = Student("Alex", 25, "Python")
# print(s.name, s.age, s.course)


class Player:
    def attack(self, target):
        return f"Атака {target}"

    def defend(self, target):
        return f"Защита от {target}"

    def heal(self, target):
        return f"Лечение {target}"


class Game:
    def execute(self, player, action, target):
        method = getattr(player, action.lower(), None)

        if not callable(method):
            raise TypeError("Неизвестное действие")

        return method(target)


player = Player()
game = Game()
print(game.execute(player, "ATTACK", "дракон"))
