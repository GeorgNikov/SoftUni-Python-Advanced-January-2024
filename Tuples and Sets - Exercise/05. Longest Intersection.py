n = int(input())

longest_intersection = []

for _ in range(n):
    a, b = input().split('-')
    first, second = a.split(',')
    third, fourth = b.split(',')
    first_intersection = set()
    second_intersection = set()
    for i in range(int(first), int(second) + 1):
        first_intersection.add(i)
    for i2 in range(int(third), int(fourth) + 1):
        second_intersection.add(i2)

    current_intersection = (first_intersection & second_intersection)
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection
        
print('Longest intersection is [', end='')
print(*longest_intersection, sep=', ', end='')
print(f'] with length {len(longest_intersection)}')
