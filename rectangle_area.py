def func_show(func):
    def wrapper(*args):
        result = func(*args)
        print(f"Площадь прямоугольника: {result}")
        return result
    return wrapper


def get_sq(width, height):
    return  width * height

