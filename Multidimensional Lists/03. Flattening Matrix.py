row = int(input())

matrix = []

for i in range(row):
    data = [int(el) for el in input().split(', ')]
    matrix.append(data)

flattened = [num for sublist in matrix for num in sublist]

print(flattened)