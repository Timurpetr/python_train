class DigitRetrieve:
    def __call__(self, string, *args, **kwargs):
        if string[0] == "-":
            if string[1:].isdigit():
                return int(string)
        elif string.isdigit():
            return int(string)
        return None


dg = DigitRetrieve()

st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))  # [123, None, None, 0, -5]
