def get_sum(it):
    int_list = list(filter(lambda x: type(x) is int, it))

    return sum(x for x in int_list) if int_list else 0


print(get_sum([1,2,3, "a", True, [4, 5], "c", (4, 5)]))
print(get_sum({5, 6, 7, '8', 5, '4'}))
print(get_sum((10, "f", '33', True, 12)))
print(get_sum(['1', True, False, (1, 23)]))