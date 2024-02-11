t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    b = list(map(int, input().split()))
    a = list(range(1, n + 1))
    diff = [x for x in a if x not in b]
    # print(diff)
    result = " ".join(str(i) for i in diff[::-1])
    print(result)