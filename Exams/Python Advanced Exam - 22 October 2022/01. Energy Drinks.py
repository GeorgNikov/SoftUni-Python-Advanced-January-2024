from collections import deque

caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque([int(x) for x in input().split(', ')])
max_caffeine = 300
stamat_caffeine = 0

while caffeine and energy_drinks:
    current_caffeine = caffeine[-1] * energy_drinks[0]
    if current_caffeine <= (max_caffeine - stamat_caffeine):
        caffeine.pop()
        energy_drinks.popleft()
        stamat_caffeine += current_caffeine
    else:
        caffeine.pop()
        energy_drinks.append(energy_drinks.popleft())
        stamat_caffeine -= 30 if stamat_caffeine >= 30 else 0

if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])} ")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")
