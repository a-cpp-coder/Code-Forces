t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    n1 = arr[0] % 10
    n2 = arr[1] % 10
    # print(n1, n2)
    d1 = min(abs(arr[2] - n1), 10 - abs(arr[2] - n1))
    d2 = min(abs(arr[2] - n2), 10 - abs(arr[2] - n2))
    # print(d1, d2)
    # d2 = min(abs(arr[2] - n2) - 1, (arr[2] + 10 - n2 - 1)%10)
    # print((arr[2] + 10 - n1 - 1)%10)
    # print(d1)
    # d2 = min(abs(n2 - arr[2]) - 1, (n2 + 10 - arr[2] - 1)%10)
    # print(d2)
    if d1 == d2:
        print("YES")
    else:
        print("NO")
    # print(s)
    # if s == arr[2]:
    #     print("YES")
    # elif arr[2] != 0 and s % arr[2] == 0:
    #     print("YES")
    # else:
    #     print("NO")