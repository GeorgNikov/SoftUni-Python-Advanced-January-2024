# first = set(input().split())
# second = set(input().split())
first = set((map(int, input().split())))
second = set((map(int, input().split())))

n = int(input())

for _ in range(n):

    token = input().split()
    command = [token[0], token[1]]
    token.pop(0)
    token.pop(0)
    numbers = set([int(x) for x in token])

    if command[0] == 'Add':
        select_set = command[1]
        if select_set == 'First':
            [first.add(el) for el in numbers]
        elif select_set == 'Second':
            [second.add(el) for el in numbers]

    elif command[0] == 'Remove':
        select_set = command[1]
        if select_set == 'First':
            [first.remove(el) for el in numbers if el in first]
        elif select_set == 'Second':
            [second.remove(el) for el in numbers if el in second]

    elif command[0] == 'Check':
        if first.issubset(second) or second.issubset(first):
            print(True)
            continue
        print(False)

print(", ".join([str(num) for num in sorted(first)]))
print(", ".join([str(num) for num in sorted(second)]))
