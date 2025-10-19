n = int(input())
max = 0
sum = 0

for i in range(n):
    a = int(input())
    if a > max:
        max = a
    sum += a

total = n * max - sum
print(total)
