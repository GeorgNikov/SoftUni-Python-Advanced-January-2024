row, col = [int(el) for el in input().split()]

matrix = []
sub_matrix = {}
counter = 0

for _ in range(row):
    matrix.append([el for el in input().split()])

for row_index in range(row - 1):
    for col_index in range(col - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        element_under = matrix[row_index + 1][col_index]
        element_diagonal = matrix[row_index + 1][col_index + 1]

        sub_matrix = {current_element, next_element, element_under, element_diagonal}
        if len(sub_matrix) == 1:
            counter += 1

print(counter)
