def check_indices_valid(indices):
    if 0 <= indices[0] < SIZE and 0 <= indices[1] < SIZE:
        return True


def shoot(direction):
    r, c = my_position[0] + directions[direction][0], my_position[1] + directions[direction][1]

    while check_indices_valid((r, c)):
        if field[r][c] == 'x':
            field[r][c] = '.'
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


def move(direction, steps):
    r = my_position[0] + directions[direction][0] * steps
    c = my_position[1] + directions[direction][1] * steps

    if not check_indices_valid((r, c)):
        return my_position
    if field[r][c] == 'x':
        return my_position

    return [r, c]


SIZE = 5

field = []
targets = 0
hits = 0

targets_position = []
my_position = []

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

for row in range(SIZE):
    field.append(input().split())

    if 'A' in field[row]:
        my_position = [row, field[row].index('A')]

    targets += field[row].count("x")

for _ in range(int(input())):
    commands = input().split()
    r, c = my_position[0], my_position[1]
    direction = commands[1]

    if commands[0] == 'move':
        steps = int(commands[2])
        my_position = move(direction, steps)

    elif commands[0] == 'shoot':
        target_hit = shoot(direction)

        if target_hit:
            hits += 1
            targets_position.append(target_hit)

        if hits == targets:
            print(f"Training completed! All {targets} targets hit.")
            break

if hits < targets:
    print(f"Training not completed! {targets - hits} targets left.")

print(*targets_position, sep='\n')
