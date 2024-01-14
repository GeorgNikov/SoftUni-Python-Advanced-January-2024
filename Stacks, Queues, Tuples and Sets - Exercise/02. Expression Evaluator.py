import functools


def calculate(nums, operator):
    if operator == '-':
        result = functools.reduce(lambda a, b: a - b, nums)
        return result
    elif operator == '+':
        result = functools.reduce(lambda a, b: a + b, nums)
        return result
    elif operator == '*':
        result = functools.reduce(lambda a, b: a * b, nums)
        return result
    elif operator == '/':
        result = functools.reduce(lambda a, b: a / b, nums)
        return int(result)


expression = [x for x in input().split()]
operators = '+-*/'

current_numbers = []
current_operator = ''

for ex in expression:
    if ex not in operators:
        current_numbers.append(int(ex))
        continue
    elif ex in operators:
        current_operator = ex
        result = calculate(current_numbers, current_operator)
        current_numbers = [result]
        current_operator = ''

print(*current_numbers)
