
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(n ** 0.5) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True



size = int(input())
matrix = []
for _ in range(size):
    row = list(map(int, input().split()))
    matrix.append(row)

prime_count = 0
for i in range(size):
    value = matrix[i][i]
    if is_prime(value):
        prime_count += 1

print(prime_count)
