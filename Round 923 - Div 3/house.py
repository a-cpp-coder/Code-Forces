t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))
    # print(arr)
    if min(arr[0], arr[1]) <= arr[2] <= max(arr[0], arr[1]):
        print("YES")
    else:
        print("NO")