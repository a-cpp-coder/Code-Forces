import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter
    
for _ in range(int(input())):
    n = int(input())
    cnt = Counter(sorted(map(int, input().split())))
    for k in cnt:
        if k < 2147483647 >> 1 and 2147483647 - k in cnt:
            n -= min(cnt[2147483647 - k], cnt[k])
    print(n)