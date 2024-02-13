def accommodate_new_pets(capacity, max_weight, *pets):
    accommodated_pets = {}
    are_all_accommodated = True

    for pet_name, pet_weight in pets:
        if not capacity:
            are_all_accommodated = False
            break

        if pet_weight <= max_weight:
            if pet_name not in accommodated_pets:
                accommodated_pets[pet_name] = 0
            accommodated_pets[pet_name] += 1
            capacity -= 1

    result = ''

    if are_all_accommodated:
        result += f"All pets are accommodated! Available capacity: {capacity}.\n"
    else:
        result += "You did not manage to accommodate all pets!\n"

    result += "Accommodated pets:\n"

    if accommodated_pets:
        for pet_name, pet_weight in sorted(accommodated_pets.items(), key=lambda kvp: kvp[0]):
            result += f"{pet_name}: {pet_weight}\n"

    return result[:-1]


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print()
print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print()
print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))