# Add int values in row and cols
rows, cols = [int(el) for el in input().split()]
# Create matrix
matrix = [input().split() for _ in range(rows)]
# Get variables str, *int
command_type, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]