n = int(input())
total = 0
cap = 0
for i in range(n):
    a, b = map(int, input().split())
    total += b - a
    if total > cap:
        cap = total
print(cap)