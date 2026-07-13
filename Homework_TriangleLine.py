# a, b, c = map(int, input().split())
# if a < b + c and b < a + c and c < a + b:
#     print(False)
# else:
#     print(True)

print(True if sum(s := list(map(int, input().split()))) - max(s) > max(s) else False)
print(dir(s))
