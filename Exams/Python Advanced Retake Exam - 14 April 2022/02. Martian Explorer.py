from collections import deque

SIZE = 6
DIRECTIONS = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}


def move(row, col, direction):
    r, c = row + DIRECTIONS[direction][0], col + DIRECTIONS[direction][1]
    if 0 <= r < SIZE and 0 <= c < SIZE:
        return row + DIRECTIONS[direction][0], col + DIRECTIONS[direction][1]
    else:
        return (row + DIRECTIONS[direction][0]) % SIZE, (col + DIRECTIONS[direction][1]) % SIZE


field = []
my_position = []

for row in range(SIZE):         # mapping field
    field.append([x for x in input().split()])

    if "E" in field[row]:        # Find my position
        my_position = [row, field[row].index("E")]
        field[my_position[0]][my_position[1]] = '-'

deposits = {
    "Water deposit": 0,
    "Metal deposit": 0,
    "Concrete deposit": 0,
}

# Current coordinates
current_row, current_col = my_position
commands = deque(input().split(', '))

while commands:
    current_direction = commands.popleft()
    current_row, current_col = move(current_row, current_col, current_direction)

    if field[current_row][current_col] == 'W':
        deposits["Water deposit"] += 1
        print(f"Water deposit found at {(current_row, current_col)}")

    elif field[current_row][current_col] == 'M':
        deposits["Metal deposit"] += 1
        print(f"Metal deposit found at {(current_row, current_col)}")

    elif field[current_row][current_col] == 'C':
        deposits["Concrete deposit"] += 1
        print(f"Concrete deposit found at {(current_row, current_col)}")

    elif field[current_row][current_col] == "R":
        print(f"Rover got broken at {(current_row, current_col)}")
        break

result = all(value > 0 for value in deposits.values())

if result:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
