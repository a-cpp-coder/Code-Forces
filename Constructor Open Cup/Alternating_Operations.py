t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # print(a[0] + n - 1)
    # fuck it, i go brute-force to test the possibility, correctness 
    # step = 1
    # max = a[0]
    # for i in range(100):
    #     if step % 2 != 0:
    #         for i in range(len(a) - 1):
    #             for j in range(i + 1, len(a)):
    #                 if a[j] > 0

    # Tired, Exhausted, I remember the old days with Hanoi Tower problem
    if n == 2:
        print(a[0] + 1)
    else:
        print(sum(a))
