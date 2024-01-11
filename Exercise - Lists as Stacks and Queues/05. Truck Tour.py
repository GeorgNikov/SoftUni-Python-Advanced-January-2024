from collections import deque

pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

pumps_data_copy = pumps_data.copy()
tank = 0
index = 0

while pumps_data_copy:
    petrol, distance = pumps_data_copy.popleft()

    tank += petrol
    if tank >= distance:
        tank -= distance
    else:
        pumps_data.rotate(-1)
        pumps_data_copy = pumps_data.copy()
        index += 1
        tank = 0

print(index)

# Solution 1 - Not working

# petrol_pumps = int(input())
# tank = 0
# start_point = 0
#
# for i in range(petrol_pumps):
#     data = input().split()
#     amount, distance = data
#     if int(amount) + tank > int(distance):
#         tank += int(amount)
#         tank -= int(distance)
#     else:
#         start_point = i + 1
#
# print(start_point)
