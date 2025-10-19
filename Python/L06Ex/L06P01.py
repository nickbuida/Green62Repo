# num_rows, num_cols = map(int, input().split())
# matrix = []
# for _ in range(num_rows):
# 	row = list(map(int, input().split()))
# 	matrix.append(row)

# row_index = 0
# for row in matrix:
# 	print(f"{row_index}: {sum(row)}")
# 	row_index += 1

num_rows, num_cols = map(int, input().split())
matrix = []
for _ in range(num_rows):
	row = list(map(int, input().split()))
	matrix.append(row)

row_index = 0
for row in matrix:
	row_sum = 0
	for value in row:
		row_sum += value
	print(f"{row_index}: {row_sum}")
	row_index += 1