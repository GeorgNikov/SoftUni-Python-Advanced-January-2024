def check_indices_valid(indices, rows, cols):
    if 0 <= indices[0] < rows and 0 <= indices[1] < cols:
        return True


def knights_position():
    position = []

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "K":
                position.append([row, col])
    return position


def knights_move(knights_position):
    for row, col in knights_position:
        for knight_move in directions:
            new_row, new_col = row + knight_move[0], col + knight_move[1]

            if check_indices_valid((new_row, new_col), rows, cols):
                if  matrix[new_row][new_col] == 'K':
                    if (row, col) not in knights:
                        knights[(row, col)] = 0
                    knights[(row, col)] += 1


import operator

rows = int(input())
cols = rows

matrix = [input() for _ in range(rows)]
counter = 0

directions = {  # Knight directions
    (-2, -1),   # up-left
    (-2, 1),    # up-right
    (-1, -2),   # left-up
    (1, -2),    # left-down
    (-1, 2),    # right-up
    (1, 2),     # right-down
    (2, -1),   # down-left
    (2, 1),    # down-right
}


while True:
    knights = {}  # { coords(0, 0): count(0) }
    knights_move(knights_position())

    if all(x==0 for x in knights.values()):
        print(counter)
        break
    else:
        to_remove = max(knights.items(), key=operator.itemgetter(1))[0]
        del knights[to_remove]
        r, c = [int(el) for el in to_remove]
        matrix[r] = matrix[r][:c] + '0' + matrix[r][c + 1:]
        counter += 1
        continue
