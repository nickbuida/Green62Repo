def multiply(x):
    total = 0
    for i in range(x + 1):
        total += i**2
    return total

n = int(input())
print(multiply(n))