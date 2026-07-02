a = list(map(int, input().split()))
b = list(map(int, input().split()))
sortA = sorted(a)
sortB = sorted(b, reverse=True)
sortSum = [x + y for x,y in zip(sortA,sortB)]
print(*sortSum)
