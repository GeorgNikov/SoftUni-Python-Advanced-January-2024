from collections import deque

water = int(input())

name = input()
people = deque()

while name != 'Start':
    people.append(name)
    name = input()

command = input()

while command != 'End':
    data = command.split()
    if len(data) == 1:
        litters_requested = int(data[0])
        person = people.popleft()

        if water >= litters_requested:
            print(f'{person} got water')
            water -= litters_requested
        else:
            print(f'{person} must wait')
    else:
        _, litters_to_add = data
        water += int(litters_to_add)

    command = input()

print(f'{water} liters left')
