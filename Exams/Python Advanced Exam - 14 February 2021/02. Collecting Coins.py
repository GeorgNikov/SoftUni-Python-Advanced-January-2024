from math import floor


def player_position():
    for row in range(SIZE):
        for col in range(SIZE):
            if field[row][col] == "P":
                field[row][col] = "-"
                path.append([row, col])
                return row, col


def get_next_step(row, col, direction):
    r, c = row + DIRECTIONS[direction][0], col + DIRECTIONS[direction][1]
    if 0 <= r < SIZE and 0 <= c < SIZE:
        return row + DIRECTIONS[direction][0], col + DIRECTIONS[direction][1]
    else:
        return (row + DIRECTIONS[direction][0]) % SIZE, (col + DIRECTIONS[direction][1]) % SIZE


SIZE = int(input())

field = []
path = []
coins = 0

for row in range(SIZE):
    matrix = [x for x in input().split()]
    field.append(matrix)

DIRECTIONS = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

r, c = player_position()

while coins < 100:
    move = input()
    if move in DIRECTIONS:
        r, c = get_next_step(r, c, move)
        path.append([r, c])
        if field[r][c].isdigit():
            coins += int(field[r][c])
            field[r][c] = '-'
        elif field[r][c] == 'X':
            coins = floor(coins * 0.5)
            break

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print(f"Your path:", *path, sep='\n')
