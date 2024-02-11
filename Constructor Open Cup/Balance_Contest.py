t  = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    # it's math, the lowest number of task (if possible) is always the number of students (just can reduce from n + x to n)
    i, j = 0, 0
    result = []
    while(i < n):   # and j < m
        count = 0
        while (j < m and a[i] >= b[j]):
            count += 1
            j += 1

        if count == 0:
            break
        else:
            i = i + 1
            result.append(j)
    
    if(i < n):
        print("-1")
    else:
        print(n)
        print(" ".join(str(x) for x in result))


