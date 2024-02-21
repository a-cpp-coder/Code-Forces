t = int(input())

def dsum(n, f=1, p=1):
    if n:
        d, r = divmod(n, 10)
        k = (45*d + sum(range(r)))*f + r*p
        return dsum(d, f*10, p + f*r) + k
    return 0


for _ in range(t):
    n = int(input())
    # a_list = list(range(1, n + 1))
    # result = sum(int(c) for i in a_list for c in str(i))
    result = dsum(n)
    print(result)

