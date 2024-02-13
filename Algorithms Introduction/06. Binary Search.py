def find_index(nums, number):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid_el = nums[mid_idx]

        if mid_el == number:
            return mid_idx
        elif mid_el < number:
            left = mid_idx + 1
        elif mid_el > number:
            right = mid_idx - 1

    return -1


nums = [int(x) for x in input().split()]
searched_num = int(input())

print(find_index(nums, searched_num))