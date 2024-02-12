from collections import deque
import operator

textiles = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]


healing_items = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100,
}

crafting_items = {
    "Bandage": 0,
    "MedKit": 0,
    "Patch": 0,
}

while textiles and medicaments:
    current_textile = textiles[0]
    current_medicament = medicaments[-1]
    craft = current_textile + current_medicament

    for key, value in healing_items.items():
        if craft in healing_items.values() or craft > 100:
            if craft == value:
                crafting_items[key] += 1
                medicaments.pop()
                textiles.popleft()
                break

            elif craft > 100:
                crafting_items["MedKit"] += 1
                diff = craft - 100
                if len(textiles) > 0:
                    textiles.popleft()
                if len(medicaments) > 0:
                    medicaments.pop()
                medicaments[-1] += diff
                break
        else:
            textiles.popleft()
            medicaments[-1] += 10
            break

if not medicaments and not textiles:
    print("Textiles and medicaments are both empty.")
else:
    if not textiles:
        print("Textiles are empty.")

    elif not medicaments:
        print("Medicaments are empty.")

sorted_crafting_items = dict(sorted(crafting_items.items(), key=operator.itemgetter(1), reverse=True))

for key, value in sorted_crafting_items.items():
    if value > 0:
        print(f"{key} - {value}")

if textiles:
    print(f"Textiles left: {', '.join([str(x) for x in textiles])}")
if medicaments:
    print(f"Medicaments left: {', '.join([str(x) for x in reversed(medicaments)])}")
