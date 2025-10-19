

def is_even(n):
    return n % 2 == 0


num_rows, num_cols = map(int, input().split())
matrix = []
for _ in range(num_rows):
    row = list(map(int, input().split()))
    matrix.append(row)

max_evens = -1
max_row = 0
row_idx = 0
for row in matrix:
    evens = 0
    for value in row:
        if is_even(value):
            evens += 1
    if evens > max_evens:
        max_evens = evens
        max_row = row_idx
    row_idx += 1

print(max_row)



