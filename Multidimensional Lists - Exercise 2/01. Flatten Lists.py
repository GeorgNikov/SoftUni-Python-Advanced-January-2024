matrix = []
flatten = []

for i in input().split('|'):
    sub_matrix = [int(el) for el in i.split()]
    matrix.insert(0, sub_matrix)

for i in range(len(matrix)):
    flatten.extend(matrix[i])

print(*flatten)
