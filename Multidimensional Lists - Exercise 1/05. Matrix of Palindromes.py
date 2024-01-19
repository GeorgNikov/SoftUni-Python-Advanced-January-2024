rows, cols = [int(el) for el in input().split()]

for row in range(rows):
    sub_matrix = []
    start = 97
    for col in range(cols):
        sub_matrix.append(chr(start + row) + chr(start + row + col) + chr(start + row))
    start += 1
    print(*sub_matrix)
