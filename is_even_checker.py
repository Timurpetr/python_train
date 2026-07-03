s = list(map(int,input().split()))

print(all(x % 2 == 0 for x in s))