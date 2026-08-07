# lst = "UUDDDUU"
# down = 0
# Up = 0
# res = [x for x in lst]
# print(down)

lst = "DDUDUUDDUU"


# def func(str):
#     i = 0
#     lst = [i for i in str]
#     start = 0
#     while i < len(lst) - 2:
#         if lst[i] == "D" and lst[i + 1] == "U" and lst[i + 2] != "D":
#             start += 1
#         i += 1
#     return start
#
#
# print(func(lst))


def func(str):
    level = 0
    valley = 0
    for step in str:
        if step == "D":
            if level == 0:
                valley += 1
            level -= 1
        else:
            level += 1
    return valley


print(func(lst))
