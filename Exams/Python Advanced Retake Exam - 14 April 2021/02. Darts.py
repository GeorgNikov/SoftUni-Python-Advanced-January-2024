def check_indices_valid(indices):
    if 0 <= indices[0] < 7 and 0 <= indices[1] < 7:
        return True


def get_points(cord):
    row, col = eval(cord)
    r, c = int(row), int(col)

    if check_indices_valid((r, c)):
        if field[r][c].isdigit():
            return int(field[r][c])
        else:
            points = int(field[r][0]) + int(field[r][-1]) + int(field[0][c]) + int(field[-1][c])
            if field[r][c] == 'D':
                return points * 2
            elif field[r][c] == 'T':
                return points * 3
            elif field[r][c] == 'B':
                return 501
    return 0


player_one, player_two = input().split(', ')

players = {
    player_one: [501, 0],
    player_two: [501, 0],
}

turns = 1
field = []

for row in range(7):
    matrix = [x for x in input().split()]
    field.append(matrix)

while True:
    if turns % 2 != 0:
        current_player = player_one
    else:
        current_player = player_two

    points = get_points(input())

    players[current_player][0] -= points
    players[current_player][1] += 1

    if players[current_player][0] <= 0:
        print(f"{current_player} won the game with {players[current_player][1]} throws!")
        break

    turns += 1
