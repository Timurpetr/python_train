
def get_sort(d):
    sorted_keys  = sorted(d.keys(), reverse=True)
    return [d[k] for k in sorted_keys]

print(get_sort({'cat': 'кот', 'horse': 'лошадь', 'tree': 'дерево', 'dog': 'собака', 'book': 'книга'}))