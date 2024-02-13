def sort_numbers(numbers):
    for idx in range(len(numbers)):
        min_idx = idx

        for current_idx in range(idx + 1, len(numbers)):
            if numbers[current_idx] < numbers[min_idx]:
                min_idx = current_idx

        numbers[idx], numbers[min_idx] = numbers[min_idx], numbers[idx]

    return ' '.join(str(x) for x in numbers)


number = [int(x) for x in input().split()]

print(sort_numbers(number))




# def sort_numbers(numbers):
#     numbers.sort()
#     return ' '.join(str(x) for x in numbers)
#
#
# number = [int(x) for x in input().split()]
#
# print(sort_numbers(number))
