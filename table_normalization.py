
lst_in = ['1 2 3 4 5 6', '3 4 5 6', '7 8 9', '9 7 5 3 2']
table = [s.split() for s in lst_in]
for row in zip(*zip(*table)):
    print(*row)