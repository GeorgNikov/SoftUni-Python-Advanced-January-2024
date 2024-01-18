row = int(input())
col = row

matrix = []
col_total = 0

for _ in range(row):
    data = [int(el) for el in input().split()]
    matrix.append(data)

for col_index in range(col, -1, -1):
    for row_index in range(row, -1, -1):
        col_total += matrix[row_index - col_index][col_index]
        break

print(col_total)
