n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if (a - b) % 2 == 0 and (a - b) >= 0:
        print ("YES")
    else:
        print ("NO")
