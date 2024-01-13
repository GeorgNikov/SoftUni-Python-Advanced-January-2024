n = int(input())

users = set()

for _ in range(n):
    users.add(input())

print(*users, sep='\n')