def check_indices_valid(indices, size):
    if 0 <= indices[0] < size and 0 <= indices[1] < size:
        return True


def alice_position():
    position = ()

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "A":
                position = (row, col)
                matrix[row][col] = "*"
                break
    return position


size = int(input())

matrix = [list(input().split()) for _ in range(size)]
tea_bags = 0

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

r, c = alice_position()

while tea_bags < 10:
    move = input()
    row, col = directions[move][0], directions[move][1]
    next_row, next_col = r + row, c + col
    if not check_indices_valid((next_row, next_col), size):
        print("Alice didn't make it to the tea party.")
        break

    if matrix[next_row][next_col] == 'R':
        matrix[next_row][next_col] = '*'
        print("Alice didn't make it to the tea party.")
        break

    elif matrix[next_row][next_col].isdigit():
        tea_bags += int(matrix[next_row][next_col])

    matrix[next_row][next_col] = '*'
    r, c = next_row, next_col

if tea_bags >= 10:
    print("She did it! She went to the party.")

[print(*row) for row in matrix]