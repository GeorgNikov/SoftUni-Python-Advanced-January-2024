def best_list_pureness(*args):
    numbers = [x for x in args[0]]
    rotations = []

    for _ in range(args[1] + 1):
        temp_pureness = 0
        for i, el in enumerate(numbers):
            temp_pureness += el * i

        rotations.append(temp_pureness)
        numbers.insert(0, numbers.pop())

    pureness = max(rotations)
    rotation = rotations.index(pureness)

    return f"Best pureness {pureness} after {rotation} rotations"


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
