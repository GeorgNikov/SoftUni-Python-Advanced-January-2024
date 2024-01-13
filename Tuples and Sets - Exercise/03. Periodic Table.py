n = int(input())

elements = set()

for _ in range(n):
    el = input().split()
    for e in el:
        elements.add(e)

for element in elements:
    print(element)