from collections import deque


materials = list([int(x) for x in input().split()])
magic = deque([int(x) for x in input().split()])

gifts = {
    "Gemstone": [100, 199, 0],
    "Porcelain Sculpture": [200, 299, 0],
    "Gold": [300, 399, 0],
    "Diamond Jewellery": [400, 499, 0],
}

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    mixing = current_material + current_magic

    if mixing < 100:
        if mixing % 2 == 0:
            mixing = current_material * 2 + current_magic * 3
        else:
            mixing = mixing * 2

    elif mixing > 499:
        mixing *= 0.5

    for gift_name in gifts:
        if gifts[gift_name][0] <= mixing <= gifts[gift_name][1]:
            gifts[gift_name][2] += 1
            break


if ((gifts["Gemstone"][2] > 0 and gifts["Porcelain Sculpture"][2] > 0)
        or (gifts["Gold"][2] > 0 and gifts["Diamond Jewellery"][2] > 0)):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")

if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for key, value in sorted(gifts.items()):
    if value[2] > 0:
        print(f"{key}: {value[2]}")
