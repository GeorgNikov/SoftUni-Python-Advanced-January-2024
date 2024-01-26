# delimiter = int(input())
#
# try:
#     result = 10 / delimiter
#     print(result)
# except:
#     print('not possible')
#


numbers = [int(el) for el in input().split(', ')]

n = int(input())

# for _ in range(n):
#     index = int(input())
#
#     if (0 <= index < len(numbers)) or index in range(-1, -len(numbers), -1):
#         print(numbers[index])
#

# Solution try - except

for _ in range(n):
    index = int(input())

    try:
        print(numbers[index])
        print(10/index)
    except (IndexError, ZeroDivisionError):
        print('Invalid input')
    # except ZeroDivisionError:
    #     print('Division of zero is not possible')