from collections import deque
import time
client = input()
customers = deque()

start_time = time.time()

while client != 'End':
    if client == 'Paid':
        while customers:
            print(customers.popleft())
    else:
        customers.append(client)

    client = input()

print(f'{len(customers)} people remaining.')
print(time.time() - start_time)
