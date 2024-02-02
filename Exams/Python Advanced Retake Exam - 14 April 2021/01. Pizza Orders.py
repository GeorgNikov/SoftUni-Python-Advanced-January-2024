from collections import deque

orders = deque([int(x) for x in input().split(', ') if int(x) > 0])
employees = list([int(x) for x in input().split(', ')])

total_pizza_made = 0

while orders and employees:
    current_order = orders[0]
    current_employer = employees[-1]
    if current_order > 10:
        orders.popleft()
        continue

    if current_employer >= current_order:
        total_pizza_made +=  current_order
        orders.popleft()
        employees.pop()

    elif current_employer < current_order:
        total_pizza_made += current_employer
        orders[0] -= current_employer
        employees.pop()

if orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in orders])}")

else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza_made}")
    print(f"Employees: {', '.join([str(x) for x in employees])}")
