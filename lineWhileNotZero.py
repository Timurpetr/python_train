lst = 0
max_sum = 0
while True:
    i = input()
    if i == "0":
        break
    lst = max(int(i), lst + int(i))
    max_sum = max(max_sum, lst)

print(max_sum)
