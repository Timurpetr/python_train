def babble_sort(lst):
    i = len(lst)
    x = 0
    flag = False
    while x < i:
        j = x + 1
        if lst[x] > lst[j]:
            lst[x], lst[j] = lst[j], lst[x]
            flag = True
        x += 1
        if x == i - 1:
            if flag:
                x = 0
                flag = False
            else:
                break
    return lst


print(babble_sort([5, 3, 1, 2, 3, 4, 5, 7, 8, 19, 20, 31]))
