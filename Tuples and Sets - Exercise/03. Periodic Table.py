# n = int(input())
#
# elements = set()
#
# for _ in range(n):
#     el = input().split()
#     for e in el:
#         elements.add(e)
#
# for element in elements:
#     print(element)
#
# 2 solution

print(*{el for _ in range(int(input())) for el in input().split()}, sep='\n')