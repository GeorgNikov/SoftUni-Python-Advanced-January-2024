n = int(input())

names_even = set()
names_odd = set()

for i in range(1, n+1):
    name = sum(ord(char) for char in input()) // i
    if name % 2 == 0:
        names_even.add(name)
    else:
        names_odd.add(name)

if sum(names_even) == sum(names_odd):
    print(*names_even | names_odd, sep=', ')
elif sum(names_odd) > sum(names_even):
    print(*names_odd - names_even, sep=', ')
elif sum(names_even) > sum(names_odd):
    print(*names_even ^ names_odd, sep=', ')
