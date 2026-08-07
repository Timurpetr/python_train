# def descending_order(num):
#     lst = [i for i in str(num)]
#     sort_lst = sorted(lst, reverse=True)
#     result = int("".join(sort_lst))
#
#     return result
#
#
# print(descending_order(4214))


# def is_square(n):
#     if n < 0:
#         return False
#     elif n**0.5 == int(n**0.5):
#         return True
#     return False
#
#
# print(is_square(25))


# def make_negative(number):
#     if number < 0:
#         return number
#     else:
#         return -number


# def accum(st):
#     lst = [i.lower() for i in st]
#     return "-".join(item.upper() + item.lower() * j for j, item in enumerate(lst))
#
#
# print(accum("abcd"))


# def basic_op(operator, value1, value2):
#     if operator == "+":
#         return value1 + value2
#     elif operator == "-":
#         return value1 - value2
#     elif operator == "*":
#         return value1 * value2
#     elif operator == "/":
#         return value1 / value2
#
#
# print(basic_op("+", 4, 7))


def split_by_mask(strng, mask):
    if len(strng) <= 0 or len(strng) != sum(mask):
        return []
    res = []
    start = 0
    for num in mask:
        res.append(strng[start : start + num])
        start += num
    return res


print(split_by_mask("codewars", (4, 4)))
