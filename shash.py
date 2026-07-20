# def triangle(a, b, c, /, mul, offset=0):
#     return (a + b + c) * mul + offset
#
#
# res2 = triangle(2, 3, 4, 4, 2)
# print(res2)

# import re
#
#
# def parser_data(text, /, max_count=0, *, ignore_sign=False):
#     found_numbers = re.findall(r"-?\d+", text)
#     new_text = [int(n) for n in found_numbers]
#
#     if ignore_sign:
#         new_text = [str(abs(i)) for i in new_text]
#     if max_count > 0:
#         new_text = new_text[:max_count]
#
#     return new_text
#
#
# data_text = input()
#
# result = parser_data(data_text, max_count=5, ignore_sign=True)


# def is_right_rect(a, b, c, d, /, *, precision=0.001):
