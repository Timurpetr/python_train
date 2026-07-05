s = list(map(int, input().split()))

# if all(x > 2 for x in s):
#     print("учится")
#
# else:
#     print("отчислен")
#

print('учится' if all(x > 2 for x in s) else 'отчислен')