max = 0
min = 10 
while True:
    n = int(input())
    if n == -1:
        break
    if n > max:
        max = n
    if n < min:
        min = n
print (max, min)
