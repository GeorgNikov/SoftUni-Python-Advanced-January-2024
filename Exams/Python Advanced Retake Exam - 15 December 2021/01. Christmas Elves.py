from collections import deque

elfs_energy = deque([int(x) for x in input().split()])
materials = list([int(x) for x in input().split()])

day = 0             # Current day
toys = 0            # Total toys
energy = 0          # Total energy spent
cookies = 1         # Added +1 to the energy
chocolate = 2       # Double the energy

while materials and elfs_energy:
    current_elf_energy = elfs_energy.popleft()
    current_material = materials.pop()

    if current_elf_energy < 5:
        materials.append(current_material)
        continue

    day += 1

    if current_elf_energy >= current_material:

        if day % 3 == 0 and day % 5 == 0:
            if current_elf_energy >= current_material * 2:
                current_elf_energy -= current_material * 2
                energy += current_material * 2
            else:
                current_elf_energy *= 2
                materials.append(current_material)
                energy += current_elf_energy - current_material * 2
            elfs_energy.append(current_elf_energy)

        elif day % 3 == 0:    # Every third day
            if current_elf_energy >= current_material * 2:
                toys += 2
                energy += current_material * 2
                current_elf_energy -= current_material * 2 - cookies
            else:
                current_elf_energy *= chocolate
                materials.append(current_material)
            elfs_energy.append(current_elf_energy)

        elif day % 5 == 0:      # every five day
            if current_elf_energy >= current_material:
                energy += current_material
                current_elf_energy -= current_material
            else:
                materials.append(current_material)
            elfs_energy.append(current_elf_energy)

        else:   # every day
            toys += 1
            energy += current_material
            current_elf_energy -= current_material - cookies
            elfs_energy.append(current_elf_energy)

    else:
        materials.append(current_material)
        elfs_energy.append(current_elf_energy * chocolate)

print(f"Toys: {toys}")
print(f"Energy: {energy}")

if elfs_energy:
    print(f"Elves left: {', '.join([str(x) for x in elfs_energy])}")

if materials:
    print(f"Boxes left: {', '.join([str(x) for x in materials])}")

