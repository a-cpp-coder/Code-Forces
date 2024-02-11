n = int(input())
for _ in range(n):
    length = int(input())
    strip = input()

    pos1 = strip.find("B")
    pos2 = strip.rfind("B")
    result = pos2 - pos1 + 1
    print(result)
    