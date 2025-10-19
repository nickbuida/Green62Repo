n, m = map(int, input().split())
# n = a ** 2 + b // original 
count = 0

for a in range (0, 1001):
    b = n - a ** 2
    if m == a + b ** 2:
        count += 1
    

print(count)