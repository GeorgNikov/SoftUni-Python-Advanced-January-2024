from collections import deque

bullet_price = int(input())
gun_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence = int(input())
count = 0
bullets_count = 0

while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks.popleft()

    if current_lock >= current_bullet:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(current_lock)

    count += 1
    bullets_count += 1

    if not bullets:
        break

    if count == gun_barrel:
        print("Reloading!")
        count = 0

earned = intelligence - (bullet_price * bullets_count)

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")