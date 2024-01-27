def check_indices_valid(indices):
    if 0 <= indices[0] < SIZE and 0 <= indices[1] < SIZE:
        return True


def snake_burrow_position():
    position = ()
    burrow = []
    for row in range(SIZE):
        for col in range(SIZE):
            if matrix[row][col] == "S":
                position = (row, col)
                matrix[row][col] = "."
                break
            elif matrix[row][col] == "B":
                burrow.append((row, col))
                break
    return position, burrow


SIZE = int(input())
matrix = [list(input()) for _ in range(SIZE)]

my_position, burrow = snake_burrow_position()
r, c = my_position[0], my_position[1]
food = 0

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

while food < 10:
    move = input()
    if move in directions:
        next_row, next_col = directions[move]
        r, c = r + next_row, c + next_col

        if not check_indices_valid((r, c)):
            break

        if (r, c) in burrow:
            r_burrow, c_burrow = burrow.pop(burrow.index((r, c)))
            r, c = burrow.pop()
            matrix[r_burrow][c_burrow] = '.'
            matrix[r][c] = '.'

        elif matrix[r][c] == '*':
            food += 1
            matrix[r][c] = '.'

        else:
            matrix[r][c] = '.'

else:
    matrix[r][c] = 'S'

if food == 10:
    print("You won! You fed the snake.")
else:
    print("Game over!")

print(f"Food eaten: {food}")
[print(*row, sep='') for row in matrix]
