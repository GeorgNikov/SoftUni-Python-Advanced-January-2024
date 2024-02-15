from collections import deque

times = deque([int(x) for x in input().split()])
tasks = [int(x) for x in input().split()]

rubber_ducky = {
    "Darth Vader Ducky": [0, 60],
    "Thor Ducky": [61, 120],
    "Big Blue Rubber Ducky": [121, 180],
    "Small Yellow Rubber Ducky": [181, 240],
}

rubber_ducky_count = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0,
}

while times and tasks:
    current_time = times[0]
    current_task = tasks[-1]
    current_mix = current_time * current_task

    for key, duck in rubber_ducky.items():
        if current_mix > 240:
            times.append(times.popleft())
            tasks[-1] -= 2
            break

        elif current_mix >= duck[0] and current_mix <= duck[1]:
            rubber_ducky_count[key] += 1
            times.popleft()
            tasks.pop()

if not times and not tasks:
    print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for duck, count in rubber_ducky_count.items():
    print(f"{duck}: {count}")