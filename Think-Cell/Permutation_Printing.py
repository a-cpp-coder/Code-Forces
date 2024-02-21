import itertools

t = int(input())

def test(p, n):
    for i in range(n - 1):
        for j in range(n -1):
            if i != j and p[i] % p[j] == 0 and p[i + 1] % p[j+1] == 0:
                return 1


for _ in range(t):
    n = int(input())
    arr = list(range(1, n + 1))
    perm = list(itertools.permutations(arr))
    for p in perm:
        if test(p, n) == 1:
            continue
        else:
            arr = p
            break

    # begin = []
    # end = [1, 2, 3]
    # for i in range(4, n + 1):
    #     if i % 2 == 0:
    #         begin.insert(0, i)
    #         # print(begin)
    #     else:
    #         end.append(i)
    # arr = begin + end
    # if n >= 18:
    #     i = arr.index(18)
    #     j = arr.index(16)
    #     arr[i], arr[j] = arr[j], arr[i]
        
    # print(test(arr, n))

    # test = 1
    # while(test):
    #     for i in range(n - 1):
    #         for j in range(n - 1):
    #             if i != j and arr[j] % arr[i] and arr[j+1] % arr[i+1]:
    #                 print(arr)
    #                 arr[i], arr[j] = arr[j], arr[i]
    #                 print(arr)

                    # print(arr)
                    # if i == n - 1 and j == n - 1:
                    #     test = 0
                    # break
            # break
        

    # arr.sort()
    # arr.insert(0, arr.pop())
    # l = list(itertools.permutations(arr))
    result = " ".join([str(x) for x in arr])
    print(result)


    # begin = []
    # end = [1, 2, 3]
    # for i in range(4, n + 1):
    #     if i % 2 == 0:
    #         begin.insert(0, i)
    #         # print(begin)
    #     else:
    #         end.append(i)
    # arr = begin + end
    # 