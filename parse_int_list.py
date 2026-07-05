s = input()

def decor(f):
    def wrapper(*args,**kwargs):
        in_lst = f(*args,**kwargs)
        lst = sorted(in_lst)
        print(*lst)
        return lst
    return wrapper


@decor
def get_list(func):
    return list(map(int, func.split()))


get_list(s)