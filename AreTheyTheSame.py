# from collections import Counter
#
# def comp(array1, array2):
#     if array1 is None or array2 is None or len(array1) != len(array2):
#         return False
#     return Counter(a**2 for a in array1) == Counter(array2)


def comp(array1, array2):
    if array1 is None or array2 is None or len(array1) != len(array2):
        return False
    array2_copy = list(array2)
    for a in array1:
        sq = a**2
        if sq in array2_copy:
            array2_copy.remove(sq)
        else:
            return False
    return True
