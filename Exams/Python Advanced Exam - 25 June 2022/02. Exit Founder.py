from collections import deque

players = deque(input().split(', '))
SIZE= 6

field = []
resting = {"Tom": 0, "Jerry": 0}

for _ in range(SIZE):         # mapping field
    field.append([x for x in input().split()])

while True:
    row, col = eval(input())
    current_player = players[0]

    if resting[current_player] == 1:
        players.rotate()
        resting[current_player] = 0
        continue

    if field[row][col] == 'W':
        print(f"{current_player} hits a wall and needs to rest.")
        resting[current_player] = 1
        players.rotate()

    elif field[row][col] == 'T':
        print(f"{current_player} is out of the game! The winner is {players[-1]}.")
        break

    elif field[row][col] == 'E':
        print(f"{current_player} found the Exit and wins the game!")
        break

    else:
        players.rotate()