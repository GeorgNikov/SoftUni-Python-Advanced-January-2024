def move(row, col, direction, size):
    r, c = row + DIRECTIONS[direction][0], col + DIRECTIONS[direction][1]
    if 0 <= r < size and 0 <= c < size:
        return r, c
    return 'Outside', 'Outside'


from collections import deque

size = int(input())
directions = deque([x for x in input().split(', ')])
field = []
squirrel_position = [0, 0]
hazelnuts = 0
game_stop = False

for row in range(size):
    data = list(input())

    if "s" in data:
        squirrel_position = [row, data.index("s")]

    field.append(data)

DIRECTIONS = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

current_row, current_col = squirrel_position
field[current_row][current_col] = "*"

while directions:
    direction = directions.popleft()
    next_row, netx_col = move(current_row, current_col, direction, size)

    if next_row == 'Outside':
        print("The squirrel is out of the field.")
        game_stop = True
        break
    else:
        symbol = field[next_row][netx_col]

        if symbol == 'h':
            hazelnuts += 1
            current_row, current_col = next_row, netx_col
            field[next_row][netx_col] = "*"
            if hazelnuts == 3:
                print("Good job! You have collected all hazelnuts!")

        elif symbol == 't':
            print("Unfortunately, the squirrel stepped on a trap...")
            game_stop = True
            break

        else:
            current_row, current_col = next_row, netx_col

if hazelnuts < 3 and not game_stop:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")
