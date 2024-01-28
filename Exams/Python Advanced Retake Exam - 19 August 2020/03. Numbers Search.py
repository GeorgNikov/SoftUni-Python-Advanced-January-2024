def numbers_searching(*args):
    numbers = set([x for x in range(min(args), max(args) + 1)])
    duplicate_numbers = set([x for x in args if args.count(x) > 1])
    duplicate_numbers_sorted = sorted(duplicate_numbers)
    searching_number = numbers.difference(set(args))

    return [*searching_number, [*duplicate_numbers_sorted]]



print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))