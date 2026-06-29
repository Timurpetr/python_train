z = zip(map(int,(input().split())),map(int,(input().split())))
multiplied_iterator = (x[0] * x[1] for x in z)
print(*(next(multiplied_iterator) for _ in range(3)))