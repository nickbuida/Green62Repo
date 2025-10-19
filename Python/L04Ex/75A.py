a = int(input())
b = int(input())
c = a + b

def remove_zeros(x):
    result = 0
    place = 1
    while x > 0:
        digit = x % 10
        if digit != 0:
            result += digit * place
            place *= 10
        x //= 10
    return result

a = remove_zeros(a)
b = remove_zeros(b)
c = remove_zeros(c)

if a + b == c:
    print("YES")
else:
    print("NO")
