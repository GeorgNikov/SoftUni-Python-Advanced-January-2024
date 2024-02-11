def move(row, col, direction, size):
    r, c = row + DIRECTIONS[direction][0], col + DIRECTIONS[direction][1]
    if 0 <= r < size and 0 <= c < size:
        return r, c


size = int(input())
racing_number = input()

route = []
tunnels = []
my_position = [0, 0]
total_race = 0

for row in range(size):
    data = list(input().split())

    if "T" in data:
        tunnels.append([row, data.index("T")])

    route.append(data)

DIRECTIONS = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

command = input()
current_row, current_col = my_position

while command != 'End':
    current_row, current_col = move(current_row, current_col, command, size)

    if route[current_row][current_col] == 'T':
        tunnels.pop(tunnels.index([current_row, current_col]))
        route[current_row][current_col] = '.'
        current_row, current_col = tunnels[0]
        route[current_row][current_col] = '.'
        total_race += 30

    elif route[current_row][current_col] == 'F':
        print(f"Racing car {racing_number} finished the stage!")
        total_race += 10
        break

    else:
        total_race += 10

    command = input()
else:
    print(f"Racing car {racing_number} DNF.")

route[current_row][current_col] = 'C'

print(f"Distance covered {total_race} km.")
[print(*row, sep='') for row in route]
