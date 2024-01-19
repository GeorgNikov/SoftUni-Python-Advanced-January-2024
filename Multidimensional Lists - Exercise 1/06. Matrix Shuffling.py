def check_valid_index(indices):
    return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_cols)


rows, cols = [int(el) for el in input().split()]
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

command = input()

while command != 'END':
    action, *data = command.split()
    if action != 'swap' and len(data) != 4:
        print('Invalid input!')
        continue
    elif action == 'swap':
        points = ([int(x) for x in data])
        if check_valid_index(points):
            matrix[points[0]][points[1]], matrix[points[2]][points[3]] = matrix[points[2]][points[3]], matrix[points[0]][points[1]]
            print(matrix)
    command = input()

# NOT WORKING
