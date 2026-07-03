def get_even_sum(it):
    int_list = list(filter(lambda x: type(x) is int and x % 2 == 0, it))
    return sum(x for x in int_list) if int_list else 0