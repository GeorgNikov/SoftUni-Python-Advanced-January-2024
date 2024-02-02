def get_magic_triangle(n):
    triangle = [[1], [1, 1]]

    while len(triangle) < n:
        current_row = triangle[-1]
        new_row = [current_row[0]]

        for i in range(len(current_row) - 1):
            new_row.append(current_row[i] + current_row[i + 1])

        new_row.append(current_row[-1])
        triangle.append(new_row)

    return triangle

print(get_magic_triangle(20))