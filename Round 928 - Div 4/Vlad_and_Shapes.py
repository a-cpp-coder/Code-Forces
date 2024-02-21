t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        row = input()
        # print(row)
        # for j in range(n):
        #     x = int(input())
        #     row.append(x)
        arr.append(row)
    
    last = 0
    for j in range(n):
        if(arr[j].count("1") > 0):
            if last == 0:
                last = arr[j].count("1")
                continue

            if last > 0 and arr[j].count("1") != last:
                print("TRIANGLE")
                break
            else:
                print("SQUARE")
                break

            



        
