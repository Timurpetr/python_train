# import string
#
#
# def is_pangram(st):
#     alphabet = list(string.ascii_lowercase)
#     letters = set(st.lower())
#     i = 0
#     for x in alphabet:
#         if x in letters:
#             i += 1
#         else:
#             continue
#     return i == 26
#
#
# st = "The quick brown fox jumps over the lazy dog"
# print(is_pangram(st))
# def get_count(sentence):
#     count = 0
#     for letter in sentence:
#         if letter in ("a", "e", "i", "o", "u"):
#             count += 1
#     return count
#
#
# print(get_count("aeiou"))

import math


def persistence(n):
    res = [int(n) for n in str(n)]
    count = 0
    while len(res) > 1:
        res = math.prod(res)
        res = [int(n) for n in str(res)]
        count += 1
    return count


print(persistence(39))
