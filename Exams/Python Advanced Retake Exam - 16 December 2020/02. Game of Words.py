def check_indices_valid(indices):
    if 0 <= indices[0] < size and 0 <= indices[1] < size:
        return True


def player_position():
    position = ()

    for row in range(size):
        for col in range(size):
            if field[row][col] == "P":
                position = [row, col]
                field[row][col] = '-'
                break
    return position


string = input()
size = int(input())

field = []

for row in range(size):
    matrix = [sub for sub in input()]
    field.append(matrix)

my_position = player_position()

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

steps = int(input())
for i in range(steps):
    going = input()
    for direction in directions:
        if direction == going:
            r, c = my_position[0] + directions[direction][0], my_position[1] + directions[direction][1]
            if check_indices_valid((r, c)):
                if field[r][c].isalpha():
                    string = string + field[r][c]
                    field[r][c] = "-"
                    my_position = [r, c]
                else:
                    my_position = [r, c]
            else:
                string = string[:-1]

field[my_position[0]][my_position[1]] = 'P'

print(string)
[print(*row, sep='') for row in field]
