from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    result = 0
    count = defaultdict(int)

    for i in arr:
        if count[i] == 0:
            result += 1
            count[(pow(2, 31) - 1) ^ i] += 1
        else:
            count[i] -= 1
    
    print(result)