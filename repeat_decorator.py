def multiply_result(times):
    def decor(f):
        def wrapper(*args, **kwargs):
            res = f(*args, **kwargs)
            if isinstance(res, int):
                return res * times
            else:
                return res
        return wrapper
    return decor








@multiply_result(times=3)
def get_bonus():
    return 500

@multiply_result(times=2)
def get_greet():
    return "Code"

print(get_bonus())  # Ожидается: 1500
print(get_greet())  # Ожидается: CodeCode