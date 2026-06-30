lst_in = ['1 2 3 4',
          '5 6 7 8',
          '9 8 7 6']

table = [s.split() for s in lst_in]

for row in zip(*table):
    print(*row)