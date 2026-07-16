class Factory:
    @staticmethod
    def build_sequence():
        empty_string = []
        return empty_string

    @staticmethod
    def build_number(number):
        return int(number)


class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


res = Loader.parse_format("4, 5, -6", Factory)
print(res)
print(Factory.build_sequence())
