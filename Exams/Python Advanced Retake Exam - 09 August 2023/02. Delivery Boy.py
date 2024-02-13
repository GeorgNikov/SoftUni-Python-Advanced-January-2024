def check_boundaries(n_row, n_col, n_r, m_c):
    return 0 <= n_row < n_r and 0 <= n_col < m_c


n, m = [int(x) for x in input().split()]

matrix = []
my_position = [0, 0]

for row in range(n):
    data = list(input())
    if "B" in data:
        my_position = [row, data.index("B")]
    matrix.append(data)

DIRECTIONS = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

current_row, current_col = my_position

while True:
    direction = input()
    next_row, next_col = current_row + DIRECTIONS[direction][0], current_col + DIRECTIONS[direction][1]

    if not check_boundaries(next_row, next_col, n, m):
        matrix[my_position[0]][my_position[1]] = " "
        print("The delivery is late. Order is canceled.")
        break

    symbol = matrix[next_row][next_col]

    if symbol == '*':
        continue

    current_row, current_col = next_row, next_col

    if symbol == 'P':
        print("Pizza is collected. 10 minutes for delivery.")
        matrix[current_row][current_col] = 'R'

    elif symbol == 'A':
        matrix[current_row][current_col] = 'P'
        print("Pizza is delivered on time! Next order...")
        break

    elif symbol == '-':
        matrix[current_row][current_col] = '.'

[print(*row, sep='') for row in matrix]
