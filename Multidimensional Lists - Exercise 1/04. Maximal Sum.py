# Function to find sum of all elements of matrix
def sum_of_matrix(row, col, mat):
    total_sum = 0

    for i in range(row):
        for j in range(col):
            total_sum += mat[i][j]

    return total_sum


row, col = [int(el) for el in input().split()]

matrix = []

sub_matrix_square = 3
max_sum = float('-inf')
max_matrix = []

for _ in range(row):
    matrix.append([int(el) for el in input().split()])

algo_row = row - (sub_matrix_square - 1)
algo_col = col - (sub_matrix_square - 1)

for row_index in range(algo_row):
    for col_index in range(algo_col):
        sub_matrix = [
            [matrix[row_index][col_index], matrix[row_index][col_index + 1], matrix[row_index][col_index + 2]],
            [matrix[row_index + 1][col_index], matrix[row_index + 1][col_index + 1],
             matrix[row_index + 1][col_index + 2]],
            [matrix[row_index + 2][col_index], matrix[row_index + 2][col_index + 1],
             matrix[row_index + 2][col_index + 2]]
        ]

        total_sum = sum_of_matrix(len(sub_matrix), len(sub_matrix[0]), sub_matrix)

        if max_sum < total_sum:
            max_sum = total_sum
            max_matrix = sub_matrix

print(f'Sum = {max_sum}')
for i in range(len(max_matrix)):
    print(*max_matrix[i])
