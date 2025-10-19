def countDigit(n):
    ans = 0
    while n > 0:
        n //= 10
        ans += 1
    return ans

n = int(input())
print(countDigit(n))