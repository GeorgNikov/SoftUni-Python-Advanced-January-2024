from collections import deque

monster = deque([int(x) for x in input().split(',')])
soldier = [int(x) for x in input().split(',')]
killed_monsters = 0

while monster and soldier:
    current_monster = monster[0]
    current_soldier = soldier[-1]

    if current_soldier >= current_monster:
        soldier[-1] -= monster.popleft()
        if len(soldier) > 1 and soldier[-1] > 0:
            remaining_strike = soldier.pop()
            soldier[-1] += remaining_strike
        elif soldier[-1] == 0:
            soldier.pop()

        killed_monsters += 1
    else:
        monster[0] -= current_soldier
        soldier.pop()
        monster.append(monster.popleft())

if not monster:
    print("All monsters have been killed!")

if not soldier:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")