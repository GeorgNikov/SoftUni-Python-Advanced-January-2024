# Add int values in row and cols
rows, cols = [int(el) for el in input().split()]
# Create matrix
matrix = [input().split() for _ in range(rows)]
# Get variables str, *int
command_type, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]

# Function *args always return tuple()
def func(*args):   #     -> (arg1, arg2, arg3 ...)
    pass
# Change placed of elements -> [1, 3], [2, 4]
mat = [[1, 2], [3, 4]]
res = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
print(res)

# From input '(0, 2)' get coordinates like [1, 2]
[r, c] = map(lambda x: int(x), input()[1:][:-1].split(', '))

# How can you check if all rows in a matrix mat have the same length
res =all(len(row) == len(mat[0]) for row in mat)
res1 = len(set(len(row) for row in mat)) == 1

#Consider the recursive function below:
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
factorial(5)    # 120

#For the recursive function to determine the nth Fibonacci number: DO NOT USE
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
fibonacci(6)    #return 8 or  13