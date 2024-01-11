clothes_in_the_box = list(input().split())
rack_capacity = int(input())

racks = []
current_rack = 0

while clothes_in_the_box:
    current_clothe = clothes_in_the_box.pop()
    if current_rack + int(current_clothe) <= rack_capacity:
        current_rack += int(current_clothe)
        if len(clothes_in_the_box) == 0:
            racks.append(current_rack)
            break
    else:
        racks.append(current_rack)
        current_rack = int(current_clothe)
        if len(clothes_in_the_box) == 0:
            racks.append(current_rack)
            break

print(len(racks))