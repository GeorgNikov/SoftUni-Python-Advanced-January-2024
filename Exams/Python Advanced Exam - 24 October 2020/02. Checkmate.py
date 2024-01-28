def check_indices_valid(indices):
    if 0 <= indices[0] < size and 0 <= indices[1] < size:
        return True


def find_king():
    for row in range(len(chess_board)):
        for col in range(size):
            if chess_board[row][col] == 'K':
                return row, col


size = 8
chess_board = [[el for el in input().split()] for r in range(size)]
king = find_king()
captured = []

directions = [
    (0, 1),     # right
    (1, 0),     # down
    (1, -1),    # down left
    (1, 1),     # down right
    (0, -1),    # left
    (-1, -1),   # left up
    (-1, 0),    # up
    (-1, 1),    # up right
]

for direction in directions:
    row, col = king[0] + direction[0], king[1] + direction[1]

    while True:
        if not check_indices_valid((row, col)):
            break

        if chess_board[row][col] == 'Q':
            captured.append([row, col])
            break

        row, col = row + direction[0], col + direction[1]

if not captured:
    print('The king is safe!')
else:
    print(*captured, sep='\n')
