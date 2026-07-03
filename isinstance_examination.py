def get_add(a, b):
    if isinstance(a, str) and isinstance(b, str):
        return a + b
    elif isinstance(a, bool) or isinstance(b, bool):
        return None
    elif isinstance(a, (int,float)) and isinstance(b, (int,float)):
        return  a + b
    else:
        return None


print(get_add(True, 1))