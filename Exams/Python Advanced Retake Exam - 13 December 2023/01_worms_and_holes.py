from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])

all_worms_count = len(worms)
count = 0

while worms and holes:
    worm = worms[-1]
    hole = holes[0]

    if worm == hole:
        worms.pop()
        holes.popleft()
        count += 1

    else:
        holes.popleft()
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()

if count:
    print(f"Matches: {count}")
else:
    print(F"There are no matches.")

if not worms and count == all_worms_count:
    print("Every worm found a suitable hole!")
elif not worms and count < all_worms_count:
    print("Worms left: none")
else:
    print(f"Worms left: {', '.join([str(x) for x in worms])}")

if holes:
    print(f"Holes left: {', '.join([str(x) for x in holes])}")
else:
    print("Holes left: none")
