from collections import deque


def check_firework_show():
    if fireworks["Palm Fireworks"] >= 3 and fireworks["Willow Fireworks"] >= 3 and fireworks["Crossette Fireworks"] >= 3:
        return True
    return False


def craft_firework(fire, power):    # Craft fireworks
    total = fire + power

    if total % 3 == 0 and total % 5 == 0:
        return 'Crossette Fireworks'
    elif total % 3 == 0 and total % 5 != 0:
        return 'Palm Fireworks'
    elif total % 3 != 0 and total % 5 == 0:
        return 'Willow Fireworks'
    return


firework_effects = deque([int(x) for x in input().split(', ') if int(x) > 0])
explosive_power = list([int(x) for x in input().split(', ') if int(x) > 0])

fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0,
}

# Start making fireworks
while firework_effects and explosive_power and not check_firework_show():
    firework = firework_effects[0]
    explosive = explosive_power[-1]

    result = craft_firework(firework, explosive)
    if result in fireworks:
        fireworks[result] += 1
        firework_effects.popleft()
        explosive_power.pop()
    else:
        firework_effects[0] -= 1
        if firework_effects[0] > 0:
            firework_effects.append(firework_effects.popleft())
            continue
        firework_effects.popleft()

if check_firework_show():
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")

for key, value in fireworks.items():
    print(f"{key}: {value}")
