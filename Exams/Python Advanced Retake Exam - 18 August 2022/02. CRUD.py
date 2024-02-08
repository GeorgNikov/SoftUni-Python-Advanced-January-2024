def move(row, col, direction):
    r, c = row + DIRECTIONS[direction][0], col + DIRECTIONS[direction][1]
    if 0 <= r < SIZE and 0 <= c < SIZE:
        return r, c


SIZE = 6
DIRECTIONS = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

read = []
matrix = []
# Create matrix
for _ in range(SIZE):
    matrix.append([x for x in input().split()])

# First coordinates
r, c = eval(input())

while True:
    commands = input().split(', ')

    if commands[0] == 'Stop':
        break

    r, c = move(r, c, commands[1])
    if commands[0] == 'Delete':
        matrix[r][c] = '.'

    elif commands[0] == 'Read':
        if matrix[r][c] != '.':
            read.append(matrix[r][c])

    elif commands[0] == 'Create':
        if matrix[r][c] == '.':
            matrix[r][c] = commands[-1]

    elif commands[0] == 'Update':
        if matrix[r][c] != '.':
            matrix[r][c] = commands[-1]

print(*read, sep='\n')
[print(*row) for row in matrix]
