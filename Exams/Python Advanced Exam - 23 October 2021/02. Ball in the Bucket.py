import sys


def check_indices_valid(indices):
    if 0 <= indices[0] < SIZE and 0 <= indices[1] < SIZE:
        return True


def get_bucket_point(column):
    pts = 0
    for r in range(SIZE):
        if board[r][column].isdigit():
            pts += int(board[r][column])
    return pts


SIZE = 6
throw = 3
board = []

points = 0

prizes = {
    "Football": [100, 199],
    "Teddy Bear": [200, 299],
    "Lego Construction Set": [300, sys.maxsize]
}

for row in range(SIZE):
    matrix = [x for x in input().split()]
    board.append(matrix)

# Creating board
for _ in range(throw):
    row, col = eval(input())
    if check_indices_valid((row, col)):
        if board[row][col] == 'B':
            points += get_bucket_point(col)  # Calculate points
            board[row][col] = '*'

# Check points for prize
if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
else:
    for prize in prizes:
        if prizes[prize][0] <= points <= prizes[prize][1]:
            print(f"Good job! You scored {points} points, and you've won {prize}.")
            break
