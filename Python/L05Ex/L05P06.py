n = int(input())
arr = list(map(int, input().split()))
 
min = 100000
sum = 0
 
for x in arr:
    if x < min:
        min = x
    sum += x
 
result = sum - min * n
print(result)