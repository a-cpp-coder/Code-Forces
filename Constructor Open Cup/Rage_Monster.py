# import itertools

t = int(input())

for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))

    damage = 0
    base_damage = 1
    s.sort()
    even = []
    odd = []
    for i in range(len(s)):
        if (i + 1) % 2 == 0:
            even.append(s[i])
        else:
            odd.append(s[i])
    
    even.sort(reverse=True)
    result = even + odd
    # print(result)
    
    for i in result:
        damage += n * base_damage * i
        n -= 1
        base_damage += 1
    print(damage)

    # flip = 0
    # s.sort(reverse=True)
    # s.sort()
    
    
    # print(perm_s) # go crazy for checking the solution
        # print(perm_s)
    
    # using bruteforce to see the pattern of solution
    # perm_s = list(itertools.permutations(s))
    # min_damage = 100000
    # for p in perm_s:
    #     damage = 0
    #     base_damage = 1
    #     for i in range(len(p)):
    #         damage += (len(p) - i) * base_damage * p[i]
    #         base_damage += 1

    #     if(damage < min_damage):
    #         min_damage = damage
    #         print(p, min_damage)

    # while(s):
    #     # if _ == 3:
    #     #     print(s, damage)
    #     # if flip == 0:
    #     #     s.sort()
    #     #     flip = 1
    #     # else:
    #     #     s.sort(reverse=True)
    #     #     flip =0
        
        # damage += len(s) * base_damage * s[-1]
        # base_damage += 1
        # s.pop()
    
    # print(min_damage)