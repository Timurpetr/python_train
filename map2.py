# from os import replace
#
# s = str(input())
#
# liters = ["b", "i", "t", "B", "I", "T"]
#
# res = ["#" if i in liters else i for i in s]
#
# print(*res, sep="")


# s = list(map(int, input().split()))
#
# digits = [i for i in s if i > 0]
# result = [True if i % 7 == 0 else False for i in s]
# print(*result)

s = input()
s_lst = s.split()

tp = tuple(map(lambda x: tuple(x.split("=")), s_lst))
