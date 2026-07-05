# def fun(a, b):
#     return a + 2 * b


def dumper(f):
    def newf(*args):
        res = f(*args)
        print(res)
        return res

    return newf


# fun = dumper(fun)  # Вот так не понятно что то идет наверху и тд а что то внизу
# fun(3, 5)


@dumper  # для удобства обозначения для других програмистов можно писать собаку декоратор и тд.
def mulmul(a, b):
    return a * b


mulmul(3, 5)


# @decor(param)
#
# def fun(a, b):
#     return a + b * 2
#
# @dumper
# def mulmul(a, b):
#     return a * b
#
#
# res = mulmul(3, 5)


# То же самое что и

def mulmul(a, b):
    return a * b


# mulmul = dumper(mulmul)  # оборачиваем функцию
# res = mulmul(3, 5)  # вызываем обёртку
def decorator(func):
    def wrapper():
        print("До вызова")
        func()
        print("После вызова")
    return wrapper

@decorator
def say_hello():
    print("Привет!")

say_hello()



# Универсальная структура декораторов:
def decorator(func):
    def wrapper(*args, **kwargs):
        # Действия до вызова (например, логирование)
        result = func(*args, **kwargs)   # вызываем исходную функцию
        # Действия после вызова
        return result                    # возвращаем результат
    return wrapper