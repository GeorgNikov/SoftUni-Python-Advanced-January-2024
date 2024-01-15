# n, m = input().split()
#
# set_a = set()
# set_b = set()
#
# for _ in range(int(n)):
#     set_a.add(int(input()))
#
# for _ in range(int(m)):
#     set_b.add(int(input()))
#
# new_set = (set_a & set_b)
# print(*new_set, sep='\n')
#

# Solution 2
n, m = [int(x) for x in input().split()]

first_set = {input() for _ in range(n)}
second_set = {input() for _ in range(m)}

print(*first_set.intersection(second_set), sep='\n')
