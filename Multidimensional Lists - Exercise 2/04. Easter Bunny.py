def check_indices_valid(indices, rows, cols):
    if 0 <= indices[0] < rows and 0 <= indices[1] < cols:
        return True


def bunny_position():
    position = ()

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "B":
                position = (row, col)
                break
    return position


def valid_path(bunny_position):
    paths = dict()
    moves = dict()
    r, c = bunny_position[0], bunny_position[1]
    for path in directions:
        new_row, new_col = r + path[0], c + path[1]
        while True:
            if not check_indices_valid((new_row, new_col), rows, cols) or matrix[new_row][new_col] == 'X':
                break

            if check_indices_valid((new_row, new_col), rows, cols):
                k = directions[(path[0], path[1])]
                if k not in paths:
                    paths[k] = []
                    moves[k] = 0
                paths[k].append([new_row, new_col])
                moves[k] += int(matrix[new_row][new_col])
            new_row, new_col = new_row + path[0], new_col + path[1]

    return paths, max(moves.items(), key=lambda x: x[1])


rows = int(input())
cols = rows

matrix = [list(input().split()) for _ in range(rows)]

directions = {
    (-1, 0): 'up',
    (1, 0): 'down',
    (0, -1): 'left',
    (0, 1): 'right',
}

path, moves = valid_path(bunny_position())
for key, value in path.items():
    if key == moves[0]:
        print(key)
        print(*value, sep='\n')
        print(moves[1])
