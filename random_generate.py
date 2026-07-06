# import random
# random.seed(1)
# s = list(map(int, input().split()))
# res = random.uniform(*s)
#
# print(round(res, 2))
import random
random.seed(1)
s = list(map(int, input().split()))
res  = random.randint(*s)

print(res)