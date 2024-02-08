from collections import deque

bowls_of_ramen = list([int(x) for x in input().split(', ')])
customers = deque([int(x) for x in input().split(', ')])

while bowls_of_ramen and customers:
    current_bow = bowls_of_ramen[-1]
    current_customers = customers[0]

    if current_bow == current_customers:
        bowls_of_ramen.pop()
        customers.popleft()

    elif current_bow > current_customers:
        bowls_of_ramen[-1] -= current_customers
        customers.popleft()

    elif current_customers > current_bow:
        customers[0] -= current_bow
        bowls_of_ramen.pop()

    if not customers:
        print("Great job! You served all the customers.")

if bowls_of_ramen:
    print(f"Bowls of ramen left: {', '.join([str(x) for x in bowls_of_ramen])}")
if customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
