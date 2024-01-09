string = list(input())
stack = []

for char in range(len(string)):
    stack.append(string.pop())

print(''.join(stack))
