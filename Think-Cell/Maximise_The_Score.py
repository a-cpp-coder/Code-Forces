t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    arr.sort()
    result = sum(arr[::2])
    # result = sum(num for num in arr if not num%2)
    # sum(filter(lambda x: not x%2, myList))
    print(result)