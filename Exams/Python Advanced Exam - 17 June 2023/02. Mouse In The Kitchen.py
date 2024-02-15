def move(row, col, direction, size):
    r, c = row + DIRECTIONS[direction][0], col + DIRECTIONS[direction][1]
    if 0 <= r < size[0] and 0 <= c < size[1]:
        return r, c
    return 'Outside', 'Outside'

rows, cols = [int(x) for x in input().split(',')]

cupboards = []
mouse_position = [0, 0]
cheese = 0

for row in range(rows):
    data = list(input())

    if "M" in data:
        mouse_position = [row, data.index("M")]

    if "C" in data:
        cheese += data.count('C')

    cupboards.append(data)

DIRECTIONS = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

direction = input()
current_row, current_col = mouse_position
cupboards[current_row][current_col] = "*"

while direction != 'danger':

    next_row, netx_col = move(current_row, current_col, direction, (rows, cols))

    if next_row == 'Outside':
        print("No more cheese for tonight!")
        break
    else:
        symbol = cupboards[next_row][netx_col]

        if symbol == 'C':
            cupboards[next_row][netx_col] = '*'
            cheese -= 1
            current_row, current_col = next_row, netx_col
            if cheese == 0:
                print("Happy mouse! All the cheese is eaten, good night!")
                current_row, current_col = next_row, netx_col
                break

        elif symbol == "T":
            print("Mouse is trapped!")
            current_row, current_col = next_row, netx_col
            break

        elif symbol == "@":
            direction = input()
            continue

    current_row, current_col = next_row, netx_col
    direction = input()

else:
    print("Mouse will come back later!")

cupboards[current_row][current_col] = "M"

[print(*row, sep='') for row in cupboards]