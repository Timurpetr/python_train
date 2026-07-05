lst_in = ['#', 'x', 'o', 'x', 'x', 'x', 'o', 'o', 'x']

pole = [list( s.split()) for s in lst_in]

def is_free(lst):
    return True if any(any(x == '#' for x in y) for y in lst) else False



print(is_free(pole))