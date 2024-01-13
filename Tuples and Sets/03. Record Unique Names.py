n = int(input())

names = set()

for _ in range(n):
    name = input()
    names.add(name)

for name in names:
    print(name)

# Second solution

# n = int(input())
#
# names = []
#
# for _ in range(n):
#     name = input()
#     names.append(name)
#
# for name in set(names):
#     print(name)
