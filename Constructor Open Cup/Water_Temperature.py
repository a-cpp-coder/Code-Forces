cases = int(input())

for _ in range(cases):
    n, l, r, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    # print(a)

    current = k
    time = 0
    
    for i in range(1, n + 1):
        if(l <= current <= r):
            break
        if (current < l):
            current = current + (a[i] - a[i - 1])
            time = a[i]
            # print(current, time, a[i] - a[i - 1], i, end="|")
        else:
            current = current - (a[i] - a[i - 1])
            time = a[i]
            # print(current, time, a[i] - a[i - 1], i,  end="|")

    if (current < l or current > r):
        time = -1
    print(time)

