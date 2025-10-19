def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

num_rows, num_cols = map(int, input().split())
matrix = []
for _ in range(num_rows):
    row = list(map(int, input().split()))
    matrix.append(row)

prime_count = 0
for row_index in range(num_rows):
    if row_index == 0 or row_index == num_rows - 1:
        for value in matrix[row_index]:
            if is_prime(value):
                prime_count += 1
    else:
        row = matrix[row_index]
        if num_cols > 0 and is_prime(row[0]):
            prime_count += 1
        if num_cols > 1 and is_prime(row[-1]):
            prime_count += 1

print(prime_count)


