def move(row, col, direction):
    r, c = row + DIRECTIONS[direction][0], col + DIRECTIONS[direction][1]
    if 0 <= r < rows and 0 <= c < cols:
        return row + DIRECTIONS[direction][0], col + DIRECTIONS[direction][1]
    else:
        return (row + DIRECTIONS[direction][0]) % rows, (col + DIRECTIONS[direction][1]) % cols


rows, cols = map(int, input().split(', '))

workshop = []
my_position = []
all_items = 0
christmas = False

DIRECTIONS = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

items = {
    "Christmas decorations": 0,
    "Gifts": 0,
    "Cookies": 0,
}

for row in range(int(rows)):        # mapping workshop
    workshop.append([x for x in input().split()])

    if "Y" in workshop[row]:        # Find my position
        my_position = [row, workshop[row].index("Y")]
        workshop[my_position[0]][my_position[1]] = 'x'
    for ele in workshop[row]:
        all_items += all(el in ["C", "D", "G"] for el in ele)

current_row, current_col = my_position

while sum(items.values()) != all_items:
    command = input().split('-')
    direction = command[0]
    if direction == 'End':
        break

    steps = int(command[1])

    for _ in range(int(steps)):
        current_row, current_col = move(current_row, current_col, direction)
        if workshop[current_row][current_col] == 'D':
            items['Christmas decorations'] += 1
        elif workshop[current_row][current_col] == 'G':
            items['Gifts'] += 1
        elif workshop[current_row][current_col] == 'C':
            items['Cookies'] += 1
        workshop[current_row][current_col] = 'x'
        if sum(items.values()) == all_items:
            christmas = True
            break

workshop[current_row][current_col] = 'Y'

if christmas:
    print('Merry Christmas!')

print("You've collected:")
for key, value in items.items():
    print(f"- {value} {key}")

[print(*row) for row in workshop]
