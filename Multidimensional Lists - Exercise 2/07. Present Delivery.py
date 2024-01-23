def cookie_time(pos, nice_kids_count, presents):
    for direction in directions.values():
        r, c = pos[0], pos[1]
        r += direction[0]
        c += direction[1]

        if neighborhood[r][c].isalpha():
            if neighborhood[r][c] == 'V':
                nice_kids_count += 1

            presents -= 1
            neighborhood[r][c] = '-'

        if not presents:
            break

    return nice_kids_count, presents


santa_presents = int(input())
size = int(input())

presents = santa_presents
neighborhood = []
nice_kids = 0
nice_kids_count = 0
my_position = []

directions = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
}

for row in range(size):  # Create a neighborhood and count nice kids!
    neighborhood.append(input().split())

    if 'S' in neighborhood[row]:
        my_position = [row, neighborhood[row].index('S')]

    nice_kids += neighborhood[row].count("V")

neighborhood[my_position[0]][my_position[1]] = '-'

while True:
    command = input()
    if command == 'Christmas morning' or presents == 0:
        break

    r, c = my_position[0] + directions[command][0], my_position[1] + directions[command][1]
    my_position = [r, c]

    if neighborhood[r][c] == 'V':
        nice_kids_count += 1
        presents -= 1
        neighborhood[r][c] = '-'
    elif neighborhood[r][c] == 'X':
        neighborhood[r][c] = '-'
        continue
    elif neighborhood[r][c] == 'C':
        nice_kids_count, presents = cookie_time([r, c], nice_kids_count, presents)
        neighborhood[r][c] = '-'

    if not presents or nice_kids_count == nice_kids:
        break

neighborhood[my_position[0]][my_position[1]] = 'S'

if not presents and nice_kids_count < nice_kids:
    print('Santa ran out of presents!')

[print(*row) for row in neighborhood]

if nice_kids_count == nice_kids:
    print(f'Good job, Santa! {nice_kids_count} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids - nice_kids_count} nice kid/s.')
