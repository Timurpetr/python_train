s = input()


def double_sum(start):
    def add_start(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs) + start
            return res

        return wrapper

    return add_start


@double_sum(start=5)
def func_trans(stroke):
    return sum(list(map(int, stroke.split())))


print(func_trans(s))
