class Money:

    def __init__(self, money):
        self.__money = 0
        self.set_money(money)

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.get_money()

    @staticmethod
    def __check_money(money):
        return isinstance(money, int) and money >= 0

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money


mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()  # 100
m2 = mn_2.get_money()
print(f"m1: {m1} (Ожидалось: 100)")
print(f"m2: {m2} (Ожидалось: 120)")
