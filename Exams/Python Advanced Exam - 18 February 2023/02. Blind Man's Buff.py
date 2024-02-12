def move(row, col, direction, n, m):
    r, c = row + DIRECTIONS[direction][0], col + DIRECTIONS[direction][1]
    if 0 <= r < n and 0 <= c < m:
        return r, c
    else:
        return row, col


n, m = input().split()

playground = []
my_position = [0, 0]

opponents = 0
moves = 0

for row in range(int(n)):
    data = list(input().split())
    if "B" in data:
        my_position = [row, data.index("B")]
    playground.append(data)

DIRECTIONS = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

command = input()
current_row, current_col = my_position
playground[current_row][current_col] = '-'

while command != 'Finish' and opponents < 3:
    next_row, next_col = move(current_row, current_col, command, int(n), int(m))

    if current_row == next_row and current_col == next_col:
        command = input()
        continue

    if playground[next_row][next_col] == 'P':
        playground[next_row][next_col] = '-'
        current_row, current_col = next_row, next_col
        opponents += 1
        moves += 1

    elif playground[next_row][next_col] == '-':
        current_row, current_col = next_row, next_col
        moves += 1

    # current_row, current_col = current_row, current_col
    command = input()

print("Game over!")
print(f"Touched opponents: {opponents} Moves made: {moves}")
