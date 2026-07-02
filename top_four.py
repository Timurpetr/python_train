

s = input().split()
unique_ints = set(int(x) for x in s)
result = sorted(unique_ints, reverse=True)
print(*result[:4])