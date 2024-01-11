from collections import deque

food = int(input())
queue = input().split()
orders_list = map(int, queue)
max_order = max(orders_list)

orders = deque(queue)

while orders:
    order = int(orders[0])
    if food >= order:
        food -= order
        orders.popleft()
    else:
        break

print(max_order)
if orders:
    print(f'Orders left: ', end='')
    while orders:
        print(orders.popleft(), end=' ')
else:
    print('Orders complete')
    