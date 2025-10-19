n = int(input())
arr = list(map(int, input().split()))

for x in arr:
    if x == 0:
        print("NO")
        break
else:
    print("YES")
