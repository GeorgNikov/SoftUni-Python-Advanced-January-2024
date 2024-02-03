class FullColumnError(Exception):
    pass


class InvalidColumnChoice(Exception):
    pass


ROWS = 6
COLS = 7

DIRECTIONS = {
    'up': [-1, 0],
    'left': [0, -1],
    'main_diagonal': [-1, -1],
    'other_diagonal': [-1, 1],
}


def print_board(board):
    for row in board:
        print(row)


def travel_direction(coordinates, current_row, current_col, element, board):
    count = 0
    row_direction, col_direction = coordinates
    for i in range(1, 4):

        next_row_element = current_row + row_direction * i
        next_col_element = current_col + col_direction * i

        try:
            if board[next_row_element][next_col_element] == element:
                count += 1
            else:
                return count
        except IndexError:
            return count
    return count

def travel_opposite_direction(coordinates, current_row, current_col, element, board):
    count = 0
    for i in range(1, 4):
        row_direction, col_direction = coordinates
        next_row_element = current_row - row_direction * -i
        next_col_element = current_col - col_direction * -i

        try:
            if board[next_row_element][next_col_element] == element:
                count += 1
            else:
                return count
        except IndexError:
            return count
    return count

def is_winner(current_row_index, current_col_index, board):
    for direction, cords in DIRECTIONS.items():
        searched_element = board[current_row_index][current_col_index]
        travel_direction_count = travel_direction(cords, current_row_index, current_col_index, searched_element, board)
        travel_opposite_direction_count = travel_opposite_direction(cords, current_row_index, current_col_index, searched_element, board)

        if travel_direction_count + travel_opposite_direction_count + 1 >= 4:
            return True

    else:
        return False
def validate_column_choice(col):
    if 1 <= col <= COLS:
        return True
    raise InvalidColumnChoice


def get_first_available_row(col_index, board):
    for row_index in range(ROWS-1, -1, -1):
        if board[row_index][col_index] == 0:
            return row_index
    else:
        raise FullColumnError


def is_board_full(board):
    available_spots =  [el for el in board[0] if el == 0]
    if not available_spots:
        return True
    return False

board = []

for _ in range(ROWS):
    board.append([0 for _ in range(COLS)])

turns = 1

while True:
    player = 2 if turns % 2 == 0 else 1

    try:
        column = int(input(f"Player {player}, please choose a column: "))
        validate_column_choice(column)
        column_index = int(column) - 1
        row = get_first_available_row(column_index, board)
        board[row][column_index] = player
        if is_winner(row, column_index, board):
            break
        if is_board_full(board):
            print("Board is full, nobody wins")
            exit()
    except FullColumnError as ex:
        print(f"This column is full, please select another one")
        continue
    except (InvalidColumnChoice, ValueError):
        print(f"This column is invalid, please select a number between 1 and {COLS}")
        continue

    print_board(board)
    turns += 1

print(f"Winner is player {player}")
print_board(board)
