def get_magic_triangle(row):
    triangle = [[1], [1, 1]]

    def recursion(triangle, recursion_count=0):
        for r in range(1):
            if recursion_count == row - 2:
                return triangle
            else:
                n = len(triangle[-1])
                middle = []
                for i in range(n-1):

                    sum_from_top = triangle[n-1][i] + triangle[n-1][i+1]
                    middle.append(sum_from_top)
                triangle.append([triangle[1][0], *middle, triangle[1][-1]])
                recursion_count += 1
                recursion(triangle, recursion_count)
        return triangle

    return recursion(triangle)


print(get_magic_triangle(5))
