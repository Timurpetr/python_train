from functools import wraps

def sum_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return sum(f(*args, **kwargs))
    return wrapper


@sum_decorator
def get_list(param):
    '''Функция для формирования списка целых значений'''
    return list(map(int, param.split()))

