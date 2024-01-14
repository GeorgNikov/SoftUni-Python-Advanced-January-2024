from collections import deque
import functools


def calculate(nums, operator):
    if operator == '-':
        return functools.reduce(lambda a, b: a - b, nums)
    elif operator == '+':
        return functools.reduce(lambda a, b: a + b, nums)
    elif operator == '*':
        return functools.reduce(lambda a, b: a * b, nums)
    elif operator == '/':
        return functools.reduce(lambda a, b: a / b, nums)


working_bees = deque(map(int, input().split()))
nectar_bees = list(map(int, input().split()))
process = deque(input().split())

honey = 0

while working_bees and len(nectar_bees):
    bees = working_bees.popleft()
    nectar = nectar_bees.pop()

    if bees > nectar:
        working_bees.appendleft(bees)
        continue

    elif bees <= nectar:
        operator = process.popleft()
        if operator == '/' and nectar == 0:
            continue
        result = calculate([bees, nectar], operator)
        honey += abs(result)

print(f'Total honey made: {honey}')

if len(nectar_bees):
    print(f"Nectar left: {', '.join(map(str, nectar_bees))}", sep=', ')

if working_bees:
    print(f"Bees left: {', '.join(map(str, working_bees))}", sep=', ')
