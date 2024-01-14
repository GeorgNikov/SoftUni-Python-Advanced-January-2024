from collections import deque

chocolate = list(map(int, input().split(', ')))
milk = deque(map(int, input().split(', ')))

milkshakes = 0

while len(chocolate) and milk and milkshakes < 5:

    current_chocolate = int(chocolate.pop())
    current_milk = int(milk.popleft())

    if current_chocolate <= 0 and current_milk <= 0:
        continue

    elif current_milk <= 0:
        chocolate.append(current_chocolate)
        continue

    elif current_chocolate <= 0:
        milk.appendleft(current_milk)
        continue

    if current_chocolate == current_milk:
        milkshakes += 1
    else:
        milk.append(current_milk)
        chocolate.append(current_chocolate - 5)

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if chocolate:
    print(f"Chocolate: {', '.join(map(str, chocolate))}", sep=', ')
else:
    print('Chocolate: empty')

if milk:
    print(f"Milk: {', '.join(map(str, milk))}", sep=', ')
else:
    print('Milk: empty')
