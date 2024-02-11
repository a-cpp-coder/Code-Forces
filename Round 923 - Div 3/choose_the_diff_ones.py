n = int(input())

for _ in range(n):
    n, m, k = map(int,input().split())
    # print(n, m, k)
    arr1 = list(map(int, input().split()))
    # print(arr1)
    arr2 = list(map(int, input().split()))
    # print(arr2)
    arr1 = [x for x in arr1 if x <= k and x >= 1]
    # print(arr1)
    arr2 = [x for x in arr2 if x <= k and x >= 1]
    # print(arr2)
    k_2 = k/2
    arr1 = set(arr1)
    # print(arr1)
    arr2 = set(arr2)
    # print(arr2)
    uni = arr1 | arr2
    # print(uni)
    inter = arr1 & arr2
    test = set(list(range(1, k + 1)))
    # print(test)
    arr1_diff = arr1 - arr2
    # print(arr1_diff)
    arr2_diff = arr2 - arr1
    # print(arr2_diff)
    if uni == test and len(arr1_diff) >= k_2 - len(inter) and len(arr2_diff) >= k_2 - len(inter):
        print("YES")
    else:
        print("NO")


