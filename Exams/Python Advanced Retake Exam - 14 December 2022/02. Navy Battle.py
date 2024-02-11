def move(row, col, direction):
    return row + DIRECTIONS[direction][0], col + DIRECTIONS[direction][1]


size = int(input())
battlefield = []
battle_cruisers = 0
mines = 0

submarine = []

for row in range(size):
    data = list(input())

    if "S" in data:
        submarine.append([row, data.index("S")])

    battlefield.append(data)

DIRECTIONS = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

current_row, current_col = submarine[0]
battlefield[current_row][current_col] = '-'
command = input()

while mines < 3 and battle_cruisers < 3:
    current_row, current_col = move(current_row, current_col, command)
    symbol = battlefield[current_row][current_col]

    if symbol == '*':
        mines += 1
        if mines < 3:
            battlefield[current_row][current_col] = '-'
        else:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{current_row}, {current_col}]!")
            break

    elif symbol == 'C':
        battlefield[current_row][current_col] = '-'
        battle_cruisers += 1

        if battle_cruisers == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

    command = input()

battlefield[current_row][current_col] = 'S'

[print(*row, sep='') for row in battlefield]
