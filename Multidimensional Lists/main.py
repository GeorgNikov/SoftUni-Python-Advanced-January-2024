# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# print(matrix[2][-1])


# matrix = []
#
# for row in range(0, 3):
#     matrix.append([])
#     for col in range(1, 4):
#         matrix[row].append(col)
#
# print(matrix)


# matrix = [[0 for j in range(2)] for i in range(3)] # Creating matrix [[0, 0], [0, 0], [0, 0]]
# matrix = [[j for j in range(1, 4)] for i in range(3)]   # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for sublist in matrix for num in sublist]

print(fa)