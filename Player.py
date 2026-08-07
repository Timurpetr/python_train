class Player:
    def __init__(self, name: str, age: int, score: int):
        self.name = name
        self.age = age
        self.score = score

    def __bool__(self):
        return self.score > 0


lst_in = ["Балакирев; 34; 2048", "Mediel; 27; 0", "Влад; 18; 9012", "Nina P; 33; 0"]

players = []
for item in lst_in:
    name, age, score = item.split("; ")
    players.append(Player(name, int(age), int(score)))

players_filtered = [x for x in players if x.score > 0]
