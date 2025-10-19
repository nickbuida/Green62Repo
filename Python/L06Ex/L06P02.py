num_rows, num_cols = map(int, input().split())
matrix = []

for _ in range(num_rows):
	row = list(map(int, input().split()))
	matrix.append(row)

all_negative_columns = []

for col in range(num_cols):
	all_negative = True
	for row in range(num_rows):
		if matrix[row][col] >= 0:
			all_negative = False
			break
	if all_negative:
		all_negative_columns.append(col)

print(*all_negative_columns)