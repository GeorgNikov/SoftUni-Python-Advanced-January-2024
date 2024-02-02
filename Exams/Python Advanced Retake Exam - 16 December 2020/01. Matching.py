from collections import deque

males = list([int(x) for x in input().split() if int(x) > 0])
females = deque([int(x) for x in input().split() if int(x) > 0])

matches = 0

while True:
    if not males or not females:
        break

    male = males[-1]
    female = females[0]

    if male <= 0:
        males.pop()
        continue
    if female <= 0:
        females.popleft()
        continue

    if male % 25 == 0:
        males.pop()
        if not males:
            break
        males.pop()
        continue

    if female % 25 == 0:
        females.popleft()
        if not females:
            break
        females.popleft()
        continue

    if male == female:
        males.pop()
        females.popleft()
        matches += 1
    elif male != female:
        females.popleft()
        males[-1] -= 2

print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join([str(male) for male in males[::-1]])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join([str(female) for female in females])}")
else:
    print("Females left: none")