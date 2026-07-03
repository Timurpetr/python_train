s = list(map(float,input().split()))

print(any(x < 0 for x in s))