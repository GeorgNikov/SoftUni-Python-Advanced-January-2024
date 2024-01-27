def check_pouch():
    if bomb_pouch["Datura Bombs"] >= 3 and bomb_pouch["Cherry Bombs"] >= 3 and bomb_pouch["Smoke Decoy Bombs"] >= 3:
        return True
    return False


from collections import deque

bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = list([int(x) for x in input().split(', ')])

materials = {
    "Datura Bombs": 40,
    "Cherry Bombs": 60,
    "Smoke Decoy Bombs": 120,
}

bomb_pouch = {
    "Cherry Bombs": 0,
    "Datura Bombs": 0,
    "Smoke Decoy Bombs": 0,
}

while bomb_effects and bomb_casings:
# Start making bombs!!1
    if check_pouch():
        break

    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()
    bomb = effect + casing

    for key, value in materials.items():
        if bomb == value:
            bomb_pouch[key] += 1
            break
    else:
        casing -= 5
        bomb_casings.append(casing)
        bomb_effects.appendleft(effect)

if check_pouch():
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects]) if bomb_effects else 'empty'}")
print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings]) if bomb_casings else 'empty'}")

for key, value in bomb_pouch.items():
    print(f"{key}: {value}")
