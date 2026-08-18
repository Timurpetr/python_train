class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance


class Game(Singleton):
    def __init__(self, name):
        if not hasattr(self, "name"):
            self.name = name


game = Game("name")
print(game.name)
