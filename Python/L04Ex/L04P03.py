def gcd(a,b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

a, b = map(int, input().split())
gcd(a,b)

c = a // gcd(a,b)
d = b // gcd(a,b)

print(c, d)