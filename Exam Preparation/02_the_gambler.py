def move(row, col, direction, size):
    r, c = row + DIRECTIONS[direction][0], col + DIRECTIONS[direction][1]
    if 0 <= r < size and 0 <= c < size:
        return r, c


size = int(input())
game_board = []

amount = 100
my_position = [0, 0]
outboard = False
jackpot = False

for row in range(size):
    data = list(input())
    if "G" in data:
        my_position = [row, data.index("G")]
    game_board.append(data)

DIRECTIONS = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

command = input()
current_row, current_col = my_position
game_board[current_row][current_col] = '-'

while command != 'end' and amount > 0:
    current_row, current_col = move(current_row, current_col, command, size)
    if not current_row and not current_col:
        outboard = True
        break

    symbol = game_board[current_row][current_col]

    if symbol == 'W':
        amount += 100

    elif symbol == 'P':
        if amount >= 200:
            amount -= 200
        else:
            amount = 0

    elif symbol == 'J':
        amount += 100000
        print("You win the Jackpot!")
        jackpot = True
        break

    game_board[current_row][current_col] = '-'
    command = input()
game_board[current_row][current_col] = 'G'

if outboard or amount == 0:
    print("Game over! You lost everything!")
else:
    print(f"End of the game. Total amount: {amount}$")
    [print(*row, sep='') for row in game_board]
