row, col = list(map(int, input().split(', ')))

matrix = []
total_amount = 0

for _ in range(row):
    data = [int(el) for el in input().split(', ')]
    total_amount += sum(data)
    matrix.append(data)

print(total_amount)
print(matrix)
 