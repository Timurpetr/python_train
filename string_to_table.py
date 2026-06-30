cities = input().split()
table = [s.split() for s in cities]
row = zip(*zip(*table))
for _ in range(3):
    print(*(next(row)[0] for _ in range(3)))
