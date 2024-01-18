row = int(input())

flatten = []

for i in range(row):
    data = [int(el) for el in input().split(', ')]
    flatten.extend(data)

print(flatten)
