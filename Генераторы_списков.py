from math import floor

lst = list(map(float,input().split()))

lst_res = [a for a in lst if int(a) % 2 == 0]
print(*lst_res)

