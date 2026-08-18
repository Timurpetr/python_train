class Validator:

    def _is_valid(self, data):
        if data:
            return True
        else:
            return False

    def __call__(self, data):
        if self._is_valid(data):
            return data
        else:
            raise ValueError("данные не прошли валидацию")


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if isinstance(data, int) and self.min_value <= data <= self.max_value:
            return True
        else:
            return False


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if isinstance(data, float) and self.min_value <= data <= self.max_value:
            return True
        else:
            return False


v = Validator()

integer_validator = IntegerValidator(-10, 10)
float_validator = FloatValidator(-1, 1)
res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
res2 = float_validator(-0.2)  # исключение не генерируется (проверка проходит)
res3 = float_validator(10)
print(res1)
print(res2)
