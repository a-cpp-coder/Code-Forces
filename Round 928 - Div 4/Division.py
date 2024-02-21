from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    result = 0
    test = defaultdict(int)

    for i in arr:
        if test[i] == 0:
            result += 1
            test[(pow(2, 31) - 1) ^ i] += 1
        else:
            test[i] -= 1
    
    print(result)

    # arr = [bin(x)[2:].zfill(31) for x in arr]
    # result = n
    # i = 0
    # while(i < n):
    #     for j in range(i + 1, n):
    #         # test = ''.join('0' if i == j else '1' for i, j in zip(arr[i], arr[j]))
    #         # if test == "1111111111111111111111111111111":
    #         # print((pow(2, 31) - 1) ^ arr[j] , arr[i])
    #         if arr[i] == (pow(2, 31) - 1) ^ arr[j]:
    #             result -= 1
    #             del arr[j]
    #             del arr[i]
    #             n -= 2
    #             i = -1
    #             break
    #     i += 1


    # test = int(arr[i],2) ^ int(arr[j],2)

    # power_list = [pow(2, x)-1 for x in range(1, 32)]
    # # print(power_list)

    # while(len(arr) > 0):
    #     for i in range(1, len(arr)):
    #         test = ''.join('0' if i == j else '1' for i, j in zip(arr[0], arr[i]))
    #         if test == "1111111111111111111111111111111":
    #             result += 1
    #             del arr[0]
    #             del arr[i]
    #             break


    # stack = []
    # for i in range(n - 1):
    #     if i in stack:
    #         continue
    #     for j in range(i + 1, n):
    #         if j in stack:
    #             continue
    #         test = ''.join('0' if i == j else '1' for i, j in zip(arr[i], arr[j]))
    #         # print(test)
    #         if test == "1111111111111111111111111111111":
    #             result -= 1
    #             stack.append(j)
    #             break
    # test