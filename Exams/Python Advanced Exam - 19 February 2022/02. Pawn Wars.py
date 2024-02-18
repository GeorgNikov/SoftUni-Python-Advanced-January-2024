from collections import deque


# Move current pawn one position ahead
def move(plr, coordinates, directions):
    r, c = coordinates[plr]
    new_r = r + directions[plr][1][0]
    return new_r, c


# Pawn fight
def fight(plr, coordinates):
    row, col = coordinates
    where = str(abs(row - SIZE)) if plr == 'Black' else str(SIZE - row)
    return f"Game over! {plr} win, capture on {board_symbols[col] + where}."


SIZE = 8
board = []
board_symbols = ['a', 'b', "c", "d", "e", "f", "g", "h"]
players_turn = deque(["White", 'Black'])

player_position = {
    'White': [],
    'Black': [],
}

directions = {
    'White': ([-1, -1], [-1, 1]),
    'Black': ([1, 1], [1, -1]),
}

# Creating a chessboard
for row in range(SIZE):
    board.append(input().split())

    if 'b' in board[row]:
        player_position['Black'] = ([row, board[row].index("b")])
    if 'w' in board[row]:
        player_position['White'] = ([row, board[row].index("w")])

while True:
    # When pawns is not close each other to fight -> 1 column distance
    if abs(player_position['White'][1] - player_position['Black'][1]) > 1:
        # What pawn is closer to the end of the board
        if player_position['White'][0] < SIZE - player_position['Black'][0]:
            print(f"Game over! White pawn is promoted to a queen at {board_symbols[player_position['White'][1]]}{8}.")
            break
        else:
            print(f"Game over! Black pawn is promoted to a queen at {board_symbols[player_position['Black'][1]]}{1}.")
            break
    else:
        # When pawns is close each other to fight -> 0 row distance
        if abs(player_position['White'][0] - player_position['Black'][0]) == 1:
            print(fight(players_turn[0], player_position[players_turn[1]]))
            break
        else:   # Just move current pawn and rotate players
            current_row, current_col = move(players_turn[0], player_position, directions)
            player_position[players_turn[0]] = [current_row, current_col]
            players_turn.rotate()
