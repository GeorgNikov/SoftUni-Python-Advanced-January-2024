def check_indices_valid(indices, rows, cols):
    if 0 <= int(indices[0]) < rows and 0 <= int(indices[1]) < cols:
        return True


n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(el) for el in input().split()])

rows, cols = n, len(matrix[0])

while True:
    command, *data = [int(x) if x.isdigit() else x for x in input().split()]
    if command == 'END':
        break

    if check_indices_valid(data, rows, cols):
        if command == 'Add':
            matrix[data[0]][data[1]] += data[2]

        elif command == 'Subtract':
            matrix[data[0]][data[1]] -= data[2]

    else:
        print('Invalid coordinates')

[print(*row) for row in matrix]
