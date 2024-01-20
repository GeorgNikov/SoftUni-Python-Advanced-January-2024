n = int(input())
commands = input().split()

matrix = []
miner_pos = []  # [miner_row, miner_col]
collected_coal, total_coal = 0, 0

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

for row in range(n):
    matrix.append(input().split())

    if 's' in matrix[row]:  # Find miner position
        miner_pos = [row, matrix[row].index('s')]   # Miner position
        matrix[miner_pos[0]][miner_pos[1]] = '*'    # Replace miner position with '*'

    total_coal += matrix[row].count('c')

for command in commands:    # Find next step
    r, c = miner_pos[0] + directions[command][0], miner_pos[1] + directions[command][1]

    if not (0 <= r < n and 0 <= c < n): # Check valid position
        continue

    miner_pos = [r, c]
    if matrix[r][c] == 'c':     # Collect coal
        collected_coal += 1

        if collected_coal == total_coal:
            print(f'You collected all coal! ({r}, {c})')
            break

    elif matrix[r][c] == 'e':
        print(f'Game over! ({r}, {c})')
        break

    matrix[r][c] = '*'

else:
    print(f'{total_coal - collected_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})')
    