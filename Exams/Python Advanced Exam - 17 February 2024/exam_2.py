def move(row, col, direction):
    return row + DIRECTIONS[direction][0], col + DIRECTIONS[direction][1]


size = int(input())

airspace = []
jet_position = [0, 0]
jet_armor = 300
enemy_planes = 4

for row in range(size):
    data = list(input())

    if "J" in data:
        jet_position = [row, data.index("J")]

    airspace.append(data)

DIRECTIONS = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

direction = input()
current_row, current_col = jet_position
airspace[current_row][current_col] = '-'

while True:
    current_row, current_col = move(current_row, current_col, direction)
    symbol = airspace[current_row][current_col]

    if symbol == 'R':
        jet_armor = 300
        airspace[current_row][current_col] = '-'

    elif symbol == 'E':
        airspace[current_row][current_col] = '-'
        enemy_planes -= 1
        if enemy_planes == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        else:
            jet_armor -= 100
            if jet_armor == 0:
                print(f"Mission failed, your jetfighter was shot down!"
                      f" Last coordinates [{current_row}, {current_col}]!")
                break
        airspace[current_row][current_col] = '-'

    direction = input()

airspace[current_row][current_col] = "J"

[print(*row, sep='') for row in airspace]