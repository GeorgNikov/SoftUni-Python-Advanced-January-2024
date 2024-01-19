row = int(input())

matrix = []

for _ in range(row):
    matrix.append([int(el) for el in input().split(', ')])

# Or
# matrix = [[int(el) for el in input().split(', ')] for _ in range(row)]

sum_of_diagonals = [[],[]]

for row_index in range(row):
    current_element = matrix[row_index][row_index]
    sum_of_diagonals[0].append(matrix[row_index][row_index])

cnt = len(sum_of_diagonals[0]) - 1
for row_index in range(row):
    current_element = matrix[row_index][cnt]
    sum_of_diagonals[1].append(current_element)
    cnt -= 1

print(f"Primary diagonal: {(', '.join([str(el) for el in sum_of_diagonals[0]]))}. Sum: {sum(sum_of_diagonals[0])}")
print(f"Secondary diagonal: {(', '.join([str(el) for el in sum_of_diagonals[1]]))}. Sum: {sum(sum_of_diagonals[1])}")
