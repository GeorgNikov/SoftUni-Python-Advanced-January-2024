n = int(input())

stack = []

for _ in range(n):
    token = input().split()
    if len(token) == 2:
        _, number = token
        stack.append(int(number))
    elif len(token) == 1:
        number = int(token[0])
        if number == 2 and stack:
            stack.pop()
        elif number == 3 and stack:
            print(max(stack))
        elif number == 4 and stack:
            print(min(stack))

if stack:
    while stack:
        if len(stack) > 1:
            print(stack.pop(), end=', ')
        else:
            print(stack.pop())