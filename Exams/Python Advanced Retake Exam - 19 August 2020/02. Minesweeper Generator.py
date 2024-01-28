def check_indices_valid(indices):
    if 0 <= indices[0] < size and 0 <= indices[1] < size:
        return True


size = int(input())
bombs = int(input())

field = [[0 for i in range(size)] for j in range(size)]

directions = {
    (0, -1),    # up
    (1, -1),    # up right
    (1, 0),     # right
    (1, 1),     # down right
    (0, 1),     # down
    (-1, 1),    # down left
    (-1, 0),    # left
    (-1, -1),   # left up
}

for _ in range(bombs):      # Mining field
    [r, c] = map(lambda x: int(x), input()[1:][:-1].split(', '))
    field[r][c] = '*'

for row in range(size):
    for col in range(size):
        if field[row][col] != '*':
            for direction in directions:
                r, c = row + direction[0], col + direction[1]
                if check_indices_valid((r, c)):
                    if field[r][c] == '*':
                        field[row][col] += 1

[print(*row) for row in field]
