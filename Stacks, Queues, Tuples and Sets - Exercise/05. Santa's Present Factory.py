from collections import deque


def craft_gift(toys):
    if (toys["Doll"][1] >= 1 and toys["Wooden train"][1] >= 1) or (toys["Teddy bear"][1] >= 1 and toys["Bicycle"][1] >= 1):
        return True
    return False


material = [int(num) for num in input().split()]
magic = deque(int(num) for num in input().split())

toys = {
    "Bicycle": [400, 0],
    "Doll": [150, 0],
    "Teddy bear": [300, 0],
    "Wooden train": [250, 0],

}

while len(material) and magic:
    current_material = material.pop()
    current_magic = magic.popleft()

    product = current_material * current_magic
    if product < 0:
        result = current_material + current_magic
        material.append(result)

    elif product > 0:
        for key, item in toys.items():
            if product == item[0]:
                toys[key][1] += 1
                break
        else:
            material.append(current_material + 15)

    elif (current_material == 0 and current_magic == 0) or current_material == 0 or current_magic == 0:
        if current_material > 0:
            material.append(current_material)
        elif current_magic > 0:
            magic.appendleft(current_magic)
        continue

if craft_gift(toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if material:
    material.reverse()
    print(f"Materials left: {', '.join(map(str, material))}", sep=', ')

if magic:
    print(f"Magic left: {', '.join(map(str, magic))}", sep=', ')

for key, item in toys.items():
    if item[1] > 0:
        print(f'{key}: {item[1]}')
