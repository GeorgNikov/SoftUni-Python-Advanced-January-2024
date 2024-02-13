def move(row, col, direction, size):
    return (row + DIRECTIONS[direction][0] + size) % size, (col + DIRECTIONS[direction][1] + size) % size


size = int(input())

fishing_area = []
my_position = []
catches = 0

# Create fishing area
for row in range(size):
    data = list(input())        # [x fro x in input()]

    if "S" in data:
        my_position = [row, data.index("S")]

    fishing_area.append(data)

DIRECTIONS = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

r, c = my_position[0], my_position[1]
fishing_area[r][c] = '-'

direction = input()

while direction != 'collect the nets':

    current_row, current_col = move(r, c, direction, size)
    symbol = fishing_area[current_row][current_col]
    fishing_area[current_row][current_col] = '-'
    r, c = current_row, current_col

    if symbol.isdigit():
        catches += int(symbol)

    elif symbol == 'W':
        catches = 0
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{current_row},{current_col}]")
        exit()

    direction = input()

fishing_area[r][c] = 'S'

if catches >= 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - catches} tons of fish more.")

if catches > 0:
    print(f"Amount of fish caught: {catches} tons.")

[print(*row, sep='') for row in fishing_area]
