s = input()
sr = list(map(str, s.split()))
sr.sort(key=int)
lst = [int(item) for item in sr]
numbers_tuple = tuple(lst)
tp_lst = tuple(sorted(numbers_tuple, key=int))
print(lst)