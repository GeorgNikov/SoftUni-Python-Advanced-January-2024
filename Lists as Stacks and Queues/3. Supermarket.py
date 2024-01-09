from collections import deque

client = input()
customers = deque()

while client != 'End':
    if client == 'Paid':
        while customers:
            print(customers.popleft())
    else:
        customers.append(client)

    client = input()

print(f'{len(customers)} people remaining.')
