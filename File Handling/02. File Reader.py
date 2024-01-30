import os

path = os.path.join("resources", "numbers.txt")

file = open(path)
total_amount = 0

for line in file.readlines():
    total_amount += int(line.strip())

print(total_amount)