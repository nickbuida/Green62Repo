n = int(input())
max_apple = 0
max_orange = 0
basket = 0

for i in range(n):
    a, b = map(int, input().split())
    if a > max_apple or (a == max_apple and b > max_orange):
        max_apple = a
        max_orange = b
        basket = i + 1  

print(basket)
