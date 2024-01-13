n, m = input().split()

set_a = set()
set_b = set()

for _ in range(int(n)):
    set_a.add(int(input()))

for _ in range(int(m)):
    set_b.add(int(input()))

new_set = (set_a & set_b)
print(*new_set, sep='\n')
