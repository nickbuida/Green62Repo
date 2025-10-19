n = int(input())  # size of the square matrix
matrix = []

# input matrix
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

count = 0  # number of Queen values

for i in range(n):
    for j in range(n):
        val = matrix[i][j]

        # find biggest in row
        biggest_row = matrix[i][0]
        for k in range(n):
            if matrix[i][k] > biggest_row:
                biggest_row = matrix[i][k]

        # find biggest in column
        biggest_col = matrix[0][j]
        for k in range(n):
            if matrix[k][j] > biggest_col:
                biggest_col = matrix[k][j]

        # find biggest in main diagonal (\)
        biggest_d1 = val
        for x in range(n):
            for y in range(n):
                if x - y == i - j:
                    if matrix[x][y] > biggest_d1:
                        biggest_d1 = matrix[x][y]

        # find biggest in secondary diagonal (/)
        biggest_d2 = val
        for x in range(n):
            for y in range(n):
                if x + y == i + j:
                    if matrix[x][y] > biggest_d2:
                        biggest_d2 = matrix[x][y]

        # check if val is biggest in all 4
        if val == biggest_row and val == biggest_col and val == biggest_d1 and val == biggest_d2:
            count += 1

print(count)
