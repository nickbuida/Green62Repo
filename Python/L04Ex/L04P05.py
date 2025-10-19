def largestDigit(n):
    max = 0
    while n > 0:
        x = n % 10
        if x > max:
            max = x
        n //= 10
    return max

n = int(input())
print(largestDigit(n))