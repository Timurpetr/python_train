notes = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

s = list(input().split())

result = sorted(s,key=lambda x: notes.index(x))
print(*result)