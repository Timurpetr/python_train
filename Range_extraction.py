def solution(args):
    res = []

    for i in range(len(args) - 1):
        if args[i] == args[i + 1] - 1:
            res.append(args[i])

    res_2 = []
    for i in range(len(args) - 1):
        if args[i] < 0:
            while abs(args[i + 1]) - abs(args[i]) == 1:
                res_2.append(args[i])

    print(res)
    print(res_2)

print(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))