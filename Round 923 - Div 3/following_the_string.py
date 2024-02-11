from collections import defaultdict

t = int(input())
alpha = "abcdefghijklmnopqrstuvwxyz"

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # print(a)
    result = ""
    index = 0
    counter = defaultdict(int)
    for i in a:
        if i == 0:
            result += alpha[index]
            counter[alpha[index]] += 1
            index += 1
        else:
            key_list = list(counter.keys())
            value_list = list(counter.values())
            pos = value_list.index(i)
            result += key_list[pos]
            counter[key_list[pos]] += 1
    
    print(result)