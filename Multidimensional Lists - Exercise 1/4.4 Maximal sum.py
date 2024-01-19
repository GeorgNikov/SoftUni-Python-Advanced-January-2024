rows, cols = [int(el) for el in input().split()]

matrix = []

max_sum = float('-inf')
max_matrix = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split()])

for row in range(rows -2):
    for col in range(cols -2):
        first_row = matrix[row][col:col+3]
        second_row = matrix[row+1][col:col+3]
        third_row = matrix[row+2][col:col+3]

        total_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if max_sum < total_sum:
            max_sum = total_sum
            max_matrix = [first_row, second_row, third_row]

print(f'Sum = {max_sum}')
[print(*row) for row in max_matrix]
