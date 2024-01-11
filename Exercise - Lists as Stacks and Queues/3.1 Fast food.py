from collections import deque

food = int(input())
queue = input().split()
orders_list = map(int, queue)
max_order = max(orders_list)

orders = deque(queue)
print(max_order)

while orders:
    order = int(orders[0])
    if food >= order:
        food -= order
        orders.popleft()
    else:
        print(f'Orders left:',*orders)
        break
else:
    print('Orders complete')
