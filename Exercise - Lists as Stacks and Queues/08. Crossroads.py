from collections import deque

green_light_time = int(input())
free_window = int(input())
cars = deque()

crossed = 0
crashed = False


command = input()

while command != 'END':
    if command == 'green':
        if cars:
            current_car = cars.popleft()
            free_time = green_light_time - len(current_car)
            while free_time > 0:
                crossed += 1
                if cars:
                    current_car = cars.popleft()
                    free_time -= len(current_car)
                else:
                    break
            if free_time == 0:
                crossed += 1
            if free_window >= abs(free_time):
                if free_time < 0:
                    crossed += 1
            else:
                hit = free_window + free_time
                print('A crash happened!')
                print(f'{current_car} was hit at {current_car[hit]}.')
                crashed = True
                break
    else:
        cars.append(command)
    command = input()

if not crashed:
    print('Everyone is safe.')
    print(f'{crossed} total cars passed the crossroads.')
