inNum = list(map(int, input().split()))

twoDigit = filter(lambda x: 10 <= abs(x) <= 99, inNum)

print(*list(twoDigit))