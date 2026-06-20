def f(x):
    return abs(x) ** 0.5 + 3.2 + x


t = tuple(map(float, input().split()))

lst = [[fx := f(x), fx ** 2 , fx ** 3] for x in t]

print(*lst)