s = input()
s_lst = s.split()

tp = tuple(map(lambda _: tuple(_.split('=')), s_lst ))
print(tp)