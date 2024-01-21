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


rows = int(input())
cols = rows

matrix = [list(input().split()) for _ in range(rows)]

directions = {
    (-1, 0): 'up',
    (1, 0): 'down',
    (0, -1): 'left',
    (0, 1): 'right',
}


print(bunny_position())