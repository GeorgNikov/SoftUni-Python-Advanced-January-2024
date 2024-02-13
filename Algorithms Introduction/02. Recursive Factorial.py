def factorial(num):
    if num == 0:
        return 1

    return num * factorial(num - 1)

num = int(input())
print(factorial(num))