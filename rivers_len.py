s = list(input().split())
descending_order = sorted(s, key = len, reverse = True)
print(*descending_order)