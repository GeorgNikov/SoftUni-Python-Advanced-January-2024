from collections import deque

fuel = [int(x) for x in input().split()]
consumption = deque([int(x) for x in input().split()])
needed_fuel = deque([int(x) for x in input().split()])

altitude = 0
reached_altitude = []

while fuel and consumption and needed_fuel:
    current_fuel = fuel[-1]
    current_consumption = consumption[0]
    current_needed_fuel = needed_fuel[0]

    if current_fuel - current_consumption >= current_needed_fuel:
        fuel.pop()
        consumption.popleft()
        needed_fuel.popleft()
        altitude += 1
        print(f"John has reached: Altitude {altitude}")
        reached_altitude.append(f"Altitude {altitude}")

    else:
        print(f"John did not reach: Altitude {altitude + 1}")
        break

if needed_fuel and altitude:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(x for x in reached_altitude)}")
elif needed_fuel and not altitude:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")
else:
    print("John has reached all the altitudes and managed to reach the top!")