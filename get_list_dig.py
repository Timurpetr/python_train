def get_list_dig(lst):
    int_list = list(filter(lambda x: (type(x) is int or type(x) is float) and type(x) is not bool, lst))
    return [x for x in int_list]