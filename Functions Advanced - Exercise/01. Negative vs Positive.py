def stronger_numbers(*args):
    negative_numbers = []
    positive_numbers = []

    for num in args[0]:
        if num.isdigit():
            positive_numbers.append(int(num))
        else:
            negative_numbers.append(int(num))

    if sum(positive_numbers) > abs(sum(negative_numbers)):
        result = f'{sum(negative_numbers)}\n{sum(positive_numbers)}\nThe positives are stronger than the negatives'
    else:
        result = f'{sum(negative_numbers)}\n{sum(positive_numbers)}\nThe negatives are stronger than the positives'

    return result


print(stronger_numbers(input().split()))