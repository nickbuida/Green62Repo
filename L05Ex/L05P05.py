n = int(input())
arr = list(map(int, input().split()))
count = 0

def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

for x in arr:
    if is_prime(x):
        count += 1

print(count)
