n = int(input())

for _ in range(n):
    string = input()
    count_A, count_B = 0, 0
    for i in string:
        if i == "A":
            count_A += 1
        else:
            count_B += 1

        if count_A == 3 or count_B == 3:
            break
    
    if count_A == 3:
        print("A")
    else:
        print("B")
